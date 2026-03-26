from aiogram import Router, types, F
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Привет! Я тестовый бот для портфолио QA.\n"
        "Доступные команды:\n"
        "/start - Запуск бота\n"
        "/echo <текст> - Повторить текст\n"
        "/info - Информация о боте"
    )

@router.message(Command("echo"))
async def cmd_echo(message: types.Message, command: Command):
    args = command.args
    text = args.strip() if args else ""
    
    if not text:
        await message.answer("⚠️ Пожалуйста, укажите текст после команды.")
        return
    
    if len(text) > 500:
        await message.answer("⚠️ Текст слишком длинный (макс. 500 символов).")
        return
    
    safe_text = text.replace('<', '&lt;').replace('>', '&gt;')
    await message.answer(f"🔁 {safe_text}")

@router.message(Command("info"))
async def cmd_info(message: types.Message):
    await message.answer(
        "🤖 Бот: QA Portfolio Bot\n"
        "📚 Стек: Python, Aiogram, Pytest\n"
        "🛡 Безопасность: Валидация ввода, .env"
    )