# Hotel Menu Program

print("Welcome to our hotel!")
print("1. Breakfast Menu")
print("2. Lunch Menu")
print("3. Dinner Menu")
print("4. Beverages Menu")
print("5. Exit")

while True:
  choice = input("Enter your choice: ")

  if choice == "1":
    print("Breakfast Menu:")
    print("1. Eggs Benedict - $10")
    print("2. Pancakes - $8")
    print("3. Omelette - $9")
    breakfast_choice = input("Enter your choice: ")
    if breakfast_choice == "1":
      print("Eggs Benedict - $10")
    elif breakfast_choice == "2":
      print("Pancakes - $8")
    elif breakfast_choice == "3":
      print("Omelette - $9")

  elif choice == "2":
    print("Lunch Menu:")
    print("1. Grilled Chicken - $15")
    print("2. Fish and Chips - $18")
    print("3. Veggie Burger - $12")
    lunch_choice = input("Enter your choice: ")
    if lunch_choice == "1":
      print("Grilled Chicken - $15")
    elif lunch_choice == "2":
      print("Fish and Chips - $18")
    elif lunch_choice == "3":
      print("Veggie Burger - $12")

  elif choice == "3":
    print("Dinner Menu:")
    print("1. Steak - $25")
    print("2. Shrimp Scampi - $22")
    print("3. Vegetarian Lasagna - $20")
    dinner_choice = input("Enter your choice: ")
    if dinner_choice == "1":
      print("Steak - $25")
    elif dinner_choice == "2":
      print("Shrimp Scampi - $22")
    elif dinner_choice == "3":
      print("Vegetarian Lasagna - $20")

  elif choice == "4":
    print("Beverages Menu:")
    print("1. Soda - $3")
    print("2. Juice - $4")
    print("3. Coffee - $2")
    beverage_choice = input("Enter your choice: ")
    if beverage_choice == "1":
      print("Soda - $3")
    elif beverage_choice == "2":
      print("Juice - $4")
    elif beverage_choice == "3":
      print("Coffee - $2")

  elif choice == "5":
    print("Thank you for visiting our hotel!")
    break

  else:
    print("Invalid choice. Please try again.")