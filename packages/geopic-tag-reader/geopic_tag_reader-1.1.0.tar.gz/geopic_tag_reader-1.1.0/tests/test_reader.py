import os
import pytest
from geopic_tag_reader import reader
from .conftest import FIXTURE_DIR, openImg


def assertGeoPicTagsEquals(gpt, expectedDict):
    assert gpt.lat == expectedDict.get("lat")
    assert gpt.lon == expectedDict.get("lon")
    assert gpt.heading == expectedDict.get("heading")
    assert gpt.type == expectedDict.get("type")
    assert gpt.make == expectedDict.get("make")
    assert gpt.model == expectedDict.get("model")
    assert gpt.focal_length == expectedDict.get("focal_length")
    assert gpt.altitude == expectedDict.get("altitude")
    assert gpt.tagreader_warnings == expectedDict.get("tagreader_warnings", [])
    assert len(gpt.exif) > 0

    if expectedDict.get("ts") is not None:
        assert gpt.ts is not None
        assert gpt.ts.isoformat() == expectedDict["ts"]
    else:
        assert gpt.ts is None

    if gpt.crop:
        assert expectedDict.get("crop") is not None
        assert gpt.crop.fullWidth == expectedDict["crop"].get("fullWidth")
        assert gpt.crop.fullHeight == expectedDict["crop"].get("fullHeight")
        assert gpt.crop.width == expectedDict["crop"].get("width")
        assert gpt.crop.height == expectedDict["crop"].get("height")
        assert gpt.crop.left == expectedDict["crop"].get("left")
        assert gpt.crop.top == expectedDict["crop"].get("top")
    else:
        assert expectedDict.get("crop") is None


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "1.jpg"))
def test_readPictureMetadata(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/1.jpg"))
    assertGeoPicTagsEquals(
        result,
        {
            "lat": 49.00688961988304,
            "lon": 1.9191854417991367,
            "ts": "2021-07-29T11:16:54+02:00",
            "heading": 349,
            "type": "equirectangular",
            "make": "GoPro",
            "model": "Max",
            "focal_length": 3,
            "altitude": 93,
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "a1.jpg"))
def test_readPictureMetadata_negCoords(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/a1.jpg"))
    assertGeoPicTagsEquals(
        result,
        {
            "lat": 48.33756428166505,
            "lon": -1.9331088333333333,
            "ts": "2022-05-13T16:53:00+02:00",
            "heading": 32,
            "type": "equirectangular",
            "make": "GoPro",
            "model": "Max",
            "focal_length": 3,
            "altitude": 79,
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "b1.jpg"))
def test_readPictureMetadata_flat(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/b1.jpg"))
    assertGeoPicTagsEquals(
        result,
        {
            "lat": 48.139852239480945,
            "lon": -1.9499731060073981,
            "ts": "2015-04-25T15:37:48+02:00",
            "heading": 155,
            "type": "flat",
            "make": "OLYMPUS IMAGING CORP.",
            "model": "SP-720UZ",
            "focal_length": 4.66,
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "c1.jpg"))
def test_readPictureMetadata_flat2(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/c1.jpg"))
    assertGeoPicTagsEquals(
        result,
        {
            "lat": 48.85779642035038,
            "lon": 2.3392783047650747,
            "ts": "2015-05-04T13:08:52+02:00",
            "heading": 302,
            "type": "flat",
            "make": "Canon",
            "model": "EOS 6D0",
            "focal_length": 35.0,
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "d1.jpg"))
def test_readPictureMetadata_xmpHeading(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/d1.jpg"))
    assertGeoPicTagsEquals(
        result,
        {
            "lat": 50.87070833333333,
            "lon": -1.5260916666666666,
            "ts": "2020-09-13T15:40:19.767000+01:00",
            "heading": 67,
            "type": "equirectangular",
            "make": "Google",
            "model": "Pixel 3",
            "focal_length": None,
            "altitude": 68,
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "e1.jpg"))
def test_readPictureMetadata_noHeading(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/e1.jpg"))
    assertGeoPicTagsEquals(
        result,
        {
            "lat": 48.15506638888889,
            "lon": -1.6844680555555556,
            "ts": "2022-10-19T09:56:34+02:00",
            "heading": None,
            "type": "flat",
            "make": "SONY",
            "model": "FDR-X1000V",
            "focal_length": 2.8,
            "altitude": 34,
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "img_Ricoh_Theta.jpg"))
def test_readPictureMetadata_ricoh_theta(datafiles):
    for f in datafiles.iterdir():
        result = reader.readPictureMetadata(openImg(str(f)))
        assertGeoPicTagsEquals(
            result,
            {
                "focal_length": 0.75,
                "heading": 270,
                "lat": 48.83930905577957,
                "lon": 2.3205357914890987,
                "make": "RICOH",
                "model": "THETA m15",
                "ts": "2016-03-25T14:12:13+01:00",
                "type": "equirectangular",
            },
        )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "img_V4MPack.jpg"))
def test_readPictureMetadata_v4mpack(datafiles):
    for f in datafiles.iterdir():
        result = reader.readPictureMetadata(openImg(str(f)))
        assertGeoPicTagsEquals(
            result,
            {
                "focal_length": None,
                "heading": 64,
                "lat": 47.08506017299737,
                "lon": -1.2761512389983616,
                "make": "STFMANI",
                "model": "V4MPOD 1",
                "ts": "2019-04-16T14:20:13+02:00",
                "type": "equirectangular",
                "altitude": 34,
            },
        )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "IMG_20210720_161352.jpg"))
def test_readPictureMetadata_a5000(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/IMG_20210720_161352.jpg"))
    assertGeoPicTagsEquals(
        result,
        {
            "focal_length": 4.103,
            "heading": 355,
            "lat": 48.96280504578332,
            "lon": 2.51197323068765,
            "make": "OnePlus",
            "model": "ONEPLUS A5000",
            "ts": "2021-07-20T16:13:52.199995+02:00",
            "type": "flat",
            "altitude": 0,
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "IMG_20210720_144918.jpg"))
def test_readPictureMetadata_a5000_2(datafiles):
    with pytest.raises(reader.PartialExifException) as e_info:
        result = reader.readPictureMetadata(openImg(str(datafiles) + "/IMG_20210720_144918.jpg"))


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "img_V4MPack.jpg"))
def test_readPictureMetadata_comment(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/img_V4MPack.jpg"))
    assert result.exif.get("Exif.Photo.UserComment") == "DCIM\\627MEDIA"


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "int_long_tag.jpg"))
def test_readPictureMetadata_int_long_tag(datafiles):
    """
    int_long_tag.jpg has an invalid longituderef tag, it's '52227'
    But since the  longitude ref is optional (and default to E based on https://www.exiftool.org/geotag.html) we get a valid position
    """
    r = reader.readPictureMetadata(openImg(str(datafiles) + "/int_long_tag.jpg"))
    assertGeoPicTagsEquals(
        r,
        {
            "focal_length": None,
            "heading": 255,
            "lat": 44.09732280555556,
            "lon": 4.700622,
            "make": None,
            "model": None,
            "ts": "2023-01-12T09:17:00+01:00",
            "type": "flat",
            "tagreader_warnings": ["GPSLongitudeRef not found, assuming GPSLongitudeRef is East"],
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "img_invalid_gps_date.jpg"))
def test_readPictureMetadata_invalidGpsDate(datafiles):
    """
    Handles fallback to OriginalDate EXIF tag if GPS time is invalid
    """
    r = reader.readPictureMetadata(openImg(str(datafiles) + "/img_invalid_gps_date.jpg"))
    assertGeoPicTagsEquals(
        r,
        {
            "focal_length": 4.2,
            "heading": 202,
            "lat": 48.88026828330809,
            "lon": 2.358506155368721,
            "make": "samsung",
            "model": None,
            "ts": "2021-09-08T11:43:57.075400+02:00",
            "type": "flat",
            "altitude": 73,
            "tagreader_warnings": [
                "Skipping GPS date/time (Exif.GPSInfo group) as it was not recognized:\n\tInvalid isoformat string: '2021-09-08H'"
            ],
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "img_gps_datestamp.jpg"))
def test_readPictureMetadata_gpsDateStamp(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/img_gps_datestamp.jpg"))
    assertGeoPicTagsEquals(
        result,
        {
            "focal_length": 4.2,
            "heading": 138,
            "lat": 48.80334166666666,
            "lon": 2.4833194444444446,
            "make": "Apple",
            "model": "iPhone 12 Pro",
            "ts": "2023-04-29T18:30:51.565000+02:00",
            "type": "flat",
            "altitude": 36,
            "tagreader_warnings": [
                "Microseconds read from decimal seconds value (3000) is not matching value from EXIF field (565000). Max value will be kept."
            ],
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "img_gps_date_string.jpg"))
def test_readPictureMetadata_gpsDateString(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/img_gps_date_string.jpg"))
    assertGeoPicTagsEquals(
        result,
        {
            "focal_length": 3.99,
            "heading": 182,
            "lat": 45.624741666666665,
            "lon": -1.0015555555555555,
            "make": "Apple",
            "model": "iPhone 8 Plus",
            "ts": "2019-07-28T13:25:42.529000+02:00",
            "type": "flat",
            "altitude": 19,
            "tagreader_warnings": [
                "Microseconds read from decimal seconds value (529000) is not matching value from EXIF field (506000). Max value will be kept."
            ],
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "img_categorisee.jpg"))
def test_readPictureMetadata_categories(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/img_categorisee.jpg"))
    assert "Xmp.mediapro.CatalogSets" in result.exif
    assert "Xmp.MicrosoftPhoto.LastKeywordXMP" in result.exif
    assert "Xmp.acdsee.categories" in result.exif


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "cropped.jpg"))
def test_readPictureMetadata_cropped(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/cropped.jpg"))
    assertGeoPicTagsEquals(
        result,
        {
            "heading": 349,
            "lat": 49.00688961988304,
            "lon": 1.919185441804927,
            "make": "GoPro",
            "model": "Max",
            "ts": "2021-07-29T11:16:54+02:00",
            "type": "equirectangular",
            "altitude": 93,
            "crop": {"fullWidth": 4032, "fullHeight": 2016, "width": 2150, "height": 1412, "top": 134, "left": 538},
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "img_datetimeoriginal.jpg"))
def test_readPictureMetadata_datetimeoriginal(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/img_datetimeoriginal.jpg"))
    assertGeoPicTagsEquals(
        result,
        {
            "heading": 228,
            "lat": 47.05369676823944,
            "lon": -1.382302762883527,
            "make": "Motorola",
            "model": "XT1052",
            "ts": "2020-08-31T09:36:28+02:00",
            "type": "flat",
            "altitude": 72,
            "tagreader_warnings": [
                "Skipping GPS date/time (Exif.GPSInfo group) as it was not recognized:\n\tGPSTimeStamp and GPSDateTime don't contain supported time format (in Exif.GPSInfo group)"
            ],
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "datetime_ms_float.jpg"))
def test_readPictureMetadata_datetimeoriginal_decimal_milliseconds(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/datetime_ms_float.jpg"))
    assertGeoPicTagsEquals(
        result,
        {
            "heading": 62,
            "lat": 14.527860666666667,
            "lon": 121.15072633333334,
            "make": "BlackVue",
            "model": "DR900S-1CH",
            "ts": "2023-11-12T00:25:19.023000+08:00",
            "type": "flat",
            "altitude": 29,
            "tagreader_warnings": [],
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "img_without_exif_tags.jpg"))
def test_readPictureWithoutExifTags(datafiles):
    """Reading tags from a picture that does not contains any should result of an exception with information about the missing tags"""
    with pytest.raises(reader.PartialExifException) as e_info:
        reader.readPictureMetadata(openImg(str(datafiles) + "/img_without_exif_tags.jpg"))

    e = e_info.value
    assert e.missing_mandatory_tags == {"lon", "lat", "datetime"}
    assert str(e) == "No GPS coordinates or broken coordinates in picture EXIF tags and No valid date in picture EXIF tags"
    assert e.tags == reader.PartialGeoPicTags(type="flat")


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "img_without_coord.jpg"))
def test_readPictureWithoutCoord(datafiles):
    """Reading tags from a picture that does not contains a coordinate should result of an exception"""
    with pytest.raises(reader.PartialExifException) as e_info:
        reader.readPictureMetadata(openImg(str(datafiles) + "/img_without_coord.jpg"))

    e = e_info.value
    assert e.missing_mandatory_tags == {"lat", "lon"}
    assert str(e) == "No GPS coordinates or broken coordinates in picture EXIF tags"
    # all the information possible should have been read
    assertGeoPicTagsEquals(
        e.tags,
        {
            "focal_length": 4.2,
            "heading": 138,
            "lat": None,  # but lat/lon should be None
            "lon": None,
            "make": "Apple",
            "model": "iPhone 12 Pro",
            "ts": "2023-04-29T16:30:51.565000+00:00",
            "type": "flat",
            "altitude": 36,
            "tagreader_warnings": [
                "Microseconds read from decimal seconds value (3000) is not matching value from EXIF field (565000). Max value will be kept."
            ],
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "img_without_dt.jpg"))
def test_readPictureWithoutDatetime(datafiles):
    """Reading tags from a picture that does not contains a datetime should result of an exception"""
    with pytest.raises(reader.PartialExifException) as e_info:
        reader.readPictureMetadata(openImg(str(datafiles) + "/img_without_dt.jpg"))

    e = e_info.value
    assert e.missing_mandatory_tags == {"datetime"}
    assert str(e) == "No valid date in picture EXIF tags"

    # all the information possible should have been read
    assertGeoPicTagsEquals(
        e.tags,
        {
            "focal_length": 4.2,
            "heading": 138,
            "lat": 48.80334166666666,
            "lon": 2.4833194444444446,
            "make": "Apple",
            "model": "iPhone 12 Pro",
            "ts": None,  # No datetime should have been parsed
            "type": "flat",
            "altitude": 36,
            "tagreader_warnings": [
                "Skipping GPS date/time (Xmp.exif group) as it was not recognized:\n\tGPSTimeStamp and GPSDateTime don't contain supported time format (in Xmp.exif group)"
            ],
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "out_of_bounds_lat.jpg"))
def test_readPictureMetadata_invalidLat(datafiles):
    with pytest.raises(reader.InvalidExifException) as e_info:
        reader.readPictureMetadata(openImg(str(datafiles) + "/out_of_bounds_lat.jpg"))

    e = e_info.value
    assert str(e) == "Read latitude is out of WGS84 bounds (should be in [-90, 90])"


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "out_of_bounds_lon.jpg"))
def test_readPictureMetadata_invalidLon(datafiles):
    with pytest.raises(reader.InvalidExifException) as e_info:
        reader.readPictureMetadata(openImg(str(datafiles) + "/out_of_bounds_lon.jpg"))

    e = e_info.value
    assert str(e) == "Read longitude is out of WGS84 bounds (should be in [-180, 180])"


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "pic_with_float_lat.jpg"))
def test_readPictureWithLatitudeAsFloat(datafiles):
    """Reading a pic with the latitude as float should work as before"""
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/pic_with_float_lat.jpg"))

    assertGeoPicTagsEquals(
        result,
        {
            "heading": 6,
            "lat": 48.553668,
            "lon": 7.683081,
            "make": None,
            "model": "PULSAR",
            "ts": "2021-11-16T16:18:16.890000+01:00",
            "type": "equirectangular",
            "altitude": None,
            "tagreader_warnings": [],
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "gps_date_time_stamp.jpg"))
def test_readPictureMetadata_gps_date_time_stamp(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/gps_date_time_stamp.jpg"))

    assertGeoPicTagsEquals(
        result,
        {
            "heading": 6,
            "lat": 48.553668,
            "lon": 7.683081,
            "make": None,
            "model": "PULSAR",
            "ts": "2021-11-16T16:18:16.890000+01:00",
            "type": "equirectangular",
            "altitude": None,
            "tagreader_warnings": [],
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "insta360_date.jpg"))
def test_readPictureMetadata_insta360(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/insta360_date.jpg"))

    assertGeoPicTagsEquals(
        result,
        {
            "heading": None,
            "lat": 43.29976944444444,
            "lon": 3.482755555555556,
            "make": "Insta360",
            "model": "One X2.PHOTO_NORMAL",
            "ts": "2023-11-22T14:17:49+01:00",
            "type": "equirectangular",
            "altitude": 84,
            "tagreader_warnings": [],
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "ricoh_theta_no_projection.jpg"))
def test_readPictureMetadata_ricoh_noproj(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/ricoh_theta_no_projection.jpg"))

    assertGeoPicTagsEquals(
        result,
        {
            "heading": None,
            "lat": 48.23105138608521,
            "lon": -1.5464416503906249,
            "make": "Ricoh",
            "model": "Theta S",
            "ts": "2023-01-01T13:15:42+01:00",
            "type": "equirectangular",
            "altitude": None,
            "tagreader_warnings": [],
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "gopromax_flat.jpg"))
def test_readPictureMetadata_gopromax_flat(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/gopromax_flat.jpg"))

    assertGeoPicTagsEquals(
        result,
        {
            "lat": 47.22555109997222,
            "lon": -1.5631604999722222,
            "ts": "2024-02-17T13:46:32+01:00",
            "heading": None,
            "type": "flat",
            "make": "GoPro",
            "model": "Max",
            "focal_length": 3,
            "altitude": 78,
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "broken_makernotes.jpg"))
def test_readPictureMetadata_broken_makernotes(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/broken_makernotes.jpg"))

    assertGeoPicTagsEquals(
        result,
        {
            "heading": 33,
            "lat": 48.24849805555556,
            "lon": -1.7841980555555554,
            "make": "SONY",
            "model": "FDR-X1000V",
            "ts": "2020-09-03T08:50:20+02:00",
            "type": "flat",
            "altitude": 99,
            "focal_length": 2.8,
            "tagreader_warnings": [],
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "datetime_offset.jpg"))
def test_readPictureMetadata_datetime_offset(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/datetime_offset.jpg"))

    assertGeoPicTagsEquals(
        result,
        {
            "lat": 48.33756428166505,
            "lon": -1.9331088333333333,
            "ts": "2022-05-13T16:54:11+02:00",
            "heading": 32,
            "type": "equirectangular",
            "make": "GoPro",
            "model": "Max",
            "focal_length": 3,
            "altitude": 79,
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "gps_date_slash.jpg"))
def test_readPictureMetadata_gps_date_slash(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/gps_date_slash.jpg"))

    assertGeoPicTagsEquals(
        result,
        {
            "lat": 43.42541569992266,
            "lon": 1.3766216000638112,
            "ts": "2023-06-13T09:15:00+02:00",
            "heading": None,
            "type": "flat",
            "make": None,
            "model": None,
            "focal_length": None,
            "altitude": None,
            "tagreader_warnings": [
                "GPSLatitudeRef not found, assuming GPSLatitudeRef is North",
                "GPSLongitudeRef not found, assuming GPSLongitudeRef is East",
            ],
        },
    )


@pytest.mark.datafiles(os.path.join(FIXTURE_DIR, "charset.jpg"))
def test_readPictureMetadata_charset(datafiles):
    result = reader.readPictureMetadata(openImg(str(datafiles) + "/charset.jpg"))
    assert result.exif["Exif.Photo.UserComment"] == "CD31 31_D0003_51_600"
