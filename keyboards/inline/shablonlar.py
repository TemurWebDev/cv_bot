from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton




cv = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='cv 1',callback_data='cv1'),
            InlineKeyboardButton(text='cv 2',callback_data='cv2'),
            InlineKeyboardButton(text='cv 3',callback_data='cv3'),
        ],
         [
            InlineKeyboardButton(text='🔙 Back',callback_data='orqaga'),
            
        ],
    ]
)



cv1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='create cv 1',callback_data='startcv1'),
        ],
        [
            InlineKeyboardButton(text='🔙 Back',callback_data='ortga'),
        ],
    ]
)