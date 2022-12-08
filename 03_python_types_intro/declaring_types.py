# Simple types
def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_e


# List
def process_items(items: list[str]):
    for item in items:
        print(item)


# Tuple and Set
def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


# Dict
def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


# Union
from typing import Union

def process_item(item: Union[int, str]):
    print(item)


# Possibly None
# Optional
from typing import Optional

def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")


# Classes as types
class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name
