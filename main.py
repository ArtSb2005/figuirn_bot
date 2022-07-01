import time
import requests
from aiogram import Bot, Dispatcher, executor, types
import logging
from instagrapi import Client

cl = Client()
cl.login('stefaniia.prudnikova', "v7kiIiSz")
bot = Bot('5324237373:AAG05maRhj2-Sibyo5WbTgZItejl5D_a1So')
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
CHANNEL_ID = '@fnl_test' # это должен быть int, например -1006666666666

last_post = ''
@dp.message_handler(commands="start")
async def send_message(message: types.Message):
    while True:
        global last_post
        medias = cl.user_medias_v1(36328749738, 1)
        if last_post == medias[0].pk:
            print(last_post)
            pass
        else:
            print(last_post)
            media = types.MediaGroup()
            last_post = medias[0].pk
            text = medias[0].caption_text
            a = 0
            for i in medias[0].resources:
                a +=1
                if a == 1:
                    media.attach_photo(f'{i.thumbnail_url}', text.split('#')[0])
                else:
                    media.attach_photo(f'{i.thumbnail_url}')
            if a > 1:
                await bot.send_media_group(CHANNEL_ID, media=media)
            elif a == 0:
                await bot.send_photo(CHANNEL_ID, photo=medias[0].thumbnail_url, caption=text.split('#')[0])
        time.sleep(100)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)

