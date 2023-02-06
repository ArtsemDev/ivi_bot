import asyncio
from datetime import datetime

from sqlalchemy.exc import IntegrityError

from utils.ivi import get_ivi_movies
from utils.models import Movie, Category


async def get_genre_movies(genre: Category):
    page = 0
    while True:
        movies = await get_ivi_movies(genre=genre.id, page=page)
        if movies.get('result'):
            page += 1
            for movie in movies.get('result'):
                movie = Movie(
                    title=movie.get('title'),
                    descr=movie.get('short_description'),
                    kp_rating=float(movie.get('kp_rating')) if movie.get('kp_rating') else None,
                    imdb_rating=float(movie.get('imdb_rating')) if movie.get('imdb_rating') else None,
                    poster=movie.get('posters')[0].get('url'),
                    release_date=datetime.strptime(movie.get('release_date'), '%Y-%m-%d'),
                    category_id=genre.id
                )
                try:
                    await movie.save()
                except IntegrityError:
                    pass
            await asyncio.sleep(3)
        else:
            break


async def main():
    categories = await Category.all()
    tasks = [asyncio.create_task(get_genre_movies(category)) for category in categories]
    for task in tasks:
        await task


if __name__ == '__main__':
    asyncio.run(main())
