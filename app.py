if __name__ == '__main__':
    from handlers.users import users_router
    from loader import bot, dp
    dp.include_router(router=users_router)
    dp.run_polling(bot)
