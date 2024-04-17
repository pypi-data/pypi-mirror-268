<!-- markdownlint-disable -->

<a href="../geopic_tag_reader/camera.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `camera`




**Global Variables**
---------------
- **EQUIRECTANGULAR_MODELS**

---

<a href="../geopic_tag_reader/camera.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `is_360`

```python
is_360(
    make: Optional[str] = None,
    model: Optional[str] = None,
    width: Optional[str] = None,
    height: Optional[str] = None
) → bool
```

Checks if given camera is equirectangular (360°) based on its make, model and dimensions (width, height). 

``` is_360()```
False
``` is_360("GoPro")``` False ``` is_360("GoPro", "Max 360")```
True
``` is_360("GoPro", "Max 360", "2048", "1024")``` True ``` is_360("GoPro", "Max 360", "1024", "768")```
False





---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
