# Exercise-2: Shopping Cart Program

item = input('What would you like to buy?: ')
price = float(input('What is the price of the item?: '))
quantity = int(input('How many would you like to buy?: '))
total_cost = price * quantity

print(f"you have bought {quantity} {item}(s) for a total of ${total_cost:.2f} only)")


