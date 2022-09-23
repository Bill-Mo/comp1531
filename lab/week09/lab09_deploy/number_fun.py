from typing import List, Union
from collections.abc import Iterable

def multiply_by_two(number: int) -> int:
    return number * 2

def print_message(message: str) -> None:
    print(message)

def sum_list_of_numbers(numbers: list) -> int:
    return sum(numbers)

def sum_iterable_of_numbers(numbers: Iterable) -> int:
    return sum(numbers)

def is_in(needle: Union[str, int], haystack: List[Union[str, int]]) -> bool:
    return needle in haystack

def index_of_number(item: int, numbers: List[int]) -> Union[int, None]:
    for idx, num in enumerate(numbers):
        if item == num:
            return idx
    return None
