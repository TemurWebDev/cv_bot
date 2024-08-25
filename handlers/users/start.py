from aiogram import Bot, types
#from data.config import CHANNELS
from loader import bot
from aiogram.dispatcher.filters.builtin import CommandStart
from handlers.users.date import usercreate
from keyboards.default.adminkeyboards import admincommands,adminusers
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from handlers.users.date import channelget
from keyboards.default.shablon import shablon_key


from loader import dp
from utils.misc import subscription


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    first_name = message.from_user.first_name
    username = message.from_user.username
    user_id = message.from_user.id

    usercreate(first_name, username, user_id)
    if message.from_user.id == 1363350178:
        await bot.send_message(chat_id=1363350178, text='Siz adminsiz',reply_markup=admincommands)
    else:
        await message.reply(f"Salom\nKerakli bo'limni tanlang. {message.from_user.first_name}",parse_mode="HTML",reply_markup=shablon_key)
        await bot.send_message(chat_id=1363350178,text=f"{message.from_user.first_name} botga /start bosdi")

    user = message.from_user.id
    final_status = True
    btn = InlineKeyboardMarkup(row_width=1)
    for channel in channelget():
        status = await subscription.check(user_id=user, channel=channel)
        final_status *= status
        chat = await bot.get_chat(channel)
        if status:
            invite_link = await chat.export_invite_link()
            btn.insert(InlineKeyboardButton(text=f"✅ {chat.title}", url=invite_link))
        if not status:
            invite_link = await chat.export_invite_link()
            btn.insert(InlineKeyboardButton(text=f"❌ {chat.title}", url=invite_link))
    btn.add(InlineKeyboardButton(text="♻️Obunani tekshirish", callback_data="check_subs"))
    if final_status:
        if message.from_user.id == 1363350178:
            await bot.send_message(chat_id=message.from_user.id,
                                       text=f"Assalomu alaykum {message.from_user.first_name} siz adminsiz",
                                       reply_markup=admincommands)
        else:
            await message.answer(f"Assalomu alaykum {message.from_user.full_name}!\n"
                                     f"Botdan foydalanish uchun kerakli bo'limni tanlang!")
    if not final_status:
        await message.answer("Botdan to'liq foydalanish uchun quyidagi kanallarga obuna bo'ling!",
                                 disable_web_page_preview=True, reply_markup=btn)


