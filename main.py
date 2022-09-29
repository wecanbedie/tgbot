from sqlite3 import paramstyle
from urllib import response
import requests
import os.path
import telegram

from pprint import pprint
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import urlparse, unquote







def download_photo(link, file_path, params=None):
    response = requests.get(link, params=params)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)
        

def get_extension_link(link):
    link_unquote = unquote(link)
    parsed_link = urlparse(link_unquote)
    link_path = parsed_link.path
    path, fullname = os.path.split(link_path)
    filename, expansion = os.path.splitext(fullname)
    return filename, expansion
    

def fetch_spacex_last_launch():
    spacex_url = "https://api.spacexdata.com/v5/launches"
    spacex_response = requests.get(spacex_url)
    spacex_launches = spacex_response.json()
    for spacex_launch in spacex_launches:
        if spacex_launch["links"]["flickr"]["original"]:
            spacex_picture_links = spacex_launch["links"]["flickr"]["original"]
    for index_image, link in enumerate(spacex_picture_links):
        file_path = f'images/images_{index_image}.jpeg'
        download_photo(link, file_path)



def fetch_nasa_pictures(NASA_API_KEY):
    nasa_url = "https://api.nasa.gov/planetary/apod" 
    params = {"api_key": NASA_API_KEY, 
    "count": 35}
    nasa_response = requests.get(nasa_url, params=params)
    nasa_pictures_links = nasa_response.json()
    for nasa_picture in nasa_pictures_links:
        if nasa_picture['url']:
            nasa_picture_located_link = nasa_picture['url']
            filename, expansion = (get_extension_link(nasa_picture_located_link)) 
            if not expansion:
                break
            folder = 'images'    
            fullname = f'{filename}{expansion}'   
            file_path = os.path.join(folder, fullname)
            download_photo(nasa_picture_located_link, file_path)



def epic_photo(NASA_API_KEY):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {"api_key": NASA_API_KEY}
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
 


def tg_picture_bot(chat_id, bot):
    #directory = 'images'
    #picture_filepath = os.listdir(directory)

    #for picture in 
    folder = 'images'
    filename = 'antennagal_cxo.jpg'
    file_path = os.path.join(folder, filename)
    bot.send_photo(chat_id=chat_id, photo=open(file_path, 'rb'))





def main():
    Path("images").mkdir(parents=True, exist_ok=True)
    

    load_dotenv()
    NASA_API_KEY = os.environ["API_KEY"]
    TG_BOT_TOKEN = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHAT_ID"]
    bot = telegram.Bot(token=TG_BOT_TOKEN)

    #fetch_nasa_pictures(NASA_API_KEY)
    #epic_photo(NASA_API_KEY)
    #fetch_spacex_last_launch()
    tg_picture_bot(chat_id, bot)

if __name__ == "__main__":
    main()  

