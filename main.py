import os
def cls(): os.system('cls')

products = {"Cappucino": 100, "Choco": 60, "Black Forest": 70}

order = [70, 60, 60, 100, 100]
price = sum(order)

def get_order():
    order = list()
    while True:
        input("\n<ENTER CORRECT VALUES>"); cls()
        
        print("Products:\n")
        for x, item in enumerate(products): print(f"<{x}> {item}: {products[item]}")
        
        #list all order using spaces ex: 0 0 1 2 - means order is (cappucino 2x, choco 1x, black forest 1x)
        print(f"\nOrder: {order}")
        try: 
            choice = int(input("\n<0> Enter order \n<1> Delete last index \n<2> Move on\n\n: "))
        except ValueError: print("Enter correct values.")

        if choice in range(0,3):
            if choice == 0: 
                order = input("\nOrder: ").split()
            elif choice == 1: 
                try: order.pop()
                except IndexError: print("No value to delete."); continue
            elif choice == 2: break
        else: continue

    for i in order:
        if i.isdigit() and i in range(0,3): break
        else: continue
    
    
        
        
# def get_voucher():
#     voucher = input("Voucher: ")
#     return voucher

def run():
    get_order()
    
run()

