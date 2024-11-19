from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Покупка валюты')],
                                     [KeyboardButton(text='Продажа валюты')],
                                     [KeyboardButton(text='Тарифы на покупку|продажу валюты')]],
                           input_field_placeholder='Выберите пункт меню...',
                           resize_keyboard=True)

pay_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Беларусский рубль --> Российский рубль')],
                                         [KeyboardButton(text='Беларусский рубль --> Евро')],
                                         [KeyboardButton(text='Беларусский рубль --> Американский доллар')],
                                         [KeyboardButton(text='Назад в меню')]],
                               resize_keyboard=True)

sell_menu = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Российский рубль --> Беларусский рубль')],
                                     [KeyboardButton(text='Евро --> Беларусский рубль')],
                                     [KeyboardButton(text='Американский доллар --> Беларусский рубль')],
                                     [KeyboardButton(text='Назад в меню')]],
                           resize_keyboard=True)

back = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Назад')]],
                           resize_keyboard=True)