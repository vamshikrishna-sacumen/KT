"""Demo python file."""

import requests
from requests import Response

PASSWORD = "password123"
def wish():
    print("Tell me about your wishlist")



wish()

print("Welcome")

def my_func(name: str) -> str:
    return f"Hello {name}, welcome to Sacumen."


print(my_func("Python developer"))


def add(num1: int, num2: int) -> int:
    """Sum of 2 numbers.

    Args:
        num1 (int) Optional: a number.
        num2 (int): another number.

    Returns:
        int: result of int which is sum of num1 and num2.
    """
    return num1 + num2



# print(add("hello", 20))


def fetch(url: str) -> Response:
    """Method to fetch data from an API.

    Args:
        url (str): Actual url required to fetch data from.
    """
    params = {"username": "vinod", "password": PASSWORD}
    return requests.get(url, params=params)


# print(fetch(url="https://api.publicapis.org/entries"))

print("kajol added a new line")

print("vamshi added new line")



