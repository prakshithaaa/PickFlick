import random
from datetime import datetime, timedelta
import math

print("Welcome to IIITKafe Express!")

menu = ["Pizza","Burger","Fries","Pancake","Coffee","Mojito"]
prices = {"Pizza":300, "Burger":250, "Fries":180, "Pancake":200, "Coffee":70, "Mojito":110}

order_id = None
order_items = []
coupon = None
is_first_order = True

def validate_coupon(coupon_code, subtotal, is_weekend, is_first_order):
    coupons = {
        "SAVE10": {"value": 10, "min": 300, "expiry": "31-12-2025", "percent": True},
        "FLAT50": {"value": 50, "min": 200, "expiry": "31-10-2025", "percent": False},
        "FESTIVE15": {"value": 15, "min": 0, "expiry": "30-11-2025", "percent": True, "weekend_only": True},
        "FIRST100": {"value": 100, "min": 0, "expiry": "31-12-2025", "percent": False, "first_order_only": True},
    }

    today = datetime.now().date()

    if coupon_code not in coupons:
        print("Invalid coupon")
        return 0

    rule = coupons[coupon_code]
    expiry = datetime.strptime(rule["expiry"], "%d-%m-%Y").date()

    if today > expiry:
        print("Coupon expired on", expiry.strftime("%d-%m-%Y"))
        return 0

    if subtotal < rule["min"]:
        print("Minimum order value ₹", rule["min"], "required")
        return 0

    if "weekend_only" in rule:
        if rule["weekend_only"] and not is_weekend:
            print("Coupon valid only on weekends")
            return 0

    if "first_order_only" in rule:
        if rule["first_order_only"] and not is_first_order:
            print("Coupon valid only on first order")
            return 0

    if rule["percent"]:
        discount = subtotal * rule["value"] / 100
        print(rule["value"], "% off applied!")
    else:
        discount = rule["value"]
        print("Flat ₹", rule["value"], "off applied!")

    return discount

while True:
    print("\n1. View Menu")
    print("2. Place Order")
    print("3. Apply/Change Coupon")
    print("4. Generate Bill")
    print("5. Exit")

    choice = int(input("Choice: "))

    if choice == 1:
        print("\n--- MENU ---")
        for item in menu:
            print(item, "₹", prices[item])

    elif choice == 2:
        order_items = []
        print("Enter items to add (type 'done' to finish):")
        while True:
            item = input()
            if item == "done":
                break
            elif item in menu:
                order_items.append(item)
            else:
                print("Enter a valid item")

        if order_items:
            order_id = "OD" + str(random.randint(1000, 9999))
            print("Your Order ID:", order_id)
        else:
            print("No items ordered.")

    elif choice == 3:
        coupon = input("Enter coupon code: ")
        print("Coupon applied:", coupon)

    elif choice == 4:
        if not order_items:
            print("No items in order.")
            continue

        subtotal = 0
        for i in order_items:
            subtotal += prices[i]

        print("\n--- BILL ---")
        print("Order ID:", order_id)
        print("Items:", order_items)
        print("Subtotal: ₹", subtotal)

        today = datetime.now()
        is_weekend = today.weekday() >= 5
        weekend_discount = 0
        if is_weekend:
            weekend_discount = subtotal * 0.15
        print("Weekend Discount: -₹", weekend_discount)

        coupon_discount = 0
        if coupon:
            coupon_discount = validate_coupon(coupon, subtotal, is_weekend, is_first_order)
        else:
            print("Coupon: None")

        discounted_total = subtotal - weekend_discount - coupon_discount

        gst = discounted_total * 0.05
        print("GST @ 5%: ₹", gst)

        final_amount = math.ceil(discounted_total + gst)
        print("\nFinal Payable (rounded up): ₹", final_amount)

        ready_time = today + timedelta(minutes=20)
        print("Ready by:", ready_time.strftime("%I:%M %p, %d-%m-%Y"))

        is_first_order = False

    elif choice == 5:
        print("Thank you for visiting IIITKafe Express!")
        break

    else:
        print("Invalid choice")
