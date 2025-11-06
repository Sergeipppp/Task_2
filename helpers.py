import random
import string
from dataclasses import dataclass

@dataclass
class MakeTestData:
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
