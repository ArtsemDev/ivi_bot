from aiogram import Router

from .start import start_router
from .catalog import catalog_router

users_router = Router(name='users')
users_router.include_router(router=start_router)
users_router.include_router(router=catalog_router)

__all__ = ['users_router']
