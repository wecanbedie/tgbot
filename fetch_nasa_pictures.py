import requests
import os.path
import argparse

from dotenv import load_dotenv
from download_photo import download_photo
from get_extension_link import get_file_format_link
from pathlib import Path

def fetch_nasa_pictures(nasa_api_key, count):
    nasa_url = "https://api.nasa.gov/planetary/apod" 
    params = {"api_key": nasa_api_key, 
    "count": count}
    nasa_response = requests.get(nasa_url, params=params)
    nasa_pictures_links = nasa_response.json()
    for nasa_picture in nasa_pictures_links:
        if nasa_picture['media_type'] == 'image':
            nasa_picture_located_link = nasa_picture['url']
            filename, file_format = get_file_format_link(nasa_picture_located_link) 
            if not file_format:
                continue
            folder = 'images'    
            fullname = f'{filename}{file_format}'   
            file_path = os.path.join(folder, fullname)
            download_photo(nasa_picture_located_link, file_path)


def main():
    Path("images").mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser(description='Укажите количество фотографий.')
    parser.add_argument('--count', type=int, help='Количество скачиваемых фотографий.', default=35)
    args = parser.parse_args() 

    load_dotenv()
    nasa_api_key = os.environ["NASA_API_KEY"]
    fetch_nasa_pictures(nasa_api_key, args.count)


if __name__ == "__main__":
    main()

