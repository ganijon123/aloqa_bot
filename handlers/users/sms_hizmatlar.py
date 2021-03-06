from aiogram import types
from keyboards.default.qoshimcha_hizmat import *

from loader import dp


@dp.message_handler(text='๐ฉ SMS xizmatlar')
async def bot_help(message: types.Message):
    await message.answer(text='๐ฉ SMS xizmatlar',reply_markup=sms_button)
@dp.message_handler(text='๐จ 20 SMS paketi')
async def bot_help(message: types.Message):
    await message.answer(text="""๐จ 20 SMS paketi

500 so'm/kun
Ulanish narxi 0 so'm
Ulanish uchun hisobdagi minimal mablagโ miqdori 600 so'm
Ulanish kodi: *110*161#

๐ @aloqa_operatorlar_bot""")
@dp.message_handler(text='๐จ 50 SMS paketi')
async def bot_help(message: types.Message):
    await message.answer(text="""๐จ 50 SMS paketi

1 000 so'm/kun
Ulanish narxi 0 so'm
Ulanish uchun hisobdagi minimal mablag' miqdori 1 100 so'm
Ulanish kodi: *110*162#

๐ @aloqa_operatorlar_bot""")
@dp.message_handler(text='๐จ SMS non-stop')
async def bot_help(message: types.Message):
    await message.answer(text="""๐จ SMS non-stop

ยซSMS non-stopยป xizmati bilan siz kuniga 250 ta mahalliy SMS olasiz. 
1 300 so'm/kun
Ulanish kodi: *110*151#

๐ @aloqa_operatorlar_bot""")
@dp.message_handler(text='๐จ 100 SMS paketi')
async def bot_help(message: types.Message):
    await message.answer(text="""๐จ 100 SMS paketi 
Yanada koโproq SMS muloqot!
5 262.5 so'm/30 kunga
Ulanish kodi: *110*044#
๐ @aloqa_operatorlar_bot""")
@dp.message_handler(text='๐จ 500 SMS paketi')
async def bot_help(message: types.Message):
    await message.answer(text="""๐จ 500 SMS paketi

Yanada koโproq SMS muloqot!
13 682.5 so'm/30 kunga
Ulanish kodi: *110*045#

๐ @aloqa_operatorlar_bot""")
@dp.message_handler(text='๐จ 1000 SMS paketi')
async def bot_help(message: types.Message):
    await message.answer(text="""๐จ 1000 SMS paketi 

Yanada koโproq SMS muloqot!
22 102.5 so'm/30 kunga
Ulanish kodi: *110*046#

๐ @aloqa_operatorlar_bot""")
@dp.message_handler(text='๐ธ SMS Flash')
async def bot_help(message: types.Message):
    await message.answer(text="""๐ธ SMS Flash

ยซSMS Flashยป xizmati bilan saqlanmaydigan SMSlarni toโgโri suhbatdoshing ekraniga yuborishing mumkin!
SMS narxi tarif rejaga binoan

๐ @aloqa_operatorlar_bot""")
@dp.message_handler(text='๐ฐ SMS Jadval')
async def bot_help(message: types.Message):
    await message.answer(text="""๐ฐ SMS Jadval

ยซSMS-jadvalยป xizmati sen uchun muhim boโlgan xabarlarni esdan chiqarmasliginga yordam beradi va avvaldan yetkazish vaqtini belgilaydi!
Vaqtni belgila, matnni yoz, va xabar manzilga kerakli vaqtda yetib boradi!

๐ @aloqa_operatorlar_bot""")