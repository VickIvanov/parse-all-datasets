from ..domain.repositories import GreetingRepository
from ..domain.models import Greeting

class ConsoleGreetingRepository(GreetingRepository):
    def save(self, greeting: Greeting) -> Greeting:
        formatted_time = greeting.timestamp.strftime('%H:%M')
        print(greeting.message)
        print(f'Сейчас {formatted_time}. Отличное время, чтобы написать немного кода!')
        return greeting