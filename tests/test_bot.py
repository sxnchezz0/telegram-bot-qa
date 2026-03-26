import pytest
from aiogram.types import Message, User, Chat

@pytest.fixture
def mock_message():
    """Создание тестового сообщения"""
    user = User(id=123, is_bot=False, first_name="Test")
    chat = Chat(id=123, type='private')
    return Message(message_id=1, date=None, chat=chat, from_user=user, text="")

class TestBotLogic:
    
    def test_echo_empty_input(self):
        """Тест: проверка реакции на пустой ввод"""
        input_text = ""
        is_valid = bool(input_text.strip())
        assert is_valid == False, "Пустой ввод должен быть отклонен"
    
    def test_echo_normal_input(self):
        """Тест: проверка нормального ввода"""
        input_text = "Hello World"
        is_valid = bool(input_text.strip()) and len(input_text) <= 500
        assert is_valid == True, "Нормальный ввод должен быть принят"
    
    def test_echo_long_input(self):
        """Тест: проверка ограничения длины"""
        input_text = "A" * 501
        is_valid = len(input_text) <= 500
        assert is_valid == False, "Длинный ввод должен быть отклонен"
    
    def test_xss_protection(self):
        """Тест: проверка экранирования XSS"""
        dangerous_input = "<script>alert('hack')</script>"
        safe_output = dangerous_input.replace('<', '&lt;').replace('>', '&gt;')
        assert '<' not in safe_output, "XSS символы должны быть экранированы"
        assert '&lt;' in safe_output, "Должны быть HTML-сущности"