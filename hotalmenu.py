#define the menu of resaurant
menu = {
    #BIRYANIS
    'Chicken Biryani':210,
    'Mutton Biryani':253,
    'Chicken Family Pack':552,
    'Mutton Family Pack':576,
    'Special Mutton Biryani':337,
    'Special Chicken Biryani' :819,
    'Veg Biryani' :154,
    'Egg Biryani' :154,
    'Veg.Family Pack' :383,
    'Veg.Supreme Pack' :574,
    #STARTERS
    'Chilli Chicken' :264,
    'Chicken 65' :264,
    'Pepper Chiicken' :196,
    'Veg.Macnchurain' :189,
    #KEBABS
    'Chicken Tikka Kebab' :243,
    'Tandoori Chicken [Half]' :243,
    'Tandoori Chicken [Full]' :379,
    'Chicken Reshmi Kebab' :243,
    #CURRIES
    'Butter Chicken Boneless' :246,
    'Nizami Pakistani' :171,
    #BREADS
    'Tandoori Roti' :40,
    'Rumali Roti' :40,
    #DRINKS
    'Kashmri Tea' :200,
    'Cofee' :100,

}

#greet
    print("Welcome to SAJIDA Restaurant")
    print("Chicken Biryani: Rs210\nMutton Biryani: Rs253")
    print("Chicken Family Pack: Rs552\nMutton Family Pack:Rs576\nSpecial Mutton Biryani:Rs337")
    print("Specail Chicken Biryani:Rs819\nVeg Biryani: Rs154\nEgg Biryani :Rs154\nVeg.Famliy Pack:Rs383\nVeg.Supreme Pack :Rs574")
    print("Chilli Chicken :264\n"Chicken 65 :Rs264\nPapper Chicken :196\nVeg.macnchurain :Rs189\nChicken Tikkka Kabab : Rs243\nTandoori Tika [Half] :243\n\nTandoori Chicken [Full]: Rs379")
    print("Chicken Reshmi Kebab: Rs243\nButter Chicken Boneless: Rs246\nNizamli Pakistani: Rs171\n\nTandoori Roti: Rs40\nRumali Roti:Rs40\nKashmirTea: Rs200\nCoffe: Rs100")

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
        
