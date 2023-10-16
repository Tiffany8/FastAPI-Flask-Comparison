from marshmallow import ValidationError
from flask import Flask, request, jsonify

from common.exceptions import InsufficientStockException
from common.types import FoodType, FoodSize, SpecialRequest
from common.utils import process_order
from flask_example.models import Order

app = Flask(__name__)


@app.route("/place_order", methods=["POST"])
def place_order():
    order_schema = Order()

    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 422
    except Exception as e:
        return jsonify({"message": "An unknown error occurred: " + str(e)}), 500

    try:
        receipt = process_order(order_data)
    except InsufficientStockException as e:
        return jsonify({"message": str(e)}), 400
    except Exception as e:
        return (
            jsonify(
                {"message": "An unknown error occurred during processing: " + str(e)}
            ),
            500,
        )

    return jsonify({"message": "Order successfully placed", "receipt": receipt}), 200
