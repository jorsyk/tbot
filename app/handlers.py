from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from aiogram import F, Router, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from app.parser import lst

import app.keyboards as kb

router = Router()


# Состояния продажи валюты
class BY_USD(StatesGroup):
    wait_for_amount = State()

class BY_RUB(StatesGroup):
    wait_for_amount = State()

class BY_EUR(StatesGroup):
    wait_for_amount = State()

#Состояния продажи валюты
class USD_BY(StatesGroup):
    wait_for_amount = State()

class RUB_BY(StatesGroup):
    wait_for_amount = State()

class EUR_BY(StatesGroup):
    wait_for_amount = State()


#Старт конвертации покупки валюты

@router.message(F.text == 'Беларусский рубль --> Американский доллар')
async def start_conversion(message: Message, state: FSMContext):
    await message.answer("Введите сумму в белорусских рублях:", reply_markup=kb.back)
    await state.set_state(BY_USD.wait_for_amount)

@router.message(F.text == 'Беларусский рубль --> Российский рубль')
async def start_conversion(message: Message, state: FSMContext):
    await message.answer("Введите сумму в белорусских рублях:", reply_markup=kb.back)
    await state.set_state(BY_RUB.wait_for_amount)

@router.message(F.text == 'Беларусский рубль --> Евро')
async def start_conversion(message: Message, state: FSMContext):
    await message.answer("Введите сумму в белорусских рублях:", reply_markup=kb.back)
    await state.set_state(BY_EUR.wait_for_amount)

#Старт конвертации продажи валюты

@router.message(F.text == 'Американский доллар --> Беларусский рубль')
async def start_conversion(message: Message, state: FSMContext):
    await message.answer("Введите сумму в Американских долларах:", reply_markup=kb.back)
    await state.set_state(USD_BY.wait_for_amount)

@router.message(F.text == 'Российский рубль --> Беларусский рубль')
async def start_conversion(message: Message, state: FSMContext):
    await message.answer("Введите сумму в Российских рублях:", reply_markup=kb.back)
    await state.set_state(RUB_BY.wait_for_amount)

@router.message(F.text == 'Евро --> Беларусский рубль')
async def start_conversion(message: Message, state: FSMContext):
    await message.answer("Введите сумму в Евро:", reply_markup=kb.back)
    await state.set_state(EUR_BY.wait_for_amount)


# Хендлеры для обработки введенного числа в режиме конвертера (Покупка валюты)

@router.message(BY_USD.wait_for_amount, lambda message: message.text.replace('.', '', 1).isdigit())
async def convert_currency_BY_USD(message: Message, state: FSMContext):
    amount_byn = float(message.text)
    amount_usd = amount_byn / float(lst[1])
    await message.answer(f"{amount_byn} BYN = {amount_usd:.2f} USD")

@router.message(BY_RUB.wait_for_amount, lambda message: message.text.replace('.', '', 1).isdigit())
async def comvert_currency_BY_RUB(message: Message, state: FSMContext):
    amount_byn = float(message.text)
    amount_rub = amount_byn * 10 * float(lst[5])
    await message.answer(f"{amount_byn} BYN = {amount_rub:.2f} RUB")

@router.message(BY_EUR.wait_for_amount, lambda message: message.text.replace('.', '', 1).isdigit())
async def comvert_currency_BY_EUR(message: Message, state: FSMContext):
    amount_byn = float(message.text)
    amount_eur = amount_byn / float(lst[3])
    await message.answer(f"{amount_byn} BYN = {amount_eur:.2f} EUR")


# Хендлеры для обработки введенного числа в режиме конвертера (Продажа валюты)

@router.message(USD_BY.wait_for_amount, lambda message: message.text.replace('.', '', 1).isdigit())
async def convert_currency_USD_BY(message: Message, state: FSMContext):
    amount_usd = float(message.text)
    amount_byn = amount_usd * float(lst[0])
    await message.answer(f"{amount_usd} USD = {amount_byn:.2f} BYN")

@router.message(RUB_BY.wait_for_amount, lambda message: message.text.replace('.', '', 1).isdigit())
async def comvert_currency_RUB_BY(message: Message, state: FSMContext):
    amount_rub = float(message.text)
    amount_byn = amount_rub / 10 / float(lst[4])
    await message.answer(f"{amount_rub} RUB = {amount_byn:.2f} BYN")

@router.message(EUR_BY.wait_for_amount, lambda message: message.text.replace('.', '', 1).isdigit())
async def comvert_currency_BY_EUR(message: Message, state: FSMContext):
    amount_eur = float(message.text)
    amount_byn = amount_eur * float(lst[2])
    await message.answer(f"{amount_eur} EUR = {amount_byn:.2f} BYN")


# Очистка состояния
@router.message(F.text == 'Назад')
async def back(message: Message, state: FSMContext) -> None:
    await message.answer("Вы вышли из режима конвертации.", reply_markup=kb.main)
    await state.clear()


# Хендлер для запуска конвертера
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Привет, {html.bold(message.from_user.full_name)}!\nДобро пожаловать в {html.bold('Конвертер валют')}.💸💸💸",
        reply_markup=kb.main)


# Хендлеры первой клавиатуры

@router.message(F.text == 'Покупка валюты')
async def pay_menu(message: Message) -> None:
    await message.answer('Покупка валюты', reply_markup=kb.pay_menu)


@router.message(F.text == 'Продажа валюты')
async def pay_menu(message: Message) -> None:
    await message.answer('Продажа валюты', reply_markup=kb.sell_menu)


@router.message(F.text == 'Тарифы на покупку|продажу валюты')
async def dashboard(message: Message) -> None:
    await message.answer(
        f"Валюта ----- Сдать ----- Купить\n{html.bold('USD')}        ----- {lst[0]} ------ {lst[1]}\n{html.bold('EUR')}        ----- {lst[2]} ------ {lst[3]}\n{html.bold('RUB')}        ----- {lst[4]} ------ {lst[5]}\n")


# Хендлеры покупки валюты
@router.message(F.text == 'Беларусский рубль --> Американский доллар')
async def dashboard(message: Message) -> None:
    await message.answer('Введите число:', reply_markup=kb.back)


@router.message(F.text == 'Беларусский рубль --> Российский рубль')
async def dashboard(message: Message) -> None:
    await message.answer('Введите число:', reply_markup=kb.back)


@router.message(F.text == 'Беларусский рубль --> Евро')
async def dashboard(message: Message) -> None:
    await message.answer('Введите число:', reply_markup=kb.back)


# Хендлеры продажи валюты
@router.message(F.text == 'Американский доллар --> Беларусский рубль')
async def dashboard(message: Message) -> None:
    await message.answer('Введите число:', reply_markup=kb.back)


@router.message(F.text == 'Российский рубль --> Беларусский рубль')
async def dashboard(message: Message) -> None:
    await message.answer('Введите число:', reply_markup=kb.back)


@router.message(F.text == 'Евро --> Беларусский рубль')
async def dashboard(message: Message) -> None:
    await message.answer('Введите число:', reply_markup=kb.back)


@router.message(F.text == 'Назад в меню')
async def pay_menu(message: Message) -> None:
    await message.answer('Назадв меню', reply_markup=kb.main)

