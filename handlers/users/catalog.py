from aiogram import F, Router
from aiogram.types import CallbackQuery
from sqlalchemy import select, func

from utils.models import Movie
from keyboards.inline import GenreCallbackData, genre_list_ikb

catalog_router = Router(name='catalog')


@catalog_router.callback_query(GenreCallbackData.filter())
async def get_movie(callback: CallbackQuery, callback_data: GenreCallbackData):
    movie = (await Movie.scalars(
        select(Movie)
        .order_by(func.random())
        .limit(1)
        .filter_by(category_id=callback_data.category_id)
    ))[0]
    await callback.message.answer_photo(
        photo=movie.poster,
        caption=f'''
***{movie.title}***

{movie.descr}

__Kinopoisk:__ ***{movie.kp_rating}***
__IMDB:__ ***{movie.imdb_rating}***

__Дата выхода:__ {movie.release_date.strftime('%d.%m.%Y')}
'''
    )
