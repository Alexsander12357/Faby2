import asyncio
import logging
from aiogram import Bot, Dispatcher, types, executor

logging.basicConfig(level=logging.INFO)
bot = Bot(token="5624081440:AAFk9hbQH7Vq01l0Cg1bfS5qrGeAqKl65WE")
dp = Dispatcher(bot)
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
greet_markup = ReplyKeyboardMarkup()
button_hi = KeyboardButton("Что ты умеешь?")
button_1 = KeyboardButton("Кто ты?")
button_2 = KeyboardButton("Мне нравится ГТА 5")
button_3 = KeyboardButton("Мне нравится Call of duty WW2")
button_4 = KeyboardButton("Мне нравится бравл старс")
button_5 = KeyboardButton("Мне нравится фнаф 1")
button_6 = KeyboardButton("Мне нравится фнаф 9")
button_7 = KeyboardButton("Мне нравится Stray")
button_8 = KeyboardButton("Мне нравится Сталкер тень чернобыля")
button_9 = KeyboardButton("Мне нравится metro exodus")
button_10 = KeyboardButton("Ты бот?")
button_11 = KeyboardButton("Мне нравится дота 2")
button_12 = KeyboardButton("Мне нравится майнкрафт")
button_13 = KeyboardButton("Мне нравится U torrent")
button_14 = KeyboardButton("Мне нравится roblox")



greet_markup.add(button_hi)
greet_markup.add(button_1)
greet_markup.add(button_2)
greet_markup.add(button_3)
greet_markup.add(button_4)
greet_markup.add(button_5)
greet_markup.add(button_6)
greet_markup.add(button_7)
greet_markup.add(button_8)
greet_markup.add(button_9)
greet_markup.add(button_10)
greet_markup.add(button_11)
greet_markup.add(button_12)
greet_markup.add(button_13)
greet_markup.add(button_14)

@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Heloo!", reply_markup=greet_markup)
@dp.message_handler()
async def cmd_text(message: types.Message):
    if message.text == "Кто ты?":
        await bot.send_message(message.from_user.id, "Я бот игр")
    elif message.text == "Мне нравится ГТА 5":
        await bot.send_message(message.from_user.id, "Эта: https://torrent-mass.ru/adventure/395-1-gta-5-pc-3.html")
    elif message.text == "Мне нравится Call of duty WW2":
        await bot.send_message(message.from_user.id, "Эта ссылка для тебя:\n https://rutor-game.info/1707-call-of-duty-wwii-digital-deluxe-edition-build-7831931-dlcs-2017-pc-repack.html")
    elif message.text == "Мне нравится бравл старс":
        await message.reply("Тогда переходи по этой ссылке: https://pcigry.com/7-brawl-stars.html")
    elif message.text == "Мне нравится фнаф 1":
        await message.reply("Тогда переходи по этой ссылке:\n https://s5.torrent-repack.club/download/igry_2014_goda/five-nights-at-freddys/14-1-0-1376")
    elif message.text == "Мне нравится фнаф 9":
        await message.reply("Тогда переходи по этой ссылке:\n https://itorrents-igruha.org/6449-five-nights-at-freddys-security-breach.html")
    elif message.text == "Мне нравится Stray":
        await message.reply("Тогда эта ссыка тебе:\n https://itorrents-igruha.org/5338-stray.html")
    elif message.text == "Мне нравится Сталкер тень чернобыля":
        await message.reply("Тогда эта ссыка тебе:\n https://torrent-mass.ru/action/269-stalker-ten-chernobylya.html")
    elif message.text == "Мне нравится metro exodus":
        await message.reply("Тогда эта ссыка тебе:\n https://torrent-mass.ru/action/462-metro-exodus-pc-4.html")
    elif message.text == "Ты бот?":
        await message.reply("Нет, ты бот(хахахахахахаха)")
    elif message.text == "Что ты умеешь?":
        await bot.send_message(message.from_user.id, "\n Я могу сказать какая ссылка для скачивания твоей любимой игры например напиши мне: Мне нравится Call of duty WW2 ")
    elif message.text == "Мне нравится дота 2":
        await message.reply("Тогда эта ссыка тебе:\n https://store.steampowered.com/app/570/Dota_2/?l=russian")
    elif message.text == "Мне нравится майнкрафт":
        await message.reply("Тогда эта ссыка тебе:\n https://tlauncher.org/#osselector")
    elif message.text == "Мне нравится U torrent":
        await message.reply("Тогда эта ссыка тебе:\n https://www.utorrent.com/intl/ru/web/downloads/complete/track/stable/os/win/")
    elif message.text == "Мне нравится roblox":
        await message.reply(
            "Тогда эта ссыка тебе:\n RobloxPlayerLauncher (3).exe ")




    else:
        await  bot.send_message(message.from_user.id, 'Мне нечего ответить')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)