import argparse
import os
from pathlib import Path
import yaml
from colorama import Fore
from subprocess import run

from .commands import set_gps
from .config import load_config





def app():
    config = load_config()

    # Создаем парсер
    parser = argparse.ArgumentParser(description="Photo GPS")
    parser.add_argument("--path", type=str, default=config.get('default-path', ''), help="Folder with images")
    args = parser.parse_args()

    # test_photo_path = MODULE_PATH.parent / 'photo'
    # run(f"rm -f {test_photo_path}/test/*", shell=True)
    # run(f"cp {test_photo_path}/src/* {test_photo_path}/test/", shell=True)

    if args.path:
        path = Path(args.path)
    else:
        path = Path(input('Enter path to the folder with images: '))
    if not os.path.exists(path):
        print(f'{Fore.RED}Path does not exist{Fore.RESET}')
        exit(1)

    if input(f'Path: {Fore.GREEN}{path.resolve()}{Fore.RESET}\n Continue? [y/n]: ') != 'y':
        exit(1)

    set_gps(path, config['auth']['user'], config['auth']['token'], config)


if __name__ == '__main__':
    app()

