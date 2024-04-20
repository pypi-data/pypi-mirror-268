import os
from pathlib import Path
import yaml
from colorama import Fore


MODULE_PATH = Path(__file__).parent
USER_HOME = Path.home()


def load_config():
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
    if type(config.get('exif')) != list or type(config.get('xmp')) != list:
        print(f'{Fore.RED}"exif" and "xmp" must be set in config file {config_file}{Fore.RESET}.')
        exit(1)

    config['exif'] = [x.lower() for x in config['exif']]
    config['xmp'] = [x.lower() for x in config['xmp']]

    return config
