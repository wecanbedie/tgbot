import requests
import os.path
#import datetime

from pathlib import Path
from download_photo import download_photo
from get_extension_link import get_file_format_link
from dotenv import load_dotenv
from datetime import datetime

def fetch_epic_photo(nasa_api_key):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {"api_key": nasa_api_key}
    response = requests.get(url, params=params)
    response_links = response.json()  
    for picture in response_links:
        image_date = picture['date']#.datetime.fromisoformat(date)
        image_name = picture['image'] 
        formated_image_date = datetime.fromisoformat(image_date).strftime("%Y/%m/%d")
        link = f'https://api.nasa.gov/EPIC/archive/natural/{formated_image_date}/png/{image_name}.png'
        filename, expansion = get_file_format_link(link)
        folder = 'images'
        fullname = f'{filename}{expansion}'
        file_path = os.path.join(folder, fullname)
        download_photo(link, file_path, params)
        
 

def main():
    Path("images").mkdir(parents=True, exist_ok=True)

    
    load_dotenv()
    nasa_api_key = os.environ["NASA_API_KEY"]
    fetch_epic_photo(nasa_api_key)


if __name__=="__main__":
    main()

