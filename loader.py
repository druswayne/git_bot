from aiogram import Bot, Dispatcher, Router
from config.token import TOKEN

router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(TOKEN)
