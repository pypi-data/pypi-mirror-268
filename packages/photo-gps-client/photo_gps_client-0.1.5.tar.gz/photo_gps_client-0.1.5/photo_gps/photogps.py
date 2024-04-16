import argparse
import os
from pathlib import Path
import yaml
from colorama import Fore
from subprocess import run

from .commands import set_gps


MODULE_PATH = Path(__file__).parent
USER_HOME = Path.home()


def app():
    # check if config file exists
    config_file = USER_HOME / 'photogps.yaml'
    if not os.path.exists(config_file):
        # copy default config file to user's home directory
        with open(MODULE_PATH / 'photogps.example.yaml') as f:
            with open(config_file, 'w') as f2:
                f2.write(f.read())
        print(
            f'{Fore.RED}Config file not found. {Fore.RESET}I created default config file {Fore.GREEN}{config_file}{Fore.RESET} for you. Please edit it and run the script again.')
        exit(1)

    with open(config_file) as f:
        config = yaml.safe_load(f)
    if not config.get('auth') or not config['auth'].get('user') or not config['auth'].get('token'):
        print(f'{Fore.RED}No Auth params in {config_file}{Fore.RESET}.')
        exit(1)

    # Создаем парсер
    parser = argparse.ArgumentParser(description="Photo GPS")
    parser.add_argument("--path", type=str, default=config.get('default-path', ''), help="Folder with images")
    args = parser.parse_args()

    # test_photo_path = MODULE_PATH.parent / 'photo'
    # run(f"rm -f {test_photo_path}/test/*", shell=True)
    # run(f"cp {test_photo_path}/src/* {test_photo_path}/test/", shell=True)

    if args.path:
        path = args.path
    else:
        path = input('Enter path to the folder with images: ')
    if not os.path.exists(path):
        print(f'{Fore.RED}Path does not exist{Fore.RESET}')
        exit(1)

    if input(f'Path: {Fore.GREEN}{path}{Fore.RESET}\n Continue? [y/n]: ') != 'y':
        exit(1)

    set_gps(args.path, config['auth']['user'], config['auth']['token'])


if __name__ == '__main__':
    app()

