from pathlib import Path
from exiftool import ExifToolHelper
import arrow
import os
from pathlib import Path
import yaml
from colorama import Fore
from jinja2 import Environment, PackageLoader, select_autoescape


def str_to_time(time_str: str) -> int:
    # Конвертация строки в объект Arrow в локальной таймзоне
    arrow_obj = arrow.get(time_str, "YYYY:MM:DD HH:mm:ss", tzinfo="local")

    # Конвертация объекта Arrow в Unix timestamp
    unix_timestamp = arrow_obj.int_timestamp

    return unix_timestamp


def deg_to_dms(deg, lat_or_lon):
    letter = ''
    if lat_or_lon == 'lat':
        letter = 'N' if deg > 0 else 'S'
    elif lat_or_lon == 'lon':
        letter = 'E' if deg > 0 else 'W'
    deg = abs(deg)
    d = int(deg)
    md = abs(deg - d) * 60
    m = int(md)
    sd = round((md - m) * 60, 2)
    # return [d, m, sd]
    return f"{d},{m},{sd}{letter}"

def get_all_meta(img: Path) -> dict:
    with ExifToolHelper() as et:
        meta = et.get_tags(str(img), [])
        return meta[0]


def get_meta(img: Path) -> [str, float, float, int]:
    with ExifToolHelper() as et:
        meta = et.get_tags(
            str(img),
            ['EXIF:DateTimeOriginal', 'EXIF:GPSLatitude', 'EXIF:GPSLongitude', 'EXIF:GPSAltitude']
        )
        meta = meta[0]
        # TODO перевести время в unixtimestamp исходя из текущего часового пояса
        return (
            meta.get('EXIF:DateTimeOriginal'),
            meta.get('EXIF:GPSLatitude'),
            meta.get('EXIF:GPSLongitude'),
            meta.get('EXIF:GPSAltitude')
        )


def set_meta(img: Path, lat: float, lon: float, alt: int):
    with ExifToolHelper() as et:
        res = et.set_tags(
            str(img),
            {
                'EXIF:GPSLatitude': abs(lat),
                'EXIF:GPSLatitudeRef': 'N' if lat > 0 else 'S',
                'EXIF:GPSLongitude': abs(lon),
                'EXIF:GPSLongitudeRef': 'E' if lon > 0 else 'W',
                'EXIF:GPSAltitude': abs(alt),
                'EXIF:GPSAltitudeRef': 0 if alt > 0 else 1
            },
            params=['-overwrite_original']
        )


def create_xmp(img: Path, lat: float, lon: float, alt: int):
    env = Environment(
        loader=PackageLoader('photo_gps', 'jinja'),
        autoescape=select_autoescape(['xml'])
    )
    tpl = env.get_template('xmp.jinja')
    file_content = tpl.render(lat=deg_to_dms(lat, 'lat'), lon=deg_to_dms(lon, 'lon'), alt=alt)
    xmp_file = img.with_suffix('.xmp')
    with open(xmp_file, 'w') as f:
        f.write(file_content)


def set_author(img: Path, name: str):
    with ExifToolHelper() as et:
        res = et.set_tags(
            str(img),
            {
                'Artist': name,
            },
            params=['-overwrite_original']
        )
