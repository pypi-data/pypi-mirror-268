import typer
from pathlib import Path
from geopic_tag_reader import reader
from geopic_tag_reader.model import PictureType
from typing import Optional
import pyexiv2  # type: ignore

app = typer.Typer(help="GeoPicTagReader")


@app.command()
def read(
    image: Path = typer.Option(..., help="Path to your JPEG image file"),
    ignore_exiv2_errors: bool = typer.Option(False, "--ignore-exiv2-errors", help="Do not stop execution even if Exiv2 throws errors"),
):
    """Reads EXIF metadata from a picture file, and prints results"""

    with open(image, "rb") as img:
        pyexiv2.set_log_level(4 if ignore_exiv2_errors else 2)

        metadata = reader.readPictureMetadata(img.read())

        print("Latitude:", metadata.lat)
        print("Longitude:", metadata.lon)
        print("Timestamp:", metadata.ts.isoformat())
        print("Heading:", metadata.heading)
        print("Type:", metadata.type)
        print("Make:", metadata.make)
        print("Model:", metadata.model)
        print("Focal length:", metadata.focal_length)
        print("Crop parameters:", metadata.crop)

        if len(metadata.tagreader_warnings) > 0:
            print("Warnings raised by reader:")
            for w in metadata.tagreader_warnings:
                print(" - " + w)


@app.command()
def write(
    input: Path = typer.Option(help="Path to your JPEG image file"),
    output: Optional[Path] = typer.Option(
        default=None, help="Output path where to write the updated image file. If not present, the input file will be overriten."
    ),
    capture_time: Optional[str] = typer.Option(
        default=None,
        help="override capture time of the image, formated in isoformat, like '2023-06-01T12:48:01Z'. Note that if no timezone offset is defined, the datetime will be taken as local time and localized using the picture position if available.",
    ),
    longitude: Optional[float] = typer.Option(
        default=None,
        help="override longitude of the image, in decimal degrees (WGS84 / EPSG:4326) (like `2.3522219` for Paris)",
    ),
    latitude: Optional[float] = typer.Option(
        default=None,
        help="override latitude of the image, in decimal degrees (WGS84 / EPSG:4326) (like `48.856614` for Paris)",
    ),
    picture_type: Optional[PictureType] = typer.Option(
        default=None,
        help="type of picture, `equirectangular` for 360° pictures, `flat` otherwise",
    ),
):
    """Override certain exiftags of a picture and write a new picture in another file"""
    from geopic_tag_reader import writer
    from dateutil.parser import parse

    capture_dt = parse(capture_time) if capture_time else None

    with open(input, "rb") as raw_input:
        updated_pic = writer.writePictureMetadata(
            raw_input.read(),
            writer.PictureMetadata(capture_time=capture_dt, longitude=longitude, latitude=latitude, picture_type=picture_type),
        )

        out = output or input
        if output is None:
            print(f"Ovewriting {input} metadatas")
        with open(out, "wb") as o:
            o.write(updated_pic)


if __name__ == "__main__":
    app()
