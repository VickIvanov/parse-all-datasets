import os


def create_project_structure():
    # Создаем структуру директорий
    directories = [
        'src/domain',
        'src/application',
        'src/infrastructure',
        'src/presentation',
        'tests/unit',
        'tests/integration'
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        with open(os.path.join(directory, '__init__.py'), 'w') as f:
            pass

    # Словарь с содержимым файлов
    files = {
        'src/domain/models.py': '''from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    name: str

@dataclass
class Greeting:
    message: str
    timestamp: datetime''',

        'src/domain/repositories.py': '''from abc import ABC, abstractmethod
from .models import Greeting

class GreetingRepository(ABC):
    @abstractmethod
    def save(self, greeting: Greeting) -> Greeting:
        pass''',

        'src/application/services.py': '''from datetime import datetime
from ..domain.models import User, Greeting
from ..domain.repositories import GreetingRepository

class GreetingService:
    def __init__(self, greeting_repository: GreetingRepository):
        self.greeting_repository = greeting_repository

    def create_greeting(self, user: User) -> Greeting:
        current_time = datetime.now()
        message = f'Hi, {user.name}!'
        greeting = Greeting(message=message, timestamp=current_time)
        return self.greeting_repository.save(greeting)''',

        'src/infrastructure/repositories.py': '''from ..domain.repositories import GreetingRepository
from ..domain.models import Greeting

class ConsoleGreetingRepository(GreetingRepository):
    def save(self, greeting: Greeting) -> Greeting:
        formatted_time = greeting.timestamp.strftime('%H:%M')
        print(greeting.message)
        print(f'Сейчас {formatted_time}. Отличное время, чтобы написать немного кода!')
        return greeting''',

        'src/presentation/cli.py': '''from ..domain.models import User
from ..application.services import GreetingService
from ..infrastructure.repositories import ConsoleGreetingRepository

def main():
    repository = ConsoleGreetingRepository()
    service = GreetingService(repository)
    user = User(name='PyCharm')
    service.create_greeting(user)''',

        'main.py': '''from src.presentation.cli import main

if __name__ == '__main__':
    main()''',

        'requirements.txt': ''''''
    }

    # Создаем файлы
    for file_path, content in files.items():
        with open(file_path, 'w') as f:
            f.write(content)


if __name__ == '__main__':
    create_project_structure()
    print("Структура проекта успешно создана!")