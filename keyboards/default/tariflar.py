from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
tariflar_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="๐ ZO'R 2"),
            KeyboardButton(text="๐ ZO'R 6"),
            KeyboardButton(text="๐ ZO'R 10")
        ],
        [
            KeyboardButton(text="๐ ZO'R 15"),
            KeyboardButton(text="๐ ALLO"),
            KeyboardButton(text="๐ Kunlik")
        ],
        [
            KeyboardButton(text='โช๏ธ Status Silver NEW'),
            KeyboardButton(text='๐ก Status Gold New')
        ],
        [
            KeyboardButton(text='๐ Status Platinum New'),
            KeyboardButton(text='โ Click +')
        ],
        [
            KeyboardButton(text='๐ Welcome'),
            KeyboardButton(text='๐ Galaba')
        ],
        [
            KeyboardButton(text='๐งธ Bolajon'),
            KeyboardButton(text='๐ Yangi Super hit')
        ],
        [
            KeyboardButton(text='๐  Bosh menu'),
            KeyboardButton(text='<-Orqaga')
        ]
    ],resize_keyboard=True
)
internet_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='๐ Oylik internet-paketlar')
        ],
        [
            KeyboardButton(text='๐ Haftalik\n'
                                'internet-paketlar'),
            KeyboardButton(text='๐ Kunlik\n'
                                'internet-paketlar')
        ],
        [
            KeyboardButton(text='๐ 4G Internet-paketlar'),
            KeyboardButton(text='<- Orqaga')
        ]
    ],resize_keyboard=True
)
boshqa_hizmatlar_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='๐ฐ Asosiy xizmatlar'),
            KeyboardButton(text='๐ Internet hizmatlar')
        ],
        [
            KeyboardButton(text='๐ฉ SMS xizmatlar'),
            KeyboardButton(text='๐ฉ Xalqaro SMS')
        ],
        [
            KeyboardButton(text='๐งพ Maxsus takliflar'),
            KeyboardButton(text='<- Orqaga')
        ]
    ],resize_keyboard=True
)

usel_tarif = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='๐ Cosmo tariflari'),
            KeyboardButton(text='๐ฒ Special tariflari')
        ],
        [
            KeyboardButton(text='โ Special+ tariflari'),
            KeyboardButton(text='๐ญ Kayfiyat tariflari')
        ],
        [
            KeyboardButton(text='๐ Tantana tariflari'),
            KeyboardButton(text='๐จ Marhamat tarifi')
        ],
        [
            KeyboardButton(text='๐ Yengil hafta'),
            KeyboardButton(text='๐ Student')
        ],
        [
            KeyboardButton(text='๐ผ๏ธ Oddiy'),
            KeyboardButton(text='โ๏ธ Uchar internet')
        ],
        [
            KeyboardButton(text='<<Orqaga')
        ]
    ]
)
