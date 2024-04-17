<!-- markdownlint-disable -->

<a href="../geopic_tag_reader/writer.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `writer`




**Global Variables**
---------------
- **FLOAT_PRECISION**

---

<a href="../geopic_tag_reader/writer.py#L75"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `writePictureMetadata`

```python
writePictureMetadata(picture: bytes, metadata: PictureMetadata) → bytes
```

Override exif metadata on raw picture and return updated bytes 


---

<a href="../geopic_tag_reader/writer.py#L158"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `format_offset`

```python
format_offset(offset: Optional[timedelta]) → str
```

Format offset for OffsetTimeOriginal. Format is like "+02:00" for paris offset ``` format_offset(timedelta(hours=5, minutes=45))```
'+05:45'
``` format_offset(timedelta(hours=-3))``` '-03:00' 


---

<a href="../geopic_tag_reader/writer.py#L171"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `localize_capture_time`

```python
localize_capture_time(
    metadata: PictureMetadata,
    img_metadata: ImageData
) → datetime
```

Localize a datetime in the timezone of the picture If the picture does not contains GPS position, the datetime will not be modified. 


---

<a href="../geopic_tag_reader/writer.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `UnsupportedExifTagException`
Exception for invalid key in additional tags 

<a href="../geopic_tag_reader/writer.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(msg)
```









---

<a href="../geopic_tag_reader/writer.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `DirectionRef`
Indicates the reference for giving the direction of the image when it is captured. 





---

<a href="../geopic_tag_reader/writer.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Direction`
Direction(value: float, ref: writer.DirectionRef = <DirectionRef.true_north: 'T'>) 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    value: float,
    ref: DirectionRef = <DirectionRef.true_north: 'T'>
) → None
```









---

<a href="../geopic_tag_reader/writer.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `PictureMetadata`
PictureMetadata(capture_time: Optional[datetime.datetime] = None, longitude: Optional[float] = None, latitude: Optional[float] = None, picture_type: Optional[geopic_tag_reader.model.PictureType] = None, altitude: Optional[float] = None, direction: Optional[writer.Direction] = None, additional_exif: Optional[dict] = None) 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    capture_time: Optional[datetime] = None,
    longitude: Optional[float] = None,
    latitude: Optional[float] = None,
    picture_type: Optional[PictureType] = None,
    altitude: Optional[float] = None,
    direction: Optional[Direction] = None,
    additional_exif: Optional[dict] = None
) → None
```








---

<a href="../geopic_tag_reader/writer.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `has_change`

```python
has_change() → bool
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
