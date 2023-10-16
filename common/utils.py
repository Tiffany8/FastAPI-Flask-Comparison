from common.exceptions import InsufficientStockException

PRICE_LIST = {
    "Pizza": {"Small": 10.00, "Medium": 15.00, "Large": 20.00},
    "Burger": {"Small": 5.00, "Medium": 7.50, "Large": 10.00},
    "Salad": {"Small": 4.00, "Medium": 6.00, "Large": 8.00},
    "Pasta": {"Small": 8.00, "Medium": 12.00, "Large": 16.00},
}

ORDERS = {
    "0001": {
        "Table Number": 1,
        "Food Items": [{"Type": "Pizza", "Size": "Large", "Quantity": 2}],
        "Special Requests": "Extra cheese",
    },
    "0002": {
        "Table Number": 2,
        "Food Items": [{"Type": "Burger", "Size": "Medium", "Quantity": 1}],
        "Special Requests": "No onions",
    },
    "0003": {
        "Table Number": 3,
        "Food Items": [{"Type": "Salad", "Size": "Small", "Quantity": 1}],
    },
}

stock = {
    "Pizza": {"Small": 10, "Medium": 8, "Large": 5},
    "Burger": {"Small": 10, "Medium": 8, "Large": 5},
    "Pasta": {"Small": 10, "Medium": 8, "Large": 5},
}


def process_order(order_data):
    """
    Process the food order and calculate the total price.

    Args:
    - order_data (dict): The validated order data.

    Returns:
    - dict: A "receipt" containing the processed information.
    """
    total_price = 0.0
    processed_items = []

    for item in order_data["food_items"]:
        food_type = item["food_type"]
        food_size = item["food_size"]
        quantity = item["quantity"]

        # Stock check
        if stock.get(food_type, {}).get(food_size, 0) < quantity:
            raise InsufficientStockException(
                f"Insufficient stock for {quantity} x {food_size} {food_type}"
            )

        # Deduct the stock
        stock[food_type][food_size] -= quantity

        # Calculate price
        item_price = PRICE_LIST[food_type][food_size]
        total_item_price = item_price * quantity
        total_price += total_item_price

        processed_item = {
            "food_type": food_type,
            "food_size": food_size,
            "quantity": quantity,
            "total_item_price": total_item_price,
        }
        processed_items.append(processed_item)

    receipt = {
        "table_number": order_data["table_number"],
        "total_price": total_price,
        "processed_items": processed_items,
        "special_requests": order_data.get("special_requests", ""),
    }

    return receipt


def get_order(order_id):
    """
    Get the order information for a given order ID.

    Args:
    - order_id (str): The order ID to retrieve.

    Returns:
    - dict: The order information.
    """
    return ORDERS.get(order_id, None)


def get_orders():
    """
    Get all the orders.

    Returns:
    - list: A list of all the orders.
    """
    return ORDERS.values()
