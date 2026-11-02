
#inventory.py
#author: Leah Grall
#module: lab 10

#reflection questions
#1 The most surprising thing about Python lists is that you can store multiple values in one variable instead of making a separate variable for each item. I also think it is interesting that you can easily add, remove, or change items in a list
#2 One business situation where a Python list would have saved time is tracking sales and customer orders for a business class. Instead of manually entering and calculating everything in Excel, I could use a Python list to store the sales amounts and calculate the total sales or average automatically. 

#exercise 1

from copy import error


inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print("---exercise 1---")

print((inventory))
print(len(inventory))

#exercise 2
print("---exercise 2---")

print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle])

#exercise 3
print("---exercise 3---")

print(inventory[:3])
print(inventory[:-2])
print(inventory[::2])

#exercise 4
print("---exercise 4---")

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

#exercise 5
print("---exercise 5---")

coords = (40.7128, -74.0060) #NYC 

try:
    coords[0] = 99
except TypeError:
    print(f"eType error caught: {error}")
    print( "Tuples protect coorinates from being changed by accident.")

#exercise 6
print("---exercise 6---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Average sales: {average}")
print(f"Number of sales: {count}")
print(f"best sale: {max(sales)}")
print(f"worst sale: {min(sales)}")

#exercise 7
print("---exercise 7---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))

print(prices)
print(discounted)

#exercise 8
print("---exercise 8---")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(high_sales)
print(f"count: {len(high_sales)}")
print(f"average: {sum(high_sales) / len(high_sales):.2f}")
