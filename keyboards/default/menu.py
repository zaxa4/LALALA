from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Николаевская оперативка'),
        ]
        [
            KeyboardButton(text="Захаровская видюха "),
            KeyboardButton(text="Барановский камень"),
        ],
    ],
    resize_keyboard=True
)