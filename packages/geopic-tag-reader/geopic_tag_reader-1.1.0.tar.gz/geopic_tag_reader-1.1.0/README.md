# ![GeoVisio](https://gitlab.com/geovisio/api/-/raw/develop/images/logo_full.png)

__GeoVisio__ is a complete solution for storing and __serving your own 📍📷 geolocated pictures__ (like [StreetView](https://www.google.com/streetview/) / [Mapillary](https://mapillary.com/)).

➡️ __Give it a try__ at [panoramax.ign.fr](https://panoramax.ign.fr/) or [geovisio.fr](https://geovisio.fr/viewer) !

## 📦 Components

GeoVisio is __modular__ and made of several components, each of them standardized and ♻️ replaceable.

![GeoVisio architecture](https://gitlab.com/geovisio/api/-/raw/develop/images/big_picture.png)

All of them are 📖 __open-source__ and available online:

|                               🌐 Server                                 |                      💻 Client                       |
|:-----------------------------------------------------------------------:|:----------------------------------------------------:|
|                 [API](https://gitlab.com/geovisio/api)                  |    [Website](https://gitlab.com/geovisio/website)    |
|            [Blur API](https://gitlab.com/geovisio/blurring)             | [Web viewer](https://gitlab.com/geovisio/web-viewer) |
| [GeoPic Tag Reader](https://gitlab.com/geovisio/geo-picture-tag-reader) |   [Command line](https://gitlab.com/geovisio/cli)    |


# 📷 GeoPic Tag Reader

This repository only contains the Python library to __read and write standardized metadata__ from geolocated pictures EXIF metadata.

## Features

This tool allows you to:

- 🔍 Analyse various EXIF variables to extract standardized metadata for geolocated pictures applications (coordinates, date, orientation, altitude...)
- ✏️ Edit a picture to change its EXIF variables through a simpler command
- 💻 Either as Python code or as a command-line utility


## Install

The library can be installed easily, for a quick glance:

```bash
pip install geopic_tag_reader
geopic-tag-reader --help
```

To know more about install and other options, see [install documentation](./docs/Install.md).

If at some point you're lost or need help, you can contact us through [issues](https://gitlab.com/geovisio/geo-picture-tag-reader/-/issues) or by [email](mailto:panieravide@riseup.net).


## Usage

This library can be used both from command-line or as Python module.

### As command-line

To see all available commands:

```bash
geopic-tag-reader --help
```

To read metadata from a single picture:

```bash
geopic-tag-reader read --image /path/to/my_image.jpg
```

To edit metadata of a single picture, for example change its capture date:

```bash
geopic-tag-reader write \
	--input /path/to/original_image.jpg \
	--capture-time "2023-01-01T12:56:38Z" \
	--output /path/to/edited_image.jpg
```

[Full documentation is also available here](./docs/CLI_USAGE.md).

### As Python library

In your own script, for reading and writing a picture metadata, you can use:

```python
from geopic_tag_reader import reader, writer, model

# Open image as binary file
img = open("my_picture.jpg", "rb")
imgBytes = img.read()
img.close()

# Read EXIF metadata
metadata = reader.readPictureMetadata(imgBytes)
print(metadata)

# Edit picture EXIF metadata
editedMetadata = writer.PictureMetadata(
	picture_type = model.PictureType.equirectangular,
	direction = writer.Direction(125)
)
editedImgBytes = writer.writePictureMetadata(imgBytes, editedMetadata)

# Save edited file
editedImg = open("my_new_picture.jpg", "wb")
editedImg.write(editedImgBytes)
editedImg.close()
```

[Full documentation is also available here](./docs/API_USAGE.md).


## Contributing

Pull requests are welcome. For major changes, please open an [issue](https://gitlab.com/geovisio/geo-picture-tag-reader/-/issues) first to discuss what you would like to change.

More information about developing is available in [documentation](./docs/Develop.md).


## 🤗 Special thanks

![Sponsors](https://gitlab.com/geovisio/api/-/raw/develop/images/sponsors.png)

GeoVisio was made possible thanks to a group of ✨ __amazing__ people ✨ :

- __[GéoVélo](https://geovelo.fr/)__ team, for 💶 funding initial development and for 🔍 testing/improving software
- __[Carto Cité](https://cartocite.fr/)__ team (in particular Antoine Riche), for 💶 funding improvements on viewer (map browser, flat pictures support)
- __[La Fabrique des Géocommuns (IGN)](https://www.ign.fr/institut/la-fabrique-des-geocommuns-incubateur-de-communs-lign)__ for offering long-term support and funding the [Panoramax](https://panoramax.fr/) initiative and core team (Camille Salou, Mathilde Ferrey, Christian Quest, Antoine Desbordes, Jean Andreani, Adrien Pavie)
- Many _many_ __wonderful people__ who worked on various parts of GeoVisio or core dependencies we use : 🧙 Stéphane Péneau, 🎚 Albin Calais & Cyrille Giquello, 📷 [Damien Sorel](https://www.strangeplanet.fr/), Pascal Rhod, Nick Whitelegg...
- __[Adrien Pavie](https://pavie.info/)__, for ⚙️ initial development of GeoVisio
- And you all ✨ __GeoVisio users__ for making this project useful !


## ⚖️ License

Copyright (c) GeoVisio team 2022-2023, [released under MIT license](https://gitlab.com/geovisio/geo-picture-tag-reader/-/blob/main/LICENSE).
