import os.path
import os
import requests
import argparse

from pathlib import Path
from download_photo import download_photo


def download_photos(spacex_image_directory, spacex_launch):
    spacex_file_name = 'image_spacex'
    spacex_url = 'https://api.spacexdata.com/v4/launches'

    response = requests.get(spacex_url)
    response.raise_for_status()

    spacex_link = response.json()[spacex_launch]['links']['flickr']['original']

    for number, image_url in enumerate(spacex_link):
        fullname = f'{number}{spacex_file_name}.jpg'
        file_path = os.path.join(spacex_image_directory, fullname)
        download_photo(image_url, file_path)


def main():
    parser = argparse.ArgumentParser(description='Скачивает фото c последнего запуска.')
    parser.add_argument('--folder', type=str, help='Путь к папке c фотографиями.', default='images')
    parser.add_argument('--spacex_id', default=66, type=int, nargs='?')
    args = parser.parse_args()

    spacex_launch = args.spacex_id
    space_image_directory = args.folder
    
    Path(space_image_directory).mkdir(parents=True, exist_ok=True)
    download_photos(space_image_directory, spacex_launch)


if __name__ == "__main__":
    main()
