#Project for Restaurant Menu
Menu = dict(
        Pizza=40, Burger=60, Pasta=50, Vegiatable_soup=120, Tomato_soup=80, Chicken_soup=150, 
        Mix_salad=200, katchumber_salad=70, Papaya_salad=100,
        )

print('\nWelcome to Python Restaurant\n        Food Menu')
print('\nList of items we can serve :------\n')
print(f"Pizza: RS40\nBurger: RS60\nPasta: Rs50Vegiatable soup: Rs120\nTomato soup: RS80\nChicken soup: Rs150\nMix salad: Rs200\nkatchumber salad: Rs70\nPapaya salad: Rs100")



order_total = 0  #Every ordered stored here

item_1 = input("Enter the item you want to order : ")
if item_1 in Menu:
    order_total = Menu[item_1]  #updating order_total with item that customer have ordered
    print(f"your item {item_1} has been added to your order")
else:
    print(f'Ordered item {item_1} is not avaialable yet') #forwated string
#Another order
another_order = input('Do you want to add another item? (Yes/No) :')
if another_order == "Yes":
    item_2 = input("Enter the item you want to order : ")
    if item_2 in Menu:
        order_total += Menu[item_2]  #updating order_total with item that customer have ordered
        print(f"your item {item_2} has been added to your order")
    else:
        print(f'Ordered item {item_2} is not avaialable yet') #forwated string

print(f'Your total Bill is {order_total}')



'''Steps : 
1 - dict
2 - welcome to customer
3 - 1 variable to store orders
4 - condition to check item in menu by membership operator

'''