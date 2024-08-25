from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admincommands = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="admin panel"),
            KeyboardButton(text="cv")
        ],

    ],
    resize_keyboard=True
)

adminusers = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="users"),
        ],
        [
            KeyboardButton(text="reklama"),
        ],
        [
            KeyboardButton(text="Javob"),
        ],
        [
            KeyboardButton(text="Kanal qo'shish"),
            KeyboardButton(text="Kanal o'chirish")
        ],
        [
            KeyboardButton(text="Kanallar")
        ],
        [
            KeyboardButton(text="back")
        ],
    ],
    resize_keyboard=True
)
