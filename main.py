import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from buttons1 import menu 
import requests
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    user = message.from_user.first_name
    await message.answer(f"Assalomu aleykum {user}😊" , reply_markup = menu)
    


@dp.message_handler(Text(equals=["EVRO ➡️ UZS"]))
async def accounts(message: types.Message):
    url1 = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur/uzs.json").json()
    msg1 = f"100 evro - {round(url1['uzs'],2)*100} so'm "
    await message.answer(msg1)    


@dp.message_handler(Text(equals=["DOLLAR ➡️ UZS"]))
async def contacts(message):
    url2 = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/usd/uzs.json").json()
    msg2 = f"100 dollar - {round(url2['uzs'],2)*100} so'm "
    await message.answer(msg2)

@dp.message_handler(Text(equals=["RUBL ➡️ UZS"]))
async def send_contact(message):
    url3 = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/rub/uzs.json").json()
    msg3 = f"100 rubl - {round(url3['uzs'],2)*100} so'm "
    await message.answer(msg3)


@dp.message_handler(Text(equals=["TENGE ➡️ UZS"]))
async def comments(message):
    url4 = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/kzt/uzs.json").json()
    msg4 = f"100 tenge - {round(url4['uzs'],2)*100} so'm "
    await message.answer(msg4)

@dp.message_handler(Text(equals=["🔙 Orqaga"]))
async def boshsahifa(message):
    await message.answer("Qaytadan ishga tushurish uchun /start bosing!")

executor.start_polling(dp, skip_updates=True)