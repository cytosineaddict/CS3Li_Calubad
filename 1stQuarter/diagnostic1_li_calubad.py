print("WELCOME TO THE HYPEKICKS CHECKOUT CENTER!")

def calculate_checkout(cart_total, shipping_speed):

    if shipping_speed == "standard":
        shipping_cost = 10.00
    elif shipping_speed == "express":
        shipping_cost = 15.00
    elif shipping_speed == "standard" and cart_total >= 100:
        shipping_cost = 0.00
    elif shipping_speed == "overnight":
        shipping_cost = 25.00
    else:
        print("Invalid shipping speed. Please choose standard, overnight or express. Shipping cost: 0.00")
        shipping_cost = 0.00

    total_cost = cart_total + shipping_cost 
    return total_cost

print(calculate_checkout(float(input("enter cart total: ")), input("enter shipping speed: ")))

