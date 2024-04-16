from pathlib import Path
from exiftool import ExifToolHelper
import arrow


def str_to_time(time_str: str) -> int:
    # Конвертация строки в объект Arrow в локальной таймзоне
    arrow_obj = arrow.get(time_str, "YYYY:MM:DD HH:mm:ss", tzinfo="local")

    # Конвертация объекта Arrow в Unix timestamp
    unix_timestamp = arrow_obj.int_timestamp

    return unix_timestamp


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


def set_author(img: Path, name: str):
    with ExifToolHelper() as et:
        res = et.set_tags(
            str(img),
            {
                'Artist': name,
            },
            params=['-overwrite_original']
        )
