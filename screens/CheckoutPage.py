import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from pizzapy.customer import Customer
from pizzapy.menu import Menu, MenuItem
from pizzapy.order import Order
from decimal import Decimal
from pizzapy.coupon import *


class CheckoutPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Placeholer = tk.Label(self, text="CHECKOUT PAGE")
        Placeholer.pack(side="top")
        self.gotonext=ttk.Button(self,text="Im done with my order and i am ready to pay",command=lambda:self.controller.show_frame("PayPage"))
        self.gotonext.pack(side="right")
        
        # ordertext has our menu in it
        self.ordertext = tk.Label(self, text="")
        self.ordertext.pack(side = "bottom")
        ThisIsPageText = tk.Label(self, text="This is your cart so far:",font=('Impact',30))
        ThisIsPageText.pack(side="bottom")
        # get our order from the controller.
        self.Nogobacc = ttk.Button(self, text="Edit Cart",command= lambda: self.controller.show_frame("MenuPage"))
        self.Nogobacc.pack(side="left")

        # totol_price has the total price before tax
        self.totol_price_txt  = tk.Label(self,text = str(self.controller.total_price),font=('Impact',50))
        self.totol_price_txt.pack(side="top")
        
        self.coupon_e = tk.Entry(self, textvariable = tk.StringVar(),cursor='mouse', width = 40)
        self.coupon_e.insert(0, "Enter any coupon codes here")
        self.coupon_e.pack()
        self.coupon_e.place(x= 0, y = 40)
        self.coupon_button = ttk.Button(self, text = "Validate and apply coupon", command=lambda:self.add_coupon())
        self.coupon_button.pack()
        self.coupon_button.place(x= 0, y =75)


        
    def display_order(self):
        self.totol_price_txt["text"] = str(self.controller.total_price)

        the_order = self.controller.order
        # the_order.data["Products"] = [{Name: item1, Price: 3}, {Name: item2, Price: 4}, {Name: item3, Price: 5}]
        item_string = ""
        
        for item in the_order.data["Products"]:
            # item = {Name: cheese pizza, Price: 30},
            item_string += item["Name"] + " $" + item["Price"] + "\n"
        print(item_string)
        # change the text in the ordertext button
        self.ordertext["text"] = item_string
        self.totol_price_txt['text'] ="price before tax = $" + str(round(Decimal(self.controller.total_price), 2))
        self.totol_price_txt['text'] += "\n Estimated Tax = $" + str(round(Decimal(0.0825 * self.controller.total_price),2))
    
    # class Coupon(object):
    # """Loose representation of a coupon - no logic. 

    # This is a coupon - you can add it to an Order (order.add_item) and,
    # if it fits, get some money off your purchase. I think. 

    # This is another thing that's worth exploring - there are some sweet 
    # coupons that would be awful without the coupon. 
    # """
    # def __init__(self, code, quantity=1):
    #     self.code = code
    #     self.quantity = quantity
    #     self.id = 1
    #     self.is_new = True
    def add_coupon(self):
        code = self.coupon_e.get()
        self.controller.order.add_item(Coupon(code))

    def next_page_ok(self):
        pass


        
            
   