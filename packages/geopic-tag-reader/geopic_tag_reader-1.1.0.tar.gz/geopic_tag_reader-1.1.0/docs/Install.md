# Install

GeoPicTagReader can be installed using two methods:

- From [PyPI](https://pypi.org/project/geopic-tag-reader/), the Python central package repository
- Using this [Git repository](https://gitlab.com/geovisio/geo-picture-tag-reader)

GeoPicTagReader is compatible with all python version >= 3.8. Note that, due to [Pyexiv2 dependency on a recent GLIBC version](https://github.com/LeoHsiao1/pyexiv2/issues/120), you have to make sure to run on a recent, up-to-date operating system.

## From PyPI

Just launch this command:

```bash
pip install geopic_tag_reader
```

After this you should be able to use the CLI tool with the name `geopic-tag-reader`:

```bash
geopic-tag-reader --help
```

Alternatively, you can use [pipx](https://github.com/pypa/pipx) if you want all the script dependencies to be in a custom virtual env.

You need to [install pipx](https://pypa.github.io/pipx/installation/), then:

```bash
pipx install geopic_tag_reader
```

## From Git repository

Download the repository:

```bash
git clone https://gitlab.com/geovisio/geo-picture-tag-reader.git geopic_tag_reader
cd geopic_tag_reader/
```

To avoid conflicts, it's considered a good practice to create a _[virtual environment](https://docs.python.org/3/library/venv.html)_ (or virtualenv). To do so, launch the following commands:

```bash
# Create the virtual environment in a folder named "env"
python3 -m venv env

# Launches utilities to make environment available in your Bash
source ./env/bin/activate
```

Then, install the dependencies using pip:

```bash
pip install -e .
```

If you want to be able to write exif tags, you need to also install the `write-exif` extra:

```bash
pip install -e .[write-exif]
```

This will install [libexiv2](https://exiv2.org/) if available in the target platform.


You can also install the `dev` dependencies if necessary (to have lints, format, tests, ...):

```bash
pip install -e .[dev]
```

Then, you can use the `geopic-tag-reader` command:
```bash
geopic-tag-reader --help
```
