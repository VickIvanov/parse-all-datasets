from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    name: str

@dataclass
class Greeting:
    message: str
    timestamp: datetime