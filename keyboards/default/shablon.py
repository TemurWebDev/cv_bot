from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

shablon_key = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Shablonlar"),
        ],
        [
            KeyboardButton(text="cv view"),
        ],
                [
            KeyboardButton(text="My cv"),
        ],


    ],
    resize_keyboard=True
)



phonkey = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon nomer",request_contact=True),
        ],
        
          
    ],
    resize_keyboard=True
)


accaunt_cv = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="cv view"),
            KeyboardButton(text="edit cv"),
        ],
        [
            KeyboardButton(text="Bosh menu"),
        ],
        
          
    ],
    resize_keyboard=True
)

edit_cv = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="add education"),
        ],
        [
            KeyboardButton(text="edit personal info"),
            KeyboardButton(text="edit education"),
        ],
        [
            KeyboardButton(text="edit img"),
        ],
        
        [
            KeyboardButton(text="Orqaga"),
        ],
        
          
    ],
    resize_keyboard=True
)

