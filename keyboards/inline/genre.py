from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from utils.models import Category


class GenreCallbackData(CallbackData, prefix='genre'):
    category_id: int = None


async def genre_list_ikb() -> InlineKeyboardMarkup:
    categories = await Category.all()
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=category.name,
                    callback_data=GenreCallbackData(
                        category_id=category.id
                    ).pack()
                )
            ]
            for category in categories
        ]
    )
