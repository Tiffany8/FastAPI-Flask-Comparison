from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Optional

from common.types import FoodType, FoodSize, SpecialRequest


class FoodItem(BaseModel):
    food_type: FoodType
    food_size: FoodSize
    quantity: int


class Receipt(BaseModel):
    table_number: int
    total_price: float
    food_items: List[FoodItem]
    special_requests: Optional[str]


class Order(BaseModel):
    table_number: int = Field(..., description="Table number for the order")
    food_items: List[FoodItem] = Field(..., description="List of food items ordered")
    special_requests: List[SpecialRequest] = Field(
        ..., description="Any special requests for the order"
    )
