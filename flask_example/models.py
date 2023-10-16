from marshmallow import Schema, fields, validate

from common.types import FoodType, FoodSize, SpecialRequest


class FoodItem(Schema):
    food_type = fields.Str(
        validate=validate.OneOf([e.value for e in FoodType]), required=True
    )
    food_size = fields.Str(
        validate=validate.OneOf([e.value for e in FoodSize]), required=True
    )
    quantity = fields.Int(required=True)


class Recepit(Schema):
    table_number: fields.Int(required=True, description="Table number for the order")
    total_price: fields.Float(
        validate=validate.Range(min=0),
        required=True,
        description="Total price of the order",
    )
    food_items: fields.List(
        fields.Nested(FoodItem),
        required=True,
        description="List of food items ordered",
    )
    special_requests: fields.List(
        fields.Nested(SpecialRequest), description="Any special requests for the order"
    )


class Order(Schema):
    table_number = fields.Int(required=True, description="Table number for the order")
    food_items = fields.List(
        fields.Nested(FoodItem),
        required=True,
        description="List of food items ordered",
    )
    special_requests = fields.Str(description="Any special requests for the order")
