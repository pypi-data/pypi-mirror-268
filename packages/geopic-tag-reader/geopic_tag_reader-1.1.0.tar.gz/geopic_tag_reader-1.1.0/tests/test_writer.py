from datetime import datetime
from .conftest import FIXTURE_DIR
import os
import pytest
from geopic_tag_reader import writer, reader, model
import io
import pytz
import math
import pyexiv2  # type: ignore
from .conftest import openImg


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "1.jpg"))
def test_writePictureMetadata_capture_time(datafiles):
    capture_time = datetime(year=2023, month=6, day=1, hour=12, minute=48, second=1, microsecond=500000, tzinfo=pytz.UTC)

    img_orig = openImg(str(datafiles / "1.jpg"))
    image_file_upd = writer.writePictureMetadata(img_orig, writer.PictureMetadata(capture_time=capture_time))
    tags = reader.readPictureMetadata(image_file_upd)

    assert tags.ts == capture_time

    # we also check specific tags:
    assert tags.exif["Exif.Photo.DateTimeOriginal"] == "2023-06-01 12:48:01"
    assert tags.exif["Exif.GPSInfo.GPSDateStamp"] == "2023-06-01"
    assert tags.exif["Exif.GPSInfo.GPSTimeStamp"] == "12/1 48/1 1/1"
    assert tags.exif["Exif.Photo.SubSecTimeOriginal"] == "500000"


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "1.jpg"))
def test_writePictureMetadata_capture_time_no_timezone(datafiles):
    capture_time = datetime(year=2023, month=6, day=1, hour=12, minute=48, second=1, tzinfo=None)

    img_orig = openImg(str(datafiles / "1.jpg"))
    image_file_upd = writer.writePictureMetadata(img_orig, writer.PictureMetadata(capture_time=capture_time))
    tags = reader.readPictureMetadata(image_file_upd)

    paris = pytz.timezone("Europe/Paris")
    assert tags.ts == paris.localize(capture_time).astimezone(pytz.UTC)

    # DateTimeOriginal should be a local time, so 12:48:01 localized in Europe/Paris timezome (since it's where the picture has been taken)
    assert tags.exif["Exif.Photo.DateTimeOriginal"] == "2023-06-01 12:48:01"
    assert tags.exif["Exif.GPSInfo.GPSDateStamp"] == "2023-06-01"
    # GPSTimeStamp should always be in UTC
    assert tags.exif["Exif.GPSInfo.GPSTimeStamp"] == "10/1 48/1 1/1"
    assert tags.exif["Exif.Photo.OffsetTimeOriginal"] == "+02:00"


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "img_without_coord.jpg"))
def test_writePictureMetadata_capture_time_no_position_in_file(datafiles):
    """Datetime should be localized if possible.
    Here no position is available, the datetime is not localized
    """
    capture_time = datetime(year=2023, month=6, day=1, hour=12, minute=48, second=1, tzinfo=pytz.UTC)

    img_orig = openImg(str(datafiles / "img_without_coord.jpg"))
    image_file_upd = writer.writePictureMetadata(img_orig, writer.PictureMetadata(capture_time=capture_time))

    with pytest.raises(reader.PartialExifException) as e_info:
        reader.readPictureMetadata(image_file_upd)

    tags = e_info.value.tags
    assert tags.exif["Exif.Photo.DateTimeOriginal"] == "2023-06-01 12:48:01"
    assert tags.exif["Exif.Photo.OffsetTimeOriginal"] == "+00:00"
    assert tags.exif["Exif.GPSInfo.GPSDateStamp"] == "2023-06-01"
    assert tags.exif["Exif.GPSInfo.GPSTimeStamp"] == "12/1 48/1 1/1"


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "img_without_coord.jpg"))
def test_writePictureMetadata_capture_time_no_position_in_file_but_overriden(datafiles):
    """Datetime should be localized with overriden coord when available"""
    capture_time = datetime(year=2023, month=6, day=1, hour=12, minute=48, second=1, tzinfo=None)

    img_orig = openImg(str(datafiles / "img_without_coord.jpg"))
    image_file_upd = writer.writePictureMetadata(
        img_orig, writer.PictureMetadata(capture_time=capture_time, latitude=48.866667, longitude=2.333333)
    )
    tags = reader.readPictureMetadata(image_file_upd)

    paris = pytz.timezone("Europe/Paris")
    assert tags.ts == paris.localize(capture_time).astimezone(pytz.UTC)

    # DateTimeOriginal should be a local time, so 12:48:01 localized in Europe/Paris timezome (since it's where the picture has been taken)
    assert tags.exif["Exif.Photo.DateTimeOriginal"] == "2023-06-01 12:48:01"
    assert tags.exif["Exif.Photo.OffsetTimeOriginal"] == "+02:00"
    assert tags.exif["Exif.GPSInfo.GPSDateStamp"] == "2023-06-01"
    # GPSTimeStamp should always be in UTC
    assert tags.exif["Exif.GPSInfo.GPSTimeStamp"] == "10/1 48/1 1/1"


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "1.jpg"))
def test_writePictureMetadata_longitude(datafiles):
    longitude = 2.4243

    img_orig = openImg(str(datafiles / "1.jpg"))
    image_file_upd = writer.writePictureMetadata(img_orig, writer.PictureMetadata(longitude=longitude))
    tags = reader.readPictureMetadata(image_file_upd)

    assert math.isclose(tags.lon, longitude)
    assert tags.exif["Exif.GPSInfo.GPSLongitude"] == "2/1 25/1 687/25"
    assert tags.exif["Exif.GPSInfo.GPSLongitudeRef"] == "E"


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "1.jpg"))
def test_writePictureMetadata_lat(datafiles):
    latitude = -38.889469

    img_orig = openImg(str(datafiles / "1.jpg"))
    image_file_upd = writer.writePictureMetadata(img_orig, writer.PictureMetadata(latitude=latitude))
    tags = reader.readPictureMetadata(image_file_upd)

    assert math.isclose(tags.lat, latitude)
    assert tags.exif["Exif.GPSInfo.GPSLatitude"] == "38/1 53/1 55221/2500"
    assert tags.exif["Exif.GPSInfo.GPSLatitudeRef"] == "S"


def _get_pyexiv_data(b: io.BytesIO) -> pyexiv2.ImageData:
    b.seek(0)
    return pyexiv2.ImageData(b.read())


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "1.jpg"))
def test_writePictureMetadata_picture_type_flat(datafiles):
    pic_type = model.PictureType.flat

    img_orig = openImg(str(datafiles / "1.jpg"))
    image_file_upd = writer.writePictureMetadata(
        img_orig,
        writer.PictureMetadata(
            picture_type=pic_type,
            # Change model to avoid auto-detection as 360° based on model
            additional_exif={"Exif.Image.Model": "Customaxi"},
        ),
    )

    file_b = io.BytesIO(image_file_upd)
    tags = reader.readPictureMetadata(image_file_upd)

    assert tags.type == "flat"
    # also check raw xmp tags
    xmp = _get_pyexiv_data(file_b).read_xmp()
    assert "Xmp.GPano.ProjectionType" not in xmp
    assert "Xmp.GPano.UsePanoramaViewer" not in xmp


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "1.jpg"))
def test_writePictureMetadata_picture_type_equi(datafiles):
    pic_type = model.PictureType.equirectangular

    img_orig = openImg(str(datafiles / "1.jpg"))
    image_file_upd = writer.writePictureMetadata(img_orig, writer.PictureMetadata(picture_type=pic_type))
    tags = reader.readPictureMetadata(image_file_upd)
    file_b = io.BytesIO(image_file_upd)

    assert tags.type == "equirectangular"
    # also check raw xmp tags
    xmp = _get_pyexiv_data(file_b).read_xmp()
    assert xmp["Xmp.GPano.ProjectionType"] == "equirectangular"
    assert xmp["Xmp.GPano.UsePanoramaViewer"] == "True"


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "flat.jpg"))
def test_writePictureMetadata_direction(datafiles):
    img_orig = openImg(str(datafiles / "flat.jpg"))
    image_file_upd = writer.writePictureMetadata(img_orig, writer.PictureMetadata(direction=writer.Direction(124)))

    file_b = io.BytesIO(image_file_upd)
    tags = reader.readPictureMetadata(image_file_upd)

    assert tags.heading == 124

    img_data = _get_pyexiv_data(file_b)
    xmp = img_data.read_xmp()
    assert xmp["Xmp.GPano.PoseHeadingDegrees"] == "124000/1000"
    exif = img_data.read_exif()
    assert exif["Exif.GPSInfo.GPSImgDirection"] == "124000/1000"
    assert exif["Exif.GPSInfo.GPSImgDirectionRef"] == "T"  # marked as true_north by default


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "flat.jpg"))
def test_writePictureMetadata_direction_north(datafiles):
    img_orig = openImg(str(datafiles / "flat.jpg"))
    image_file_upd = writer.writePictureMetadata(
        img_orig, writer.PictureMetadata(direction=writer.Direction(-14, writer.DirectionRef.magnetic_north))
    )

    file_b = io.BytesIO(image_file_upd)
    tags = reader.readPictureMetadata(image_file_upd)

    assert tags.heading == 346

    img_data = _get_pyexiv_data(file_b)
    xmp = img_data.read_xmp()
    assert xmp["Xmp.GPano.PoseHeadingDegrees"] == "346000/1000"
    exif = img_data.read_exif()
    assert exif["Exif.GPSInfo.GPSImgDirection"] == "346000/1000"
    assert exif["Exif.GPSInfo.GPSImgDirectionRef"] == "M"  # marked as magnetic_north


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "flat.jpg"))
def test_writePictureMetadata_altitude(datafiles):
    img_orig = openImg(str(datafiles / "flat.jpg"))
    image_file_upd = writer.writePictureMetadata(img_orig, writer.PictureMetadata(altitude=145))

    file_b = io.BytesIO(image_file_upd)
    tags = reader.readPictureMetadata(image_file_upd)

    assert tags.altitude == 145

    img_data = _get_pyexiv_data(file_b)
    exif = img_data.read_exif()
    assert exif["Exif.GPSInfo.GPSAltitude"] == "145000/1000"
    assert exif["Exif.GPSInfo.GPSAltitudeRef"] == "0"


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "flat.jpg"))
def test_writePictureMetadata_altitude_below_sea_level(datafiles):
    img_orig = openImg(str(datafiles / "flat.jpg"))
    image_file_upd = writer.writePictureMetadata(img_orig, writer.PictureMetadata(altitude=-145))

    file_b = io.BytesIO(image_file_upd)
    tags = reader.readPictureMetadata(image_file_upd)

    assert tags.altitude == -145

    img_data = _get_pyexiv_data(file_b)
    exif = img_data.read_exif()
    assert exif["Exif.GPSInfo.GPSAltitude"] == "145000/1000"
    assert exif["Exif.GPSInfo.GPSAltitudeRef"] == "1"  # 1 is below sea.. level


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "flat.jpg"))
def test_writePictureMetadata_additional_exif(datafiles):
    additional_tags = {"Exif.Image.Artist": "R. Doisneau"}
    img_orig = openImg(str(datafiles / "flat.jpg"))
    image_file_upd = writer.writePictureMetadata(img_orig, writer.PictureMetadata(additional_exif=additional_tags))

    file_b = io.BytesIO(image_file_upd)
    img_data = _get_pyexiv_data(file_b)
    exif = img_data.read_exif()
    assert exif["Exif.Image.Artist"] == "R. Doisneau"


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "a1.jpg"))
def test_writePictureMetadata_additional_xmp(datafiles):
    # check that existing XMP tags are not deleted by the update
    additional_tags = {"Xmp.GPano.StitchingSoftware": "GoPro Max 2"}
    img_orig = openImg(str(datafiles / "a1.jpg"))
    image_file_upd = writer.writePictureMetadata(img_orig, writer.PictureMetadata(additional_exif=additional_tags))

    file_b = io.BytesIO(image_file_upd)
    img_data = _get_pyexiv_data(file_b)
    xmp = img_data.read_xmp()

    assert xmp["Xmp.GPano.ProjectionType"] == "equirectangular"
    assert xmp["Xmp.GPano.CroppedAreaImageWidthPixels"] == "5760"
    assert xmp["Xmp.GPano.FullPanoHeightPixels"] == "2880"
    assert xmp["Xmp.GPano.StitchingSoftware"] == "GoPro Max 2"


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "flat.jpg"))
def test_writePictureMetadata_bad_key_in_additional_exif(datafiles):
    additional_tags = {"Foo.Bar": "something"}
    with pytest.raises(writer.UnsupportedExifTagException) as e_info:
        img_orig = openImg(str(datafiles / "flat.jpg"))
        writer.writePictureMetadata(img_orig, writer.PictureMetadata(additional_exif=additional_tags))

    e = e_info.value
    assert str(e).startswith("Unsupported key in additional tags")
