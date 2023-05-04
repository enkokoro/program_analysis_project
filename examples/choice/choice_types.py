import random
from typing import List

def choice(items: List[str]) -> str:
    """Get a random element from the given list.
    """
    return random.choice(items)
