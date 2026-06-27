from fastapi import FastAPI

app = FastAPI()

orders = []

@app.post("/orders")
def create_order(order: dict):
    orders.append(order)
    return {"message": "Order placed", "order": order}

@app.get("/orders")
def get_orders():
    return orders
