import os.path
import telegram

from time import sleep
from pathlib import Path
from dotenv import load_dotenv


def tg_picture_bot(TG_CHAT_ID, bot, publication_frequency):
    directory = 'images'
    picture_filepath = os.listdir(directory)
    while True:
        try:
            for filename in picture_filepath:
                filepath = os.path.join(directory, filename)
                send_message(TG_CHAT_ID, bot, filepath)
                sleep(int(publication_frequency))
        except ConnectionError:
            sleep(20)


def send_message(chat_id, bot, filepath):
    with open(filepath, 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file)


def main():
    Path("images").mkdir(parents=True, exist_ok=True)
    
    load_dotenv()
    TG_BOT_TOKEN = os.environ["TG_BOT_TOKEN"]
    TG_CHAT_ID = os.environ["TG_CHAT_ID"]
    publication_frequency = os.getenv('PUBLICATION_FREQUENCY', default=14400)
    bot = telegram.Bot(token=TG_BOT_TOKEN)

    
    tg_picture_bot(TG_CHAT_ID, bot, publication_frequency)


    

if __name__ == "__main__":
    main()

