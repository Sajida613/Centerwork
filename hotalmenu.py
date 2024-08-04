#define the menu of resaurant
menu = {
    'pizza':40,
    'burger':150,
    'salad':80,
    'cofee':100,
    'pasta':90,
}

#greet
print("Welcome to SAJIDA Restaurant")
print("pizza: Rs40\nburger: Rs150\nsalad: Rs80\ncofee: Rs100\npasta: Rs90")

order_total = 0


item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not avaialable yet!")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]  
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not avaialable!")


print(f"The total amount of items is {order_total}")
        
