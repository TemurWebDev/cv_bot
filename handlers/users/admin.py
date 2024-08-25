import asyncio
from aiogram import types
from aiogram.types import ContentType
from aiogram.dispatcher import FSMContext
from keyboards.default.adminkeyboards import adminusers,admincommands
from handlers.users.date import userget,channelal,channelget,delete_channel,create_channel
from loader import bot
from keyboards.default.shablon import shablon_key

from loader import dp
from aiogram.dispatcher.filters.state import StatesGroup, State


class Reklama(StatesGroup):
    message = State()






ADMINS = [1363350178]



@dp.message_handler(text="cv", user_id=1363350178)
async def admincv(message: types.Message):

    await message.answer('Hush kelibsiz admen',reply_markup=shablon_key)



@dp.message_handler(text="admin panel", user_id=1363350178)
async def adminpanel(message: types.Message):

    await message.answer('admin panel',reply_markup=adminusers)



@dp.message_handler(chat_id=1363350178, text='users')
async def users(message: types.Message):
    countuser = userget()
    datauser = userget()[-45:]
    text = f"Interview Questions || Foydalanuvchilar soni: {len(countuser)}\n\n"
    for user in datauser:
        text += f"{user['id']}). || {user['first_name']} || @{user['last_name']} || {user['language']}\n"
    await message.answer(text)


@dp.message_handler(text="back", user_id=1363350178)
async def back_button(message: types.Message):

    await message.answer('Bosh menyu',reply_markup=admincommands)



@dp.message_handler(text="reklama",user_id=ADMINS)
async def bot_start(message: types.Message):
    await message.answer("reklama yuboring")
    await Reklama.message.set()


@dp.message_handler(content_types=ContentType.ANY,state=Reklama.message)
async def answer_fullname(message: types.Message, state: FSMContext):
    habar = message.text

    await state.update_data(
        {"habar": habar}
    )
    data = await state.get_data()
    reklama = data.get("habar")

    msg = reklama
    users = userget()
    for user in users:
        user_id = user['user_id']
        try:
            await message.send_copy(chat_id=user_id)
            await asyncio.sleep(0.05)
        except Exception as e:
            await bot.send_message(chat_id=ADMINS[0],text=f"{e}")
    await bot.send_message(chat_id=ADMINS[0],text=f"Reklama yuborildi! ✅")
    await state.finish()



class Channel(StatesGroup):
    name = State()
    channel_idi = State()


class Channel_delete(StatesGroup):
    channel_id = State()


@dp.message_handler(text="Kanal qo'shish", user_id=1363350178)
async def kanal_qoshish(message: types.Message):
    await message.answer("Kanal nomini yozing")
    await Channel.name.set()



@dp.message_handler(state=Channel.name)
async def channel_name(message: types.Message,state: FSMContext):
    name = message.text

    await state.update_data(
        {"name": name}
    )
    
    await message.answer("Kanal Id sini kiriting")
    await Channel.next()






@dp.message_handler(state=Channel.channel_idi)
async def channel_id(message: types.Message,state: FSMContext):
    channe_id = message.text

    await state.update_data(
        {"channe_id": channe_id}
    )

    data = await state.get_data()
    name = data.get("name")
    channelId = data.get("channe_id")

    try:
        create_channel(name,channelId)
        await bot.send_message(chat_id=1363350178,text="Kanal qo'shildi")
    except Exception as e:
        await bot.send_message(chat_id=1363350178,text=e)

    await state.finish()




@dp.message_handler(text="Kanal o'chirish", user_id=1363350178)
async def kanal_delete(message: types.Message):
    await message.answer("Kanal id sini yozing")
    await Channel_delete.channel_id.set()


@dp.message_handler(state=Channel_delete.channel_id)
async def channel_i(message: types.Message,state: FSMContext):
    channel_id = message.text

    await state.update_data(
        {"channel_id": channel_id}
    )

    data = await state.get_data()
    channelId = data.get("channel_id")

    try:
        delete_channel(str(channelId))
        await bot.send_message(chat_id=1363350178,text="Kanal o'chirildi")
    except Exception as e:
        await bot.send_message(chat_id=1363350178,text=e)

    await state.finish()


@dp.message_handler(text="Kanallar", user_id=1363350178)
async def kanal_qoshish(message: types.Message):
    data = channelal()
    text = f"Kanallar soni: {len(data)}\n\n"
    for channe in data:
        text+=f"{channe['name']}  ||  {channe['channel_id']}\n"

    await message.answer(text)



@dp.message_handler(text="channels", user_id=1363350178)
async def kanal_qoshish(message: types.Message):
    

    await message.answer(channelal())


