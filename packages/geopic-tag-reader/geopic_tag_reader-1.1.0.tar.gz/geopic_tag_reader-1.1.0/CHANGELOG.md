# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2024-04-17

### Changed

- Encoding information (`charset=...`) is now stripped out of text EXIF tags.
- `GeoPicTags` objects returns `ts` as a Python `datetime` object (instead of decimal epoch).
- Improved timezone handling in reader, GPS coordinates are used to find appropriate timezone when no timezone is defined in EXIF tags. If a UTC fallback is done, a warning is thrown.

## [1.0.6] - 2024-04-02

### Changed

- Bump some dependencies, the most important one being [typer](https://typer.tiangolo.com/) since it removes the need for typer-cli.

## [1.0.5] - 2024-03-06

### Fixed

- Automatic detection of 360° pictures based on make and model also checks for image dimensions (to avoid false positive, when 360° camera can also take flat pictures).
- Slash character in GPS date stamp was not correctly interpreted.

## [1.0.4] - 2024-02-12

### Changed

- When using date/time not coming from GPS, offset time EXIF field are also read (`Exif.Photo.OffsetTimeOriginal` or `Exif.Photo.OffsetTime` depending on used date/time EXIF tag).

## [1.0.3] - 2023-12-18

### Added

- Support reading date from EXIF fields `Exif.Image.DateTime` and `Xmp.GPano.SourceImageCreateTime`.
- Auto-detect if a picture is 360° based on make and model.

### Fixed

- Avoid failures for pictures with invalid offset for maker notes (due to PyExiv2 log level).

## [1.0.2] - 2023-11-20

### Added

- A warning is thrown when microseconds values between decimal seconds and sub-second time fields are not matching.

### Changed

- Fraction values for date, time and GPS coordinates are supported.

## [1.0.1] - 2023-11-17

### Fixed

- `DateTimeOriginal` field wasn't correctly read when seconds value was decimal.

## [1.0.0] - 2023-10-18

### Added

- Add subseconds to written metadata
- Read altitude in metadata
- Write direction and altitude metadata
- Add `additional_exif` tags in `writePictureMetadata`

### Changed

- EXIF list of tags now uses the [Exiv2](https://exiv2.org/metadata.html) notation (example `Exif.Image.Artist`) in returned data. To do this, pyexiv2 dependency is always necessary, and Pillow dependency has been removed. As a consequence, `readPictureMetadata` function **now takes in input `bytes`** read from picture file instead of Pillow image. This is a breaking change.
- Use overriden metadata is available to localize overriden capture_time

## [0.4.1] - 2023-09-08

### Added

- Latitude and longitude values are checked to verify they fit into WGS84 projection bounds (-180, -90, 180, 90).

## [0.4.0] - 2023-09-01

### Added

- When a picture does not contain a mandatory exif tag (coordinates or datetime), a `PartialExifException` is thrown containing some information about what has been parsed and what is missing.

## [0.3.1] - 2023-07-31

### Added

- A way to write exif lon/lat and type tags.

## [0.3.0] - 2023-07-31

### Added

- Support of any date/time separator for EXIF tag `DateTimeOriginal`
- A way to write exif tags. To use this, you need to install this library with the extra `[write-exif]`.

## [0.2.0] - 2023-07-13

### Added

- Support of cropped equirectangular panoramas

### Changed

- Support python 3.8

## [0.1.3]

### Changed

- Bump [Typer](typer.tiangolo.com/) version, and use fork of [Typer-cli](https://gitlab.com/geovisio/infra/typer-cli)

## [0.1.2]

### Added

- Full typing support ([PEP 484](https://peps.python.org/pep-0484/) and [PEP 561](https://peps.python.org/pep-0561/))

## [0.1.1]

### Added

- Support of Mapillary tags stored in EXIF tag `ImageDescription`

## [0.1.0]

### Added

- If GPS Date or time can't be read, fallbacks to Original Date EXIF tag associated with a reader warning
- New EXIF tags are supported: `GPSDateTime`

### Changed

- `tag_reader:warning` property has been moved from EXIF, and is now available as a direct property named `tagreader_warnings` of `GeoPicTags` class
- Reader now supports `GPSLatitude` and `GPSLongitude` stored as decimal values instead of tuple
- Reader now supports reading `FocalLength` written in `NUMBER/NUMBER` format
- If EXIF tags for heading `PoseHeadingDegrees` and `GPSImgDirection` have contradicting values, we use by default `GPSImgDirection` value and issue a warning, instead of raising an error

### Fixed

- EXIF tag `SubsecTimeOriginal` was not correctly read due to a typo

## [0.0.2] - 2023-05-10

### Added

- EXIF tag `UserComment` is now read and available in raw `exif` tags
- If not set, `GPSLatitudeRef` defaults to North and `GPSLongitudeRef` defaults to East
- A new `tag_reader:warning` property lists non-blocking warnings raised while reading EXIF tags

## [0.0.1] - 2023-03-31

### Added

- EXIF tag reading methods extracted from [GeoVisio API](https://gitlab.com/geovisio/api)

[Unreleased]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/1.1.0...main
[1.1.0]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/1.0.6...1.1.0
[1.0.6]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/1.0.5...1.0.6
[1.0.5]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/1.0.4...1.0.5
[1.0.4]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/1.0.3...1.0.4
[1.0.3]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/1.0.2...1.0.3
[1.0.2]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/1.0.1...1.0.2
[1.0.1]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/1.0.0...1.0.1
[1.0.0]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/0.4.1...1.0.0
[0.4.1]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/0.4.0...0.4.1
[0.4.0]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/0.3.1...0.4.0
[0.3.1]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/0.3.0...0.3.1
[0.3.0]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/0.2.0...0.3.0
[0.2.0]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/0.1.3...0.2.0
[0.1.3]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/0.1.2...0.1.3
[0.1.2]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/0.1.1...0.1.2
[0.1.1]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/0.1.0...0.1.1
[0.1.0]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/0.0.2...0.1.0
[0.0.2]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/compare/0.0.1...0.0.2
[0.0.1]: https://gitlab.com/geovisio/geo-picture-tag-reader/-/commits/0.0.1
