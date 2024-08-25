from aiogram import Bot, types
from loader import bot
from loader import dp
from aiogram.types import CallbackQuery,ReplyKeyboardRemove
from aiogram.types import InputFile
from keyboards.inline.shablonlar import cv1, cv
from keyboards.default.shablon import shablon_key,phonkey,accaunt_cv,edit_cv

from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType
from .date import userpersonalinfo,userperinfo,edit_userinfo


from handlers.users.cv1file import create_image_with_greeting




class PersonalDanny(StatesGroup):
    name = State()
    job = State()
    rasm = State()
    Tel = State()
    telegram_username = State()
    email = State()
    addres = State()


class Education(StatesGroup):
    name = State()
    diskreption = State()
    date = State()



class Skills(StatesGroup):
    name = State()



class Edit_img(StatesGroup):
    rasm = State()






@dp.message_handler(text="Shablonlar")
async def adminpanel(message: types.Message):

    
    await message.answer('Shablonlardan birini tanlang!',reply_markup=cv)


@dp.message_handler(text="Bosh menu")
async def adminpanel(message: types.Message):

    
    await message.answer('Bosh menu',reply_markup=shablon_key)


@dp.message_handler(text="Orqaga")
async def adminpanel(message: types.Message):

    
    await message.answer('my accaunt',reply_markup=accaunt_cv)


@dp.message_handler(text="My cv")
async def adminpanel(message: types.Message):

    
    await message.answer('my accaunt',reply_markup=accaunt_cv)


@dp.message_handler(text="edit cv")
async def adminpanel(message: types.Message):

    
    await message.answer("Qaysi qismni o'zgartirmoqchisz",reply_markup=edit_cv)



@dp.message_handler(text="edit personal info")
async def adminpanel(message: types.Message):

    
    await message.answer(f"Ismingizni kiriting!")
    await PersonalDanny.name.set()



@dp.callback_query_handler(text="cv1",state=None)
async def start_question(call: CallbackQuery):

    await call.message.delete()
    await call.answer(cache_time=60)

    photo_file = InputFile(path_or_bytesio="C:/Users/User/Desktop/cv_bot/handlers/files/img/shablon1.jpg")
    await call.message.answer_photo(
        photo_file,reply_markup=cv1
    )

    



    
@dp.callback_query_handler(text="orqaga",state=None)
async def start_question(call: CallbackQuery):

    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer('Bosh sahifa,',reply_markup=shablon_key)



@dp.callback_query_handler(text="ortga",state=None)
async def start_question(call: CallbackQuery):

    await call.message.delete()
    await call.answer(cache_time=60)
    await call.message.answer('Shablonlardan birini tanlang!,',reply_markup=cv)



# @dp.callback_query_handler(text="startcv1",state=None)
# async def start_question(call: CallbackQuery):

#     await call.message.delete()
#     await call.answer(cache_time=60)

#     img = f"C:/Users/User/Desktop/cv_bot/handlers/files/img/shablon1.jpg"
#     file = f"C:/Users/User/Desktop/cv_bot/handlers/files/file/{call.from_user.id}.pdf"

#     create_image_with_greeting(file,img)
#     await call.message.answer('Yaratildi')

#     files = f"C:/Users/User/Desktop/cv_bot/handlers/files/file/{call.from_user.id}.pdf"
#     with open(files, "rb") as file:
#         # Document jo'natish
#         await bot.send_document(chat_id=call.from_user.id, document=file)


@dp.callback_query_handler(text="startcv1",state=None)
async def start_question(call: CallbackQuery):

    await call.message.delete()
    await call.answer(cache_time=60)

    # await call.message.answer(f"Ismingizni kiriting!")
    # await PersonalDanny.name.set()


    if userperinfo(str(call.from_user.id)) != "null":
        await call.message.answer(f"Siz cv yaratgansiz, yangi cv yaratish uchun new cv tugmasidan foydalaning!!\nEslatma siz faqat 2 ta cv yaratolasiz.\nyaratilgan cv larni tahrirlashingiz mumkun!")
    else:
        await call.message.answer(f"Ismingizni kiriting!")
        await PersonalDanny.name.set()


@dp.message_handler(state=PersonalDanny.name)
async def answer_city(message: types.Message, state: FSMContext):

    name = message.text[:20]

    await state.update_data(
            {"name": name}
        )
    

    await message.answer(f"Kasbingizni kiriting!")
    await PersonalDanny.next()

    

@dp.message_handler(state=PersonalDanny.job)
async def answer_city(message: types.Message, state: FSMContext):

    job = message.text[:20]

    await state.update_data(
            {"job": job}
        )
    

    await message.answer(f"Shaxsiy rasmingizni yuboring!")
    await PersonalDanny.next()



@dp.message_handler(content_types=ContentType.ANY,state=PersonalDanny.rasm)
async def answer_img(message: types.Message, state: FSMContext):
    if message.content_type == ContentType.PHOTO:
        photo = message.photo[-1]
        file_id = photo.file_id
        file_info = await bot.get_file(file_id)
        file_path = file_info.file_path

    # Rasmni faylga yuklash
        await bot.download_file(file_path, f"C:/Users/User/Desktop/cv_bot/handlers/files/img/{message.from_user.id}.jpg")
        #await message.photo[-1].download()
        await message.answer("Telefon nomer yuboring!",reply_markup=phonkey)
        await PersonalDanny.next()
    else:
        await message.answer("rasm yuboring!")



@dp.message_handler(state=PersonalDanny.Tel,content_types=types.ContentTypes.CONTACT)
async def answer_city(message: types.Message, state: FSMContext):
    tel = message.contact.phone_number

    await state.update_data(
        {"tel": tel}
    )

    await message.answer("Telegram username kiriting!",reply_markup=ReplyKeyboardRemove())

    
    await PersonalDanny.next()




@dp.message_handler(state=PersonalDanny.telegram_username)
async def answer_city(message: types.Message, state: FSMContext):

    username = message.text[:20]

    await state.update_data(
            {"username": username}
        )
    

    await message.answer(f"Email manzilingizni kiriting!")
    await PersonalDanny.next()



@dp.message_handler(state=PersonalDanny.email)
async def answer_city(message: types.Message, state: FSMContext):

    email = message.text[:20]

    await state.update_data(
            {"email": email}
        )
    

    await message.answer(f"Addres kiriting!")
    await PersonalDanny.next()



@dp.message_handler(state=PersonalDanny.addres)
async def answer_city(message: types.Message, state: FSMContext):

    addres = message.text[:20]

    await state.update_data(
            {"addres": addres}
        )
    
    data = await state.get_data()
    name = data.get("name")
    job = data.get("job")
    tel = data.get("tel")
    telegram_username = data.get("username")
    email = data.get("email")
    addres = data.get("addres")

    msg = "Quyidai ma`lumotlar qabul qilindi:\n"
    msg += f"ISM - {name}\n"
    msg += f"Kasb - {job}\n"
    msg += f"Tel - {tel}\n"
    msg += f"Username - {telegram_username}\n"
    msg += f"Email - {email}\n"
    msg += f"Manzil - {addres}\n"

    user_id = message.from_user.id

    await message.answer(msg)


    #malumotlar = [name,job,tel,telegram_username,email,addres]

    if userperinfo(str(message.from_user.id)) != "null":
        edit_userinfo(str(user_id),name,job,tel,telegram_username,email,addres)
    else:
        userpersonalinfo(user_id,name,job,tel,telegram_username,email,addres)

    img = f"C:/Users/User/Desktop/cv_bot/handlers/files/img/{message.from_user.id}.jpg"
    file = f"C:/Users/User/Desktop/cv_bot/handlers/files/file/{message.from_user.id}.pdf"
    
    
    #create_image_with_greeting(file,img,malumotlar)
    malumotlar = userperinfo(str(user_id))

    #create_image_with_greeting(file,img,malumotlar)

    await state.finish()

    await message.answer(malumotlar,reply_markup=shablon_key)






@dp.message_handler(text="cv view")
async def cv_view(message: types.Message):

    user_id = message.from_user.id
    malumotlar = userperinfo(str(user_id))

    print(malumotlar['name'].split())

    #img = f"C:/Users/User/Desktop/cv_bot/handlers/files/img/shablon1.jpg"
    img = f"C:/Users/User/Desktop/cv_bot/handlers/files/img/{message.from_user.id}.jpg"
    file = f"C:/Users/User/Desktop/cv_bot/handlers/files/file/{message.from_user.id}.pdf"

    create_image_with_greeting(file,img,malumotlar)

    files = f"C:/Users/User/Desktop/cv_bot/handlers/files/file/{message.from_user.id}.pdf"
    with open(files, "rb") as file:
        # Document jo'natish
        await bot.send_document(chat_id=message.from_user.id, document=file)
    

    #await message.answer(malumotlar)



@dp.message_handler(text="edit img")
async def adminpanel(message: types.Message):

    
    await message.answer("Shaxsiy rasmingizni kiriting!")
    await Edit_img.rasm.set()


@dp.message_handler(content_types=ContentType.ANY,state=Edit_img.rasm)
async def answer_img(message: types.Message, state: FSMContext):
    if message.content_type == ContentType.PHOTO:
        photo = message.photo[-1]
        file_id = photo.file_id
        file_info = await bot.get_file(file_id)
        file_path = file_info.file_path

    # Rasmni faylga yuklash
        await bot.download_file(file_path, f"C:/Users/User/Desktop/cv_bot/handlers/files/img/{message.from_user.id}.jpg")
        #await message.photo[-1].download()
        await message.answer("Rasm o'zgartirildi")
        await state.finish()
        
    else:
        await message.answer("rasm yuboring")


@dp.message_handler(text="add education")
async def adminpanel(message: types.Message):

    
    await message.answer('my accaunt',reply_markup=accaunt_cv)