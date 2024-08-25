import logging
from aiogram import types
from data.config import ADMINS
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from loader import bot, dp
from utils.misc import subscription
from handlers.users.date import user
from handlers.users.date import channelget
#from keyboards.default.imagebackremove import imagremove




@dp.callback_query_handler(text="check_subs")
async def checker(call: types.CallbackQuery):
    #userr = user(user_id=call.from_user.id)
    # if user[-1] == None:
    #     pass

    # elif user[-1] == 'uzbek':
        #await call.answer()
    result = str()
    btn = InlineKeyboardMarkup()
    final_status = True
    for channel in channelget():
        status = await subscription.check(user_id=call.from_user.id,
                                              channel=channel)
        final_status *= status
        channel = await bot.get_chat(channel)
        if not status:
            invite_link = await channel.export_invite_link()
            btn.add(InlineKeyboardButton(text=f"❌ {channel.title}", url=invite_link))

    btn.add(InlineKeyboardButton(text="♻️Obunani tekshirish", callback_data="check_subs"))
    if final_status:
        await call.message.answer("Assalomu alaykum! Kerakli bo'limni tanlang")
        await call.message.delete()
    if not final_status:
        await call.answer('Kanalga obuna bolishingiz kerak!', cache_time=0.05, show_alert=True)