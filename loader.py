from aiogram import Bot, Dispatcher


bot = Bot(
    token='TOKEN',
    parse_mode='Markdown'
)
dp = Dispatcher(
    disable_fsm=True,
    name='dp'
)
