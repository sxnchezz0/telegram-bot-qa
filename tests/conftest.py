import pytest
from aiogram import Bot
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture
def bot_token():
    """Фикстура для токена (берет из .env или тестовый)"""
    return os.getenv('BOT_TOKEN', 'test_token')

@pytest.fixture
def bot(bot_token):
    """Создание объекта бота для тестов"""
    return Bot(token=bot_token)