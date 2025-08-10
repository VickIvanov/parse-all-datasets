from dataclasses import dataclass
from datetime import datetime
from abc import ABC, abstractmethod

# Domain Layer
@dataclass
class User:
    name: str

@dataclass
class Greeting:
    message: str
    timestamp: datetime

# Application Layer
class GreetingService:
    def __init__(self, greeting_repository):
        self.greeting_repository = greeting_repository

    def create_greeting(self, user: User) -> Greeting:
        current_time = datetime.now()
        message = f'Hi, {user.name}!'
        greeting = Greeting(message=message, timestamp=current_time)
        return self.greeting_repository.save(greeting)

# Infrastructure Layer
class GreetingRepository(ABC):
    @abstractmethod
    def save(self, greeting: Greeting) -> Greeting:
        pass

class ConsoleGreetingRepository(GreetingRepository):
    def save(self, greeting: Greeting) -> Greeting:
        formatted_time = greeting.timestamp.strftime('%H:%M')
        print(greeting.message)
        print(f'Сейчас {formatted_time}. Отличное время, чтобы написать немного кода!')
        return greeting

# Presentation Layer
def main():
    repository = ConsoleGreetingRepository()
    service = GreetingService(repository)
    user = User(name='PyCharm')
    service.create_greeting(user)

if __name__ == '__main__':
    main()