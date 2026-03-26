import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import os
from bot.handlers import router

load_dotenv()

logging.basicConfig(level=logging.INFO)

async def main():
    token = os.getenv('BOT_TOKEN')
    
    if not token:
        logging.error("❌ BOT_TOKEN не найден в переменных окружения!")
        return
    
    bot = Bot(token=token)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)
    
    logging.info("✅ Бот запущен...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())