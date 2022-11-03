import os.path
import os
from pathlib import Path
import argparse

import requests
from dotenv import load_dotenv

from download_photo import download_photo


def download_photos_spacex(spacex_image_directory, spacex_last_launch):
    spacex_file_name = 'image_spacex'
    spacex_url = 'https://api.spacexdata.com/v4/launches'

    response = requests.get(spacex_url)
    response.raise_for_status()

    spacex_link = response.json(
    )[spacex_last_launch]['links']['flickr']['original']

    for number, image_url in enumerate(spacex_link):
        fullname = f'{number}{spacex_file_name}.jpg'
        file_path = os.path.join(spacex_image_directory, fullname)
        download_photo(image_url, file_path)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
      description='Номер запуска'
    )
    parser.add_argument('spacex_id', default=66, 
                        type=int, nargs='?')
    spacex_launch = parser.parse_args().spacex_id
    space_image_directory = 'images'
    Path(space_image_directory).mkdir(parents=True, exist_ok=True)
    download_photos_spacex(space_image_directory, spacex_launch)


if __name__ == "__main__":
    main()
