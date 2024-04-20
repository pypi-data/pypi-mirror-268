import os
from pathlib import Path
from colorama import Fore
from tqdm import tqdm
import requests

from .tools import get_meta, get_all_meta, str_to_time, set_meta, create_xmp

COLOR_GREEN = '#27AE60'
COLOR_YELLOW = '#F1C40F'
COLOR_RED = '#E74C3C'
COLOR_BLUE = '#3498DB'


def set_gps(path: str, user: str, token: str, config: dict, log_func, progress_func):
    assert os.path.isdir(path), f"Path does not exist: {path}"
    path = Path(path)

    log_func("Searching for images...")
    progress_func(0)
    images = []
    for file in path.glob(f'**/*'):
        if file.is_file():
            suffix = file.suffix.lower()[1:]
            if suffix in config['exif'] or suffix in config['xmp']:
                images.append(file)

    log_func("Reading GPS data...")
    ts_to_files = {}
    cnt_ok = cnt_todo = cnt_no_time = 0
    for idx, img in enumerate(images):
        progress_func(round(50 * (idx + 1) / len(images)))
        tm, lat, lon, alt = get_meta(img)
        if not tm:
            tqdm.write(f"{Fore.RED}{img.name} has no shooting time{Fore.RESET}")
            cnt_no_time += 1
            continue
        if not lat or not lon:
            ts = str_to_time(tm)
            if ts in ts_to_files:
                ts_to_files[ts].append(img)
            else:
                ts_to_files[ts] = [img]
            # tqdm.write(f"{Fore.YELLOW}{img.name} {tm}{Fore.RESET}")
            cnt_todo += 1
        else:
            # tqdm.write(f"{Fore.GREEN}{img.name} {tm} {lat} {lon} {alt}{Fore.RESET}")
            cnt_ok += 1
    log_func(f"Files with GPS:     {cnt_ok}", COLOR_GREEN)
    log_func(f"Files without GPS:  {cnt_todo}", COLOR_YELLOW)
    log_func(f"Files without time: {cnt_no_time}", COLOR_RED)

    if not cnt_todo:
        log_func(f"\nAll files have GPS data", COLOR_GREEN)
        return 

    log_func(f"Requesting GPS data...")
    domain = 'https://photogps.antonio-dev.com'
    # domain = 'http://127.0.0.1:8000'  # чтобы тестировать локально
    r = requests.post(
        f'{domain}/api/get-gps/',
        json={"timestamps": list(ts_to_files.keys())},
        auth=(user, token)
    )
    if r.status_code != 200:
        log_func(f"Error: {r.status_code}", COLOR_RED)
        log_func(r.text, COLOR_RED)
        return
    ts_to_loc = r.json()['ts_to_loc']
    log_func(f"GPS data received")

    log_func(f"Writing GPS data to files...")
    _len = len(ts_to_files.items())
    for idx, (ts, files) in enumerate(ts_to_files.items()):
        progress_func(50 + round(50 * (idx + 1) / _len))
        loc = ts_to_loc.get(str(ts))
        if loc:
            for img in files:
                if img.suffix.lower()[1:] in config['exif']:
                    set_meta(img, loc[0], loc[1], loc[2])
                    log_func(f"{img.name}: {loc} written to EXIF", COLOR_GREEN)
                else:
                    create_xmp(img, loc[0], loc[1], loc[2])
                    log_func(f"{img.name}: {loc} written to XMP", COLOR_BLUE)
        else:
            for img in files:
                log_func(f"{img.name} no location", COLOR_RED)
    log_func(f"DONE!", COLOR_GREEN)

