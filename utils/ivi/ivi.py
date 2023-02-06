from http import HTTPStatus

from aiohttp import ClientSession


async def get_ivi_movies(genre: int, page: int = 0):
    async with ClientSession(base_url='https://api2.ivi.ru') as session:
        async with session.get(
            url='/mobileapi/catalogue/v7/',
            params={
                'genre': genre,
                'from': page * 100,
                'to': page * 100 + 99,
                'app_version': 870
            }
        ) as response:
            if response.status == HTTPStatus.OK:
                return await response.json()
