from pathlib import Path
from colorama import Fore
from tqdm import tqdm
import requests

from .tools import get_meta, get_all_meta, str_to_time, set_meta, create_xmp


def set_gps(path: Path, user: str, token: str, config: dict):
    images = []
    for file in path.glob(f'**/*'):
        if file.is_file():
            suffix = file.suffix.lower()[1:]
            if suffix in config['exif'] or suffix in config['xmp']:
                images.append(file)

    ts_to_files = {}

    cnt_ok = cnt_todo = cnt_no_time = 0
    for img in tqdm(images, desc="Reading images"):
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
    print(f"{Fore.GREEN}Files with GPS: {cnt_ok}{Fore.RESET}")
    print(f"{Fore.YELLOW}Files without GPS: {cnt_todo}{Fore.RESET}")
    print(f"{Fore.RED}Files without time: {cnt_no_time}{Fore.RESET}")
    print()

    if not cnt_todo:
        print(f"{Fore.GREEN}All files have GPS data{Fore.RESET}")
        return 

    # for ts, files in ts_to_files.items():
    #     print(f"{ts}: {files}")

    domain = 'https://photogps.antonio-dev.com'
    # domain = 'http://127.0.0.1:8000'  # чтобы тестировать локально
    r = requests.post(
        f'{domain}/api/get-gps/',
        json={"timestamps": list(ts_to_files.keys())},
        auth=(user, token)
    )
    if r.status_code != 200:
        print(f"{Fore.RED}Error: {r.status_code}{Fore.RESET}")
        print(r.text)
        return
    ts_to_loc = r.json()['ts_to_loc']

    for ts, files in tqdm(ts_to_files.items(), desc="Writing GPS data"):
        loc = ts_to_loc.get(str(ts))
        if loc:
            for img in files:
                if img.suffix.lower() in config['exif']:
                    set_meta(img, loc[0], loc[1], loc[2])
                    _mode = f'{Fore.BLUE}written to EXIF{Fore.RESET}'
                else:
                    create_xmp(img, loc[0], loc[1], loc[2])
                    _mode = f'{Fore.CYAN}created .XMP file{Fore.RESET}'
                tqdm.write(f"{img.name} {loc} {_mode}")
        else:
            for img in files:
                tqdm.write(f"{Fore.RED}{img.name} no location{Fore.RESET}")

