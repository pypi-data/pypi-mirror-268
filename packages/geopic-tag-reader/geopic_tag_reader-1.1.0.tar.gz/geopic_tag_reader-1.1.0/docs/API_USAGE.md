<!-- markdownlint-disable -->

# API Overview

## Modules

- [`camera`](./camera.md#module-camera)
- [`model`](./model.md#module-model)
- [`reader`](./reader.md#module-reader)
- [`writer`](./writer.md#module-writer)

## Classes

- [`model.PictureType`](./model.md#class-picturetype)
- [`reader.CropValues`](./reader.md#class-cropvalues): Cropped equirectangular pictures metadata
- [`reader.GeoPicTags`](./reader.md#class-geopictags): Tags associated to a geolocated picture
- [`reader.InvalidExifException`](./reader.md#class-invalidexifexception): Exception for invalid EXIF information from image
- [`reader.PartialExifException`](./reader.md#class-partialexifexception): Exception for partial / missing EXIF information from image
- [`reader.PartialGeoPicTags`](./reader.md#class-partialgeopictags): Tags associated to a geolocated picture when not all tags have been found
- [`writer.Direction`](./writer.md#class-direction): Direction(value: float, ref: writer.DirectionRef = <DirectionRef.true_north: 'T'>)
- [`writer.DirectionRef`](./writer.md#class-directionref): Indicates the reference for giving the direction of the image when it is captured.
- [`writer.PictureMetadata`](./writer.md#class-picturemetadata): PictureMetadata(capture_time: Optional[datetime.datetime] = None, longitude: Optional[float] = None, latitude: Optional[float] = None, picture_type: Optional[geopic_tag_reader.model.PictureType] = None, altitude: Optional[float] = None, direction: Optional[writer.Direction] = None, additional_exif: Optional[dict] = None)
- [`writer.UnsupportedExifTagException`](./writer.md#class-unsupportedexiftagexception): Exception for invalid key in additional tags

## Functions

- [`camera.is_360`](./camera.md#function-is_360): Checks if given camera is equirectangular (360°) based on its make, model and dimensions (width, height).
- [`reader.decodeDateTimeOriginal`](./reader.md#function-decodedatetimeoriginal)
- [`reader.decodeGPSDateTime`](./reader.md#function-decodegpsdatetime)
- [`reader.decodeLatLon`](./reader.md#function-decodelatlon): Reads GPS info from given group to get latitude/longitude as float coordinates
- [`reader.decodeMakeModel`](./reader.md#function-decodemakemodel): Python 2/3 compatible decoding of make/model field.
- [`reader.decodeManyFractions`](./reader.md#function-decodemanyfractions): Try to decode a list of fractions, separated by spaces
- [`reader.decodeSecondsAndMicroSeconds`](./reader.md#function-decodesecondsandmicroseconds)
- [`reader.decodeTimeOffset`](./reader.md#function-decodetimeoffset)
- [`reader.isExifTagUsable`](./reader.md#function-isexiftagusable): Is a given EXIF tag usable (not null and not an empty string)
- [`reader.isValidManyFractions`](./reader.md#function-isvalidmanyfractions)
- [`reader.readPictureMetadata`](./reader.md#function-readpicturemetadata): Extracts metadata from picture file
- [`writer.format_offset`](./writer.md#function-format_offset): Format offset for OffsetTimeOriginal. Format is like "+02:00" for paris offset
- [`writer.localize_capture_time`](./writer.md#function-localize_capture_time): Localize a datetime in the timezone of the picture
- [`writer.writePictureMetadata`](./writer.md#function-writepicturemetadata): Override exif metadata on raw picture and return updated bytes


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
