import requests
import os.path

from pathlib import Path
from download_photo import download_photo
from get_extension_link import get_extension_link
from dotenv import load_dotenv

def epic_photo(nasa_api_key):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {"api_key": nasa_api_key}
    epic_response = requests.get(epic_url, params=params)
    epic_response_links = epic_response.json()  
    for epic_picture in epic_response_links:
        epic_image_date = epic_picture['date']
        epic_image_name = epic_picture['image']
        epic_image_notime_date = epic_image_date.split()
        epic_image_formated_date = epic_image_notime_date[0].replace('-', '/')
        epic_link = f'https://api.nasa.gov/EPIC/archive/natural/{epic_image_formated_date}/png/{epic_image_name}.png'
        filename, expansion = (get_extension_link(epic_link))
        folder = 'images'
        fullname = f'{filename}{expansion}'
        file_path = os.path.join(folder, fullname)
        download_photo(epic_link, file_path, params)
 

def main():
    Path("images").mkdir(parents=True, exist_ok=True)

    load_dotenv()
    nasa_api_key = os.environ["NASA_API_KEY"]
    epic_photo(nasa_api_key)


if __name__=="__main__":
    main()