from Percentage.main import Percentage
import os
def cls(): os.system('cls')

products = {"Cappucino": 100, "Choco": 60, "Black Forest": 70}

def get_order():
    order = list()
    while True:
        while True:
            input("\n<ENTER>"); cls()
            
            print("Products:\n")
            for x, item in enumerate(products): print(f"<{x}> {item}: {products[item]}")
            
            #list all order using spaces ex: 0 0 1 2 - means order is (cappucino 2x, choco 1x, black forest 1x)
            print(f"\nOrder: {order}")
            try: 
                choice = int(input("<0> Enter order \n<1> Delete last index \n<2> Move on\n\n: "))
            except ValueError: print("Enter correct values.")

            if choice == 0: order = input("\nOrder: ").split()
            elif choice == 1: 
                try: order.pop()
                except IndexError: print("No value to delete."); continue
            elif choice == 2: break
            else: continue

        for i in order:
            if i.isdigit(): pass
            else: print("Enter correct values."); continue
            
        break

# Test
order = [0,1,1,2,0]
def getget_price(order):
    individual_price = list()
    
    for element in order:
        if element == 0: individual_price.append(100)
        elif element == 1: individual_price.append(60)
        else: individual_price.append(70)
        
        price = sum(individual_price)

    return price

# print(getget_price(get_order()))
get_order()