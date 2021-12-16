from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="EVRO ➡️ UZS"),KeyboardButton(text="DOLLAR ➡️ UZS")],
        [KeyboardButton(text="RUBL ➡️ UZS"),KeyboardButton(text='TENGE ➡️ UZS')],
        [KeyboardButton(text= '🔙 Orqaga')],

    ],
    resize_keyboard=True,
    # one_time_keyboard=True
)
