from pathlib import Path
from colorama import Fore
from tqdm import tqdm
import requests

from .tools import get_meta, get_all_meta, str_to_time, set_meta, set_author


def set_gps(path: str, user: str, token: str):
    path = Path(path)

    images = []
    # extensions = ['RAF', 'JPG', 'MP4']  RAF файлы ломаются при записи метаданных
    extensions = ['JPG', 'jpg', 'MP4']
    for ext in extensions:
        for img in path.glob(f'**/*.{ext}'):
            images.append(img)

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
                set_meta(img, loc[0], loc[1], loc[2])
                # set_author(img, 'Anton Silin')
                tqdm.write(f"{Fore.GREEN}{img.name} {loc}{Fore.RESET}")
        else:
            for img in files:
                tqdm.write(f"{Fore.RED}{img.name} no location{Fore.RESET}")

    # metas = []
    # for img in sorted(images):
    #     metas.append(get_all_meta(img))
    #
    # for key in metas[0]:
    #     # if 'GPS' not in key.upper():
    #     #     continue
    #     values = [meta.get(key) for meta in metas]
    #     if len(set(values)) == 1:
    #         print(f"{key.center(30)}: {values}")

