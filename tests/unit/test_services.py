import unittest
from datetime import datetime
from src.domain.models import User, Greeting
from src.domain.repositories import GreetingRepository
from src.application.services import GreetingService

class MockGreetingRepository(GreetingRepository):
    def save(self, greeting: Greeting) -> Greeting:
        return greeting

class TestGreetingService(unittest.TestCase):
    def setUp(self):
        self.repository = MockGreetingRepository()
        self.service = GreetingService(self.repository)

    def test_create_greeting(self):
        user = User(name="Test User")
        message = "Hello, World!"
        greeting = self.service.create_greeting(user)

        self.assertIsInstance(greeting, Greeting)
        # Предположительно, Greeting хранит только сообщение и время создания
        # без прямой ссылки на объект пользователя
        self.assertEqual(greeting.message, f"Hi, {user.name}!")

if __name__ == '__main__':
    unittest.main()