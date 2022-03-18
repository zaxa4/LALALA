from main import dp
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from aiogram.dispatcher.filters import Command, Text

@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer("Выбери шмот из меню ниже пес",
                         reply_markup=menu)
@dp.message_handler(Text(equals=["Николаевская оперативка","Захаровская видюха","Барановский камень"
                                 ]))
async def get_iron(message: Message):
    await  message.answer(f"Ты выбираешь{message.text}.изи заскамили мамонта"
                          ,reply_markup=ReplyKeyboardRemove())


