from enum import Enum

from pydantic import BaseModel


class FoodType(str, Enum):
    PIZZA = "Pizza"
    BURGER = "Burger"
    SALAD = "Salad"
    PASTA = "Pasta"


class FoodSize(str, Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"


class SpecialRequest(str, Enum):
    ADD_UTENSILS = "add_utensils"
    EXTRA_CONDIMENTS = "extra_condiments"
    ADD_NAPKINS = "add_napkins"
