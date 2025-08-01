# validation.py

def validate_product_data(name, quantity, price):
    if not name or not isinstance(name, str):
        return False, "Product name is required and must be a string."
    if not isinstance(quantity, int) or quantity < 0:
        return False, "Quantity must be a non-negative integer."
    if not isinstance(price, (int, float)) or price < 0:
        return False, "Price must be a non-negative number."
    return True, ""
