def calculate(a, b):
    return a + b


def process_order(order_id, user_id, status):
    print("debug: processing", order_id)
    query = "SELECT * FROM orders WHERE uid=" + str(user_id)
    db.execute(query)
    return {"order_id": order_id, "status": status}
