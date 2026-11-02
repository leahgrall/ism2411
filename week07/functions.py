#the first bug i found was that there was no : on line 72 behind sales i just found it when i. was looking ovwer the code without ai help.
#The apply_discount(price, tier) function calculates the final price of an item after applying a discount. The inputs are the original price and the customer's discount tier. It uses the tier to determine how much of a discount to apply and then returns the new price.
# No ai used



# ---Exercise 1---

#define a function
def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: $${tax2:.2f}")
print(f"tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# ---Exercise 2---

def apply_discount(price, tier):
    if tier == 'gold':
        return price * 0.85
    elif tier == 'silver':
        return price * 0.90
    elif tier == 'bronze':
        return price * 0.95
    else:
        return price  # No discount
    

#calling the function with different tiers
original_price = 200

for tier in ['gold', 'silver', 'bronze', 'none']:
   print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

#---Exercise 3---

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

# Calling the final_price function
print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

#---Exercise 4---

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07  
for price, tier in orders:
    total = final_price(price, 0.07, tier)
    print(f"price: ${price} | Tier: {tier} | total: ${total:.2f}")


# ---Exercise 5---

 #broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total = sale
print(f"Total: ${total}")

count = 0
for sale in sales:     # added : to sales
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):  # remove the = because we need to reach 5 not just 0-4 the < does not include the 5
    print(sales[i])
    i += 1

# ---Exercise 6---

x =100          #global x 

def double_it():
    x = 999     #local x
    return x * 2

print(x)
print(double_it())
print(x)

