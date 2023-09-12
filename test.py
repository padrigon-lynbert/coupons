from Percentage.main import Percentage

price = 200
voucher = 10

def discounted_price(voucher, price):
    global discount
    
    discount = Percentage.value_of_percentage(voucher, price)
    
    return price - discount

print(discounted_price(voucher, price))