import requests
import os.path

from dotenv import load_dotenv
from download_photo import download_photo
from get_extension_link import get_extension_link
from pathlib import Path

def fetch_nasa_pictures(NASA_API_KEY):
    nasa_url = "https://api.nasa.gov/planetary/apod" 
    params = {"api_key": NASA_API_KEY, 
    "count": 35}
    nasa_response = requests.get(nasa_url, params=params)
    nasa_pictures_links = nasa_response.json()
    for nasa_picture in nasa_pictures_links:
        if nasa_picture['media_type'] == 'image':
            nasa_picture_located_link = nasa_picture['url']
            filename, expansion = get_extension_link(nasa_picture_located_link) 
            if not expansion:
                continue
            folder = 'images'    
            fullname = f'{filename}{expansion}'   
            file_path = os.path.join(folder, fullname)
            download_photo(nasa_picture_located_link, file_path)


def main():
    Path("images").mkdir(parents=True, exist_ok=True)

    load_dotenv()
    NASA_API_KEY = os.environ["NASA_API_KEY"]
    fetch_nasa_pictures(NASA_API_KEY)


if __name__ == "__main__":
    main()

