<!-- markdownlint-disable -->

<a href="../geopic_tag_reader/reader.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `reader`





---

<a href="../geopic_tag_reader/reader.py#L118"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `readPictureMetadata`

```python
readPictureMetadata(picture: bytes) → GeoPicTags
```

Extracts metadata from picture file 



**Args:**
 
 - <b>`picture`</b> (bytes):  Picture file 



**Returns:**
 
 - <b>`GeoPicTags`</b>:  Extracted metadata from picture 


---

<a href="../geopic_tag_reader/reader.py#L355"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `decodeMakeModel`

```python
decodeMakeModel(value) → str
```

Python 2/3 compatible decoding of make/model field. 


---

<a href="../geopic_tag_reader/reader.py#L366"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `isValidManyFractions`

```python
isValidManyFractions(value: str) → bool
```






---

<a href="../geopic_tag_reader/reader.py#L373"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `decodeManyFractions`

```python
decodeManyFractions(value: str) → List[Fraction]
```

Try to decode a list of fractions, separated by spaces 


---

<a href="../geopic_tag_reader/reader.py#L386"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `decodeLatLon`

```python
decodeLatLon(
    data: dict,
    group: str
) → Tuple[Optional[float], Optional[float], List[str]]
```

Reads GPS info from given group to get latitude/longitude as float coordinates 


---

<a href="../geopic_tag_reader/reader.py#L441"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `decodeDateTimeOriginal`

```python
decodeDateTimeOriginal(
    data: dict,
    datetimeField: str,
    lat: Optional[float] = None,
    lon: Optional[float] = None
) → Tuple[Optional[datetime], List[str]]
```






---

<a href="../geopic_tag_reader/reader.py#L495"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `decodeTimeOffset`

```python
decodeTimeOffset(data: dict, offsetTimeField: str) → Optional[tzinfo]
```






---

<a href="../geopic_tag_reader/reader.py#L501"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `decodeGPSDateTime`

```python
decodeGPSDateTime(
    data: dict,
    group: str,
    lat: Optional[float] = None,
    lon: Optional[float] = None
) → Tuple[Optional[datetime], List[str]]
```






---

<a href="../geopic_tag_reader/reader.py#L552"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `decodeSecondsAndMicroSeconds`

```python
decodeSecondsAndMicroSeconds(
    secondsRaw: str,
    microsecondsRaw: str
) → Tuple[int, int, List[str]]
```






---

<a href="../geopic_tag_reader/reader.py#L578"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `isExifTagUsable`

```python
isExifTagUsable(exif, tag, expectedType: Any = <class 'str'>) → bool
```

Is a given EXIF tag usable (not null and not an empty string) 



**Args:**
 
 - <b>`exif`</b> (dict):  The EXIF tags 
 - <b>`tag`</b> (str):  The tag to check 
 - <b>`expectedType`</b> (class):  The expected data type 



**Returns:**
 
 - <b>`bool`</b>:  True if not empty 


---

<a href="../geopic_tag_reader/reader.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CropValues`
Cropped equirectangular pictures metadata 



**Attributes:**
 
 - <b>`fullWidth`</b> (int):  Full panorama width 
 - <b>`fullHeight`</b> (int):  Full panorama height 
 - <b>`width`</b> (int):  Cropped area width 
 - <b>`height`</b> (int):  Cropped area height 
 - <b>`left`</b> (int):  Cropped area left offset 
 - <b>`top`</b> (int):  Cropped area top offset 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    fullWidth: int,
    fullHeight: int,
    width: int,
    height: int,
    left: int,
    top: int
) → None
```









---

<a href="../geopic_tag_reader/reader.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `GeoPicTags`
Tags associated to a geolocated picture 



**Attributes:**
 
 - <b>`lat`</b> (float):  GPS Latitude (in WGS84) 
 - <b>`lon`</b> (float):  GPS Longitude (in WGS84) 
 - <b>`ts`</b> (datetime):  The capture date (date & time with timezone) 
 - <b>`heading`</b> (int):  Picture heading (in degrees, North = 0°, East = 90°, South = 180°, West = 270°) 
 - <b>`type`</b> (str):  The kind of picture (flat, equirectangular) 
 - <b>`make`</b> (str):  The camera manufacturer name 
 - <b>`model`</b> (str):  The camera model name 
 - <b>`focal_length`</b> (float):  The camera focal length (in mm) 
 - <b>`crop`</b> (CropValues):  The picture cropped area metadata (optional) 
 - <b>`exif`</b> (dict[str, str]):  Raw EXIF tags from picture (following Exiv2 naming scheme, see https://exiv2.org/metadata.html) 
 - <b>`tagreader_warnings`</b> (list[str]):  List of thrown warnings during metadata reading 
 - <b>`altitude`</b> (float):  altitude (in m) (optional) 



Implementation note: this needs to be sync with the PartialGeoPicTags structure 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    lat: float,
    lon: float,
    ts: datetime,
    heading: Optional[int],
    type: str,
    make: Optional[str],
    model: Optional[str],
    focal_length: Optional[float],
    crop: Optional[CropValues],
    exif: Dict[str, str] = <factory>,
    tagreader_warnings: List[str] = <factory>,
    altitude: Optional[float] = None
) → None
```









---

<a href="../geopic_tag_reader/reader.py#L77"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `InvalidExifException`
Exception for invalid EXIF information from image 

<a href="../geopic_tag_reader/reader.py#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(msg)
```









---

<a href="../geopic_tag_reader/reader.py#L84"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `PartialGeoPicTags`
Tags associated to a geolocated picture when not all tags have been found 

Implementation note: this needs to be sync with the GeoPicTags structure 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    lat: Optional[float] = None,
    lon: Optional[float] = None,
    ts: Optional[datetime] = None,
    heading: Optional[int] = None,
    type: Optional[str] = None,
    make: Optional[str] = None,
    model: Optional[str] = None,
    focal_length: Optional[float] = None,
    crop: Optional[CropValues] = None,
    exif: Dict[str, str] = <factory>,
    tagreader_warnings: List[str] = <factory>,
    altitude: Optional[float] = None
) → None
```









---

<a href="../geopic_tag_reader/reader.py#L105"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `PartialExifException`
Exception for partial / missing EXIF information from image 

Contains a PartialGeoPicTags with all tags that have been read and the list of missing tags 

<a href="../geopic_tag_reader/reader.py#L112"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(msg, missing_mandatory_tags: Set[str], partial_tags: PartialGeoPicTags)
```











---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
