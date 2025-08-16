from datetime import datetime
from ..domain.models import User, Greeting
from ..domain.repositories import GreetingRepository

class GreetingService:
    def __init__(self, greeting_repository: GreetingRepository):
        self.greeting_repository = greeting_repository

    def create_greeting(self, user: User) -> Greeting:
        current_time = datetime.now()
        message = f'Hi, {user.name}!'
        greeting = Greeting(message=message, timestamp=current_time)
        return self.greeting_repository.save(greeting)