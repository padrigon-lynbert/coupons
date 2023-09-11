from Percentage.main import Percentage
import os
def cls(): os.system('cls')

products = {"Cappucino": 100, "Choco": 60, "Black Forest": 70}

order = [70, 60, 60, 100, 100]
price = sum(order)

# print(products["Cappucino"])
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

def get_price(): #example only (edit this next)
    price = [50,50,50,50,50]
    return(sum(price))
           
voucher = lambda: input("voucher: ")

def discounted_price(voucher, price):
    global discount
    
    discount = Percentage.value_of_percentage(voucher, price)
    
    return get_price() - discount

def run(): pass
    

run()

