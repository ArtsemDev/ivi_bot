from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from keyboards.inline import GenreCallbackData, genre_list_ikb

start_router = Router(name='start')


@start_router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        text='HELLO',
        reply_markup=await genre_list_ikb()
    )
