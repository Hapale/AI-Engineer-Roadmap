from application import Application

def get_user_input():
    print("=====Set your shipping type=====")

    shipping_type = input("Set your shipping type (Standard/Express/Free):").strip().lower()

    try:
        weight = float(input("Weight:"))
        distance = float(input("Distance:"))
        order_total = float(input("Total Order:"))
    except ValueError:
        return None, None, None, None, "Error : Most enter true"

    return shipping_type, weight, distance, order_total

if __name__== "__main__":

    app = Application()

    shipping_type, weight, distance, order_total = get_user_input()

    result = app.handle_request(shipping_type, weight, distance, order_total)

    print(result)
