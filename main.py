import requests
import os.path
import telegram
import time

from pprint import pprint
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import urlparse, unquote
from fetch_spacex_last_launch import download_photos_spacex


def download_photo(link, file_path, params=None):
    response = requests.get(link, params=params)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)
 

def tg_picture_bot(chat_id, bot, publication_frequency):
    directory = 'images'
    picture_filepath = os.listdir(directory)
    for filename in picture_filepath:
        filepath = os.path.join(directory, filename)
        send_message(chat_id, bot, filepath)
        time.sleep(int(publication_frequency))


def send_message(chat_id, bot, filepath):
    with open(filepath, 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file)


def main():
    Path("images").mkdir(parents=True, exist_ok=True)
    
    TG_BOT_TOKEN = os.environ["BOT_TOKEN"]
    chat_id = os.environ["CHAT_ID"]
    publication_frequency = os.environ['PUBLICATION_FREQUENCY']
    bot = telegram.Bot(token=TG_BOT_TOKEN)


    tg_picture_bot(chat_id, bot, publication_frequency)


    

if __name__ == "__main__":
    main()

