import xmltodict
import pyexiv2  # type: ignore
import datetime
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any, Set, Tuple
import re
import json
from fractions import Fraction
from geopic_tag_reader import camera
import timezonefinder  # type: ignore
import pytz

# This is a fix for invalid MakerNotes leading to picture not read at all
# https://github.com/LeoHsiao1/pyexiv2/issues/58
pyexiv2.set_log_level(4)

tz_finder = timezonefinder.TimezoneFinder()


@dataclass
class CropValues:
    """Cropped equirectangular pictures metadata

    Attributes:
        fullWidth (int): Full panorama width
        fullHeight (int): Full panorama height
        width (int): Cropped area width
        height (int): Cropped area height
        left (int): Cropped area left offset
        top (int): Cropped area top offset
    """

    fullWidth: int
    fullHeight: int
    width: int
    height: int
    left: int
    top: int


@dataclass
class GeoPicTags:
    """Tags associated to a geolocated picture

    Attributes:
        lat (float): GPS Latitude (in WGS84)
        lon (float): GPS Longitude (in WGS84)
        ts (datetime): The capture date (date & time with timezone)
        heading (int): Picture heading (in degrees, North = 0°, East = 90°, South = 180°, West = 270°)
        type (str): The kind of picture (flat, equirectangular)
        make (str): The camera manufacturer name
        model (str): The camera model name
        focal_length (float): The camera focal length (in mm)
        crop (CropValues): The picture cropped area metadata (optional)
        exif (dict[str, str]): Raw EXIF tags from picture (following Exiv2 naming scheme, see https://exiv2.org/metadata.html)
        tagreader_warnings (list[str]): List of thrown warnings during metadata reading
        altitude (float): altitude (in m) (optional)


    Implementation note: this needs to be sync with the PartialGeoPicTags structure
    """

    lat: float
    lon: float
    ts: datetime.datetime
    heading: Optional[int]
    type: str
    make: Optional[str]
    model: Optional[str]
    focal_length: Optional[float]
    crop: Optional[CropValues]
    exif: Dict[str, str] = field(default_factory=lambda: {})
    tagreader_warnings: List[str] = field(default_factory=lambda: [])
    altitude: Optional[float] = None


class InvalidExifException(Exception):
    """Exception for invalid EXIF information from image"""

    def __init__(self, msg):
        super().__init__(msg)


@dataclass
class PartialGeoPicTags:
    """Tags associated to a geolocated picture when not all tags have been found

    Implementation note: this needs to be sync with the GeoPicTags structure
    """

    lat: Optional[float] = None
    lon: Optional[float] = None
    ts: Optional[datetime.datetime] = None
    heading: Optional[int] = None
    type: Optional[str] = None
    make: Optional[str] = None
    model: Optional[str] = None
    focal_length: Optional[float] = None
    crop: Optional[CropValues] = None
    exif: Dict[str, str] = field(default_factory=lambda: {})
    tagreader_warnings: List[str] = field(default_factory=lambda: [])
    altitude: Optional[float] = None


class PartialExifException(Exception):
    """
    Exception for partial / missing EXIF information from image

    Contains a PartialGeoPicTags with all tags that have been read and the list of missing tags
    """

    def __init__(self, msg, missing_mandatory_tags: Set[str], partial_tags: PartialGeoPicTags):
        super().__init__(msg)
        self.missing_mandatory_tags = missing_mandatory_tags
        self.tags = partial_tags


def readPictureMetadata(picture: bytes) -> GeoPicTags:
    """Extracts metadata from picture file

    Args:
        picture (bytes): Picture file

    Returns:
        GeoPicTags: Extracted metadata from picture
    """

    warnings = []
    img = pyexiv2.ImageData(picture)
    data = {}
    data.update(img.read_exif())
    data.update(img.read_xmp())

    imgComment = img.read_comment()
    if imgComment is not None and len(imgComment.strip()) > 0:
        data["Exif.Photo.UserComment"] = imgComment
    img.close()

    # Read Mapillary tags
    if "Exif.Image.ImageDescription" in data:
        # Check if data can be read
        imgDesc = data["Exif.Image.ImageDescription"]
        try:
            imgDescJson = json.loads(imgDesc)
            data.update(imgDescJson)
        except:
            pass

    # Sanitize charset information
    for k, v in data.items():
        if isinstance(v, str):
            data[k] = re.sub(r"charset=[^\s]+", "", v).strip()

    # Parse latitude/longitude
    lat, lon, llw = decodeLatLon(data, "Exif.GPSInfo")
    if len(llw) > 0:
        warnings.extend(llw)

    if lat is None:
        lat, lon, llw = decodeLatLon(data, "Xmp.exif")
        if len(llw) > 0:
            warnings.extend(llw)

    if lat is None and isExifTagUsable(data, "MAPLatitude", float) and isExifTagUsable(data, "MAPLongitude", float):
        lat = float(data["MAPLatitude"])
        lon = float(data["MAPLongitude"])

    # Check coordinates validity
    if lat is not None and (lat < -90 or lat > 90):
        raise InvalidExifException("Read latitude is out of WGS84 bounds (should be in [-90, 90])")
    if lon is not None and (lon < -180 or lon > 180):
        raise InvalidExifException("Read longitude is out of WGS84 bounds (should be in [-180, 180])")

    # Parse date/time
    d, llw = decodeGPSDateTime(data, "Exif.GPSInfo", lat, lon)

    if len(llw) > 0:
        warnings.extend(llw)

    if d is None:
        d, llw = decodeGPSDateTime(data, "Xmp.exif", lat, lon)
        if len(llw) > 0:
            warnings.extend(llw)

    for exifField in [
        "Exif.Image.DateTimeOriginal",
        "Exif.Photo.DateTimeOriginal",
        "Exif.Image.DateTime",
        "Xmp.GPano.SourceImageCreateTime",
    ]:
        if d is None:
            d, llw = decodeDateTimeOriginal(data, exifField, lat, lon)
            if len(llw) > 0:
                warnings.extend(llw)

        if d is not None:
            break

    if d is None and isExifTagUsable(data, "MAPGpsTime"):
        try:
            year, month, day, hour, minutes, seconds, milliseconds = [int(dp) for dp in data["MAPGpsTime"].split("_")]
            d = datetime.datetime(
                year,
                month,
                day,
                hour,
                minutes,
                seconds,
                milliseconds * 1000,
                tzinfo=datetime.timezone.utc,
            )

        except Exception as e:
            warnings.append("Skipping Mapillary date/time as it was not recognized:\n\t" + str(e))

    # Heading
    heading = None
    if isExifTagUsable(data, "Xmp.GPano.PoseHeadingDegrees", float) and isExifTagUsable(data, "Exif.GPSInfo.GPSImgDirection", Fraction):
        gpsDir = int(round(float(Fraction(data["Exif.GPSInfo.GPSImgDirection"]))))
        gpanoHeading = int(round(float(data["Xmp.GPano.PoseHeadingDegrees"])))
        if gpsDir > 0 and gpanoHeading == 0:
            heading = gpsDir
        elif gpsDir == 0 and gpanoHeading > 0:
            heading = gpanoHeading
        else:
            if gpsDir != gpanoHeading:
                warnings.append("Contradicting heading values found, GPSImgDirection value is used")
            heading = gpsDir

    elif isExifTagUsable(data, "Xmp.GPano.PoseHeadingDegrees", float):
        heading = int(round(float(data["Xmp.GPano.PoseHeadingDegrees"])))

    elif isExifTagUsable(data, "Exif.GPSInfo.GPSImgDirection", Fraction):
        heading = int(round(float(Fraction(data["Exif.GPSInfo.GPSImgDirection"]))))

    elif "MAPCompassHeading" in data and isExifTagUsable(data["MAPCompassHeading"], "TrueHeading", float):
        heading = int(round(float(data["MAPCompassHeading"]["TrueHeading"])))

    # Make and model
    make = data.get("Exif.Image.Make") or data.get("MAPDeviceMake")
    model = data.get("Exif.Image.Model") or data.get("MAPDeviceModel")

    if make is not None:
        make = decodeMakeModel(make).strip()

    if model is not None:
        model = decodeMakeModel(model).strip()

    if make is not None and model is not None and model.startswith(make) and len(model) > len(make):
        model = model.replace(make, "").strip()

    # Focal length
    focalLength = None
    if isExifTagUsable(data, "Exif.Image.FocalLength", Fraction):
        focalLength = float(Fraction(data["Exif.Image.FocalLength"]))
    elif isExifTagUsable(data, "Exif.Photo.FocalLength", Fraction):
        focalLength = float(Fraction(data["Exif.Photo.FocalLength"]))

    # Cropped pano data
    crop = None
    if (
        isExifTagUsable(data, "Xmp.GPano.FullPanoWidthPixels", int)
        and isExifTagUsable(data, "Xmp.GPano.FullPanoHeightPixels", int)
        and isExifTagUsable(data, "Xmp.GPano.CroppedAreaImageWidthPixels", int)
        and isExifTagUsable(data, "Xmp.GPano.CroppedAreaImageHeightPixels", int)
        and isExifTagUsable(data, "Xmp.GPano.CroppedAreaLeftPixels", int)
        and isExifTagUsable(data, "Xmp.GPano.CroppedAreaTopPixels", int)
    ):
        fw = int(data["Xmp.GPano.FullPanoWidthPixels"])
        fh = int(data["Xmp.GPano.FullPanoHeightPixels"])
        w = int(data["Xmp.GPano.CroppedAreaImageWidthPixels"])
        h = int(data["Xmp.GPano.CroppedAreaImageHeightPixels"])
        l = int(data["Xmp.GPano.CroppedAreaLeftPixels"])
        t = int(data["Xmp.GPano.CroppedAreaTopPixels"])

        if fw > w or fh > h:
            crop = CropValues(fw, fh, w, h, l, t)

    elif (
        isExifTagUsable(data, "Xmp.GPano.CroppedAreaImageWidthPixels", int)
        or isExifTagUsable(data, "Xmp.GPano.CroppedAreaImageHeightPixels", int)
        or isExifTagUsable(data, "Xmp.GPano.CroppedAreaLeftPixels", int)
        or isExifTagUsable(data, "Xmp.GPano.CroppedAreaTopPixels", int)
    ):
        raise InvalidExifException("EXIF tags contain partial cropped area metadata")

    # Type
    pic_type = None
    # 360° based on GPano EXIF tag
    if isExifTagUsable(data, "Xmp.GPano.ProjectionType"):
        pic_type = data["Xmp.GPano.ProjectionType"]
    # 360° based on known models
    elif camera.is_360(make, model, data.get("Exif.Photo.PixelXDimension"), data.get("Exif.Photo.PixelYDimension")):
        pic_type = "equirectangular"
    # Flat by default
    else:
        pic_type = "flat"

    # Altitude
    altitude = None
    if isExifTagUsable(data, "Exif.GPSInfo.GPSAltitude", Fraction):
        altitude_raw = int(round(float(Fraction(data["Exif.GPSInfo.GPSAltitude"]))))
        ref = -1 if data.get("Exif.GPSInfo.GPSAltitudeRef") == "1" else 1
        altitude = altitude_raw * ref

    errors = []
    missing_fields = set()
    if not lat or not lon:
        errors.append("No GPS coordinates or broken coordinates in picture EXIF tags")
        if not lat:
            missing_fields.add("lat")
        if not lon:
            missing_fields.add("lon")
    if d is None:
        errors.append("No valid date in picture EXIF tags")
        missing_fields.add("datetime")

    if errors:
        raise PartialExifException(
            " and ".join(errors),
            missing_fields,
            PartialGeoPicTags(
                lat,
                lon,
                d,
                heading,
                pic_type,
                make,
                model,
                focalLength,
                crop,
                exif=data,
                tagreader_warnings=warnings,
                altitude=altitude,
            ),
        )

    assert lon and lat and d  # at this point all those fields cannot be null
    return GeoPicTags(
        lat,
        lon,
        d,
        heading,
        pic_type,
        make,
        model,
        focalLength,
        crop,
        exif=data,
        tagreader_warnings=warnings,
        altitude=altitude,
    )


def decodeMakeModel(value) -> str:
    """Python 2/3 compatible decoding of make/model field."""
    if hasattr(value, "decode"):
        try:
            return value.decode("utf-8").replace("\x00", "")
        except UnicodeDecodeError:
            return value
    else:
        return value.replace("\x00", "")


def isValidManyFractions(value: str) -> bool:
    try:
        return len(decodeManyFractions(value)) > 0
    except:
        return False


def decodeManyFractions(value: str) -> List[Fraction]:
    """Try to decode a list of fractions, separated by spaces"""

    try:
        vals = [Fraction(v.strip()) for v in value.split(" ")]
        if len([True for v in vals if v.denominator == 0]) > 0:
            raise ValueError()
        return vals

    except:
        raise ValueError("Not a valid list of fractions")


def decodeLatLon(data: dict, group: str) -> Tuple[Optional[float], Optional[float], List[str]]:
    """Reads GPS info from given group to get latitude/longitude as float coordinates"""

    lat, lon = None, None
    warnings = []

    if isExifTagUsable(data, f"{group}.GPSLatitude", List[Fraction]) and isExifTagUsable(data, f"{group}.GPSLongitude", List[Fraction]):
        latRaw = decodeManyFractions(data[f"{group}.GPSLatitude"])
        if len(latRaw) == 3:
            if not isExifTagUsable(data, f"{group}.GPSLatitudeRef"):
                warnings.append("GPSLatitudeRef not found, assuming GPSLatitudeRef is North")
                latRef = 1
            else:
                latRef = -1 if data[f"{group}.GPSLatitudeRef"].startswith("S") else 1
            lat = latRef * (float(latRaw[0]) + float(latRaw[1]) / 60 + float(latRaw[2]) / 3600)

            lonRaw = decodeManyFractions(data[f"{group}.GPSLongitude"])
            if len(lonRaw) != 3:
                raise InvalidExifException("Broken GPS coordinates in picture EXIF tags")

            if not isExifTagUsable(data, f"{group}.GPSLongitudeRef"):
                warnings.append("GPSLongitudeRef not found, assuming GPSLongitudeRef is East")
                lonRef = 1
            else:
                lonRef = -1 if data[f"{group}.GPSLongitudeRef"].startswith("W") else 1
            lon = lonRef * (float(lonRaw[0]) + float(lonRaw[1]) / 60 + float(lonRaw[2]) / 3600)

    if lat is None and lon is None:
        rawLat, rawLon = None, None
        if isExifTagUsable(data, f"{group}.GPSLatitude", float) and isExifTagUsable(data, f"{group}.GPSLongitude", float):
            rawLat = float(data[f"{group}.GPSLatitude"])
            rawLon = float(data[f"{group}.GPSLongitude"])
        elif isExifTagUsable(data, f"{group}.GPSLatitude", Fraction) and isExifTagUsable(data, f"{group}.GPSLongitude", Fraction):
            rawLat = float(Fraction(data[f"{group}.GPSLatitude"]))
            rawLon = float(Fraction(data[f"{group}.GPSLongitude"]))

        if rawLat and rawLon:
            latRef = 1
            if not isExifTagUsable(data, f"{group}.GPSLatitudeRef"):
                warnings.append("GPSLatitudeRef not found, assuming GPSLatitudeRef is North")
            else:
                latRef = -1 if data[f"{group}.GPSLatitudeRef"].startswith("S") else 1

            lonRef = 1
            if not isExifTagUsable(data, f"{group}.GPSLongitudeRef"):
                warnings.append("GPSLongitudeRef not found, assuming GPSLongitudeRef is East")
            else:
                lonRef = -1 if data[f"{group}.GPSLongitudeRef"].startswith("W") else 1

            lat = latRef * rawLat
            lon = lonRef * rawLon

    return (lat, lon, warnings)


def decodeDateTimeOriginal(
    data: dict, datetimeField: str, lat: Optional[float] = None, lon: Optional[float] = None
) -> Tuple[Optional[datetime.datetime], List[str]]:
    d = None
    warnings = []

    if d is None and isExifTagUsable(data, datetimeField):
        try:
            dateRaw = data[datetimeField][:10].replace(":", "-")
            timeRaw = data[datetimeField][11:].split(":")
            hourRaw = int(timeRaw[0])
            minutesRaw = int(timeRaw[1])
            secondsRaw, microsecondsRaw, msw = decodeSecondsAndMicroSeconds(
                timeRaw[2], data["Exif.Photo.SubSecTimeOriginal"] if isExifTagUsable(data, "Exif.Photo.SubSecTimeOriginal", float) else "0"
            )
            warnings += msw

            d = datetime.datetime.combine(
                datetime.date.fromisoformat(dateRaw),
                datetime.time(
                    hourRaw,
                    minutesRaw,
                    secondsRaw,
                    microsecondsRaw,
                ),
            )

            # Timezone handling
            # Try to read from EXIF
            tz = decodeTimeOffset(data, f"Exif.Photo.OffsetTime{'Original' if 'DateTimeOriginal' in datetimeField else ''}")
            if tz is not None:
                d = d.replace(tzinfo=tz)

            # Otherwise, try to deduct from coordinates
            elif lon is not None and lat is not None:
                tz_name = tz_finder.timezone_at(lng=lon, lat=lat)
                if tz_name is not None:
                    d = pytz.timezone(tz_name).localize(d)
                # Otherwise, default to UTC + warning
                else:
                    d = d.replace(tzinfo=datetime.timezone.utc)
                    warnings.append("Precise timezone information not found, fallback to UTC")

            # Otherwise, default to UTC + warning
            else:
                d = d.replace(tzinfo=datetime.timezone.utc)
                warnings.append("Precise timezone information not found (and no GPS coordinates to help), fallback to UTC")

        except ValueError as e:
            warnings.append("Skipping original date/time (from " + datetimeField + ") as it was not recognized:\n\t" + str(e))

    return (d, warnings)


def decodeTimeOffset(data: dict, offsetTimeField: str) -> Optional[datetime.tzinfo]:
    if isExifTagUsable(data, offsetTimeField, datetime.tzinfo):
        return datetime.datetime.fromisoformat(f"2020-01-01T00:00:00{data[offsetTimeField]}").tzinfo
    return None


def decodeGPSDateTime(
    data: dict, group: str, lat: Optional[float] = None, lon: Optional[float] = None
) -> Tuple[Optional[datetime.datetime], List[str]]:
    d = None
    warnings = []

    if d is None and isExifTagUsable(data, f"{group}.GPSDateStamp"):
        try:
            dateRaw = data[f"{group}.GPSDateStamp"].replace(":", "-").replace("\x00", "").replace("/", "-")

            # Time
            if isExifTagUsable(data, f"{group}.GPSTimeStamp", List[Fraction]):
                timeRaw = decodeManyFractions(data[f"{group}.GPSTimeStamp"])
            elif isExifTagUsable(data, f"{group}.GPSTimeStamp", datetime.time):
                timeRaw = data[f"{group}.GPSTimeStamp"].split(":")
            elif isExifTagUsable(data, f"{group}.GPSDateTime", List[Fraction]):
                timeRaw = decodeManyFractions(data[f"{group}.GPSDateTime"])
            else:
                raise ValueError(f"GPSTimeStamp and GPSDateTime don't contain supported time format (in {group} group)")

            seconds, microseconds, msw = decodeSecondsAndMicroSeconds(
                str(float(timeRaw[2])),
                data["Exif.Photo.SubSecTimeOriginal"] if isExifTagUsable(data, "Exif.Photo.SubSecTimeOriginal", float) else "0",
            )

            warnings += msw

            if timeRaw:
                d = datetime.datetime.combine(
                    datetime.date.fromisoformat(dateRaw),
                    datetime.time(
                        int(float(timeRaw[0])),  # float->int to avoid DeprecationWarning
                        int(float(timeRaw[1])),
                        seconds,
                        microseconds,
                        tzinfo=datetime.timezone.utc,
                    ),
                )

                # Set timezone from coordinates
                if lon is not None and lat is not None:
                    tz_name = tz_finder.timezone_at(lng=lon, lat=lat)
                    if tz_name is not None:
                        d = d.astimezone(pytz.timezone(tz_name))

        except ValueError as e:
            warnings.append(f"Skipping GPS date/time ({group} group) as it was not recognized:\n\t{str(e)}")

    return (d, warnings)


def decodeSecondsAndMicroSeconds(secondsRaw: str, microsecondsRaw: str) -> Tuple[int, int, List[str]]:
    warnings = []

    # Read microseconds from SubSecTime field
    if microsecondsRaw.endswith(".0"):
        microsecondsRaw = microsecondsRaw.replace(".0", "")
    microseconds = int(str(microsecondsRaw)[:6].ljust(6, "0"))

    # Check if seconds is decimal, and should then be used for microseconds
    if "." in secondsRaw:
        secondsParts = secondsRaw.split(".")
        seconds = int(secondsParts[0])
        microsecondsFromSeconds = int(secondsParts[1][:6].ljust(6, "0"))

        # Check if microseconds from decimal seconds is not mismatching microseconds from SubSecTime field
        if microseconds != microsecondsFromSeconds and microseconds > 0 and microsecondsFromSeconds > 0:
            warnings.append(
                f"Microseconds read from decimal seconds value ({microsecondsFromSeconds}) is not matching value from EXIF field ({microseconds}). Max value will be kept."
            )
        microseconds = max(microseconds, microsecondsFromSeconds)
    else:
        seconds = int(secondsRaw)

    return (seconds, microseconds, warnings)


def isExifTagUsable(exif, tag, expectedType: Any = str) -> bool:
    """Is a given EXIF tag usable (not null and not an empty string)

    Args:
        exif (dict): The EXIF tags
        tag (str): The tag to check
        expectedType (class): The expected data type

    Returns:
        bool: True if not empty
    """

    try:
        if not tag in exif:
            return False
        elif expectedType == List[Fraction]:
            return isValidManyFractions(exif[tag])
        elif expectedType == Fraction:
            try:
                Fraction(exif[tag])
                return True
            except:
                return False
        elif expectedType == datetime.time:
            try:
                datetime.time.fromisoformat(exif[tag])
                return True
            except:
                return False
        elif expectedType == datetime.tzinfo:
            try:
                datetime.datetime.fromisoformat(f"2020-01-01T00:00:00{exif[tag]}")
                return True
            except:
                return False
        elif not (expectedType in [float, int] or isinstance(exif[tag], expectedType)):
            return False
        elif not (expectedType != str or len(exif[tag].strip().replace("\x00", "")) > 0):
            return False
        elif not (expectedType not in [float, int] or float(exif[tag]) is not None):
            return False
        else:
            return True
    except ValueError:
        return False
