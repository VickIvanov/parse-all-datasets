from abc import ABC, abstractmethod
from .models import Greeting

class GreetingRepository(ABC):
    @abstractmethod
    def save(self, greeting: Greeting) -> Greeting:
        pass