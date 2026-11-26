def calculator(price,tax,discount):
    total_price = price + (price * tax) - (price * discount)
    return total_price

print(calculator(price=100, tax=0.1, discount=0.05))