#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount= 0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.purchases = []
        
    def add_item(self, title, price, quantity = 1):
        self.total += price * quantity
        self.items += [title] * quantity
        self.purchases.append(price*quantity)
        
    def apply_discount(self):
        if(self.discount == 0):
            print("There is no discount to apply.")
        else:
            self.total -= (self.discount / 100) * self.total
            print(f"After the discount, the total comes to ${int(self.total)}.")
            
    def void_last_transaction(self):
        self.total -= self.purchases.pop()
