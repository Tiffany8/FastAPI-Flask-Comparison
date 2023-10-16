from fastapi import FastAPI, HTTPException
from fastapi_example.models import Order, Receipt

from common.exceptions import InsufficientStockException
from common.utils import process_order

app = FastAPI(
    title="Restaurant Orders API",
    description="Place orders for a restaurant",
    version="0.1.0",
)


@app.post("/order", response_model=Receipt)
async def place_order(order: Order):
    try:
        receipt = process_order(order.model_dump())
        return {"message": "Order successfully placed", "receipt": receipt}
    except InsufficientStockException as e:
        raise HTTPException(status_code=400, detail=str(e))
