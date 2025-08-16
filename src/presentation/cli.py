from ..domain.models import User
from ..application.services import GreetingService
from ..infrastructure.repositories import ConsoleGreetingRepository

def main():
    repository = ConsoleGreetingRepository()
    service = GreetingService(repository)
    user = User(name='PyCharm')
    service.create_greeting(user)