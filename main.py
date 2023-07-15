import os.path
import telegram
import argparse

from time import sleep
from pathlib import Path
from dotenv import load_dotenv


def publicate_picture(tg_chat_id, bot, publication_frequency, directory):
    picture_filepath = os.listdir(directory)
    while True:
        try:
            for filename in picture_filepath:
                filepath = os.path.join(directory, filename)
                send_message(tg_chat_id, bot, filepath)
                sleep(publication_frequency)
        except telegram.error.NetworkError:
            sleep(3)


def send_message(chat_id, bot, filepath):
    with open(filepath, 'rb') as file:
        bot.send_photo(chat_id=chat_id, photo=file)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description='Отправляет фотографии через бота в телеграм-канал.')
    parser.add_argument('--frequency', type=int, help='Количество секунд между отправкой изображений.', default=14400)
    parser.add_argument('--folder', type=str, help='Путь к папке c фотографиями.', default='images')
    args = parser.parse_args()
    Path(args.folder).mkdir(parents=True, exist_ok=True)

    tg_bot_token = os.environ["TG_BOT_TOKEN"]
    tg_chat_id = os.environ["TG_CHAT_ID"]
    publication_frequency = args.frequency
    bot = telegram.Bot(token=tg_bot_token)

    publicate_picture(tg_chat_id, bot, publication_frequency, args.folder)


if __name__ == "__main__":
    main()
