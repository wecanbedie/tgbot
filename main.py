import os.path
import telegram

from time import sleep
from pprint import pprint
from pathlib import Path
from dotenv import load_dotenv
from urllib.parse import urlparse, unquote
from fetch_spacex_last_launch import download_photos_spacex
from download_photo import download_photo


def tg_picture_bot(TG_CHAT_ID, bot, publication_frequency):
    directory = 'images'
    picture_filepath = os.listdir(directory)
    while True:
        for filename in picture_filepath:
            filepath = os.path.join(directory, filename)
            send_message(TG_CHAT_ID, bot, filepath)
            sleep(int(publication_frequency))


def send_message(chat_id, bot, filepath):
    with open(filepath, 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file)


def main():
    Path("images").mkdir(parents=True, exist_ok=True)
    
    load_dotenv()
    TG_BOT_TOKEN = os.environ["TG_BOT_TOKEN"]
    TG_CHAT_ID = os.environ["TG_CHAT_ID"]
    publication_frequency = os.environ['PUBLICATION_FREQUENCY']
    bot = telegram.Bot(token=TG_BOT_TOKEN)

    
    tg_picture_bot(TG_CHAT_ID, bot, publication_frequency)


    

if __name__ == "__main__":
    main()

