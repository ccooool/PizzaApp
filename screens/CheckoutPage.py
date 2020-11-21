import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from pizzapy.customer import Customer
from pizzapy.menu import Menu, MenuItem
from pizzapy.order import Order
from decimal import Decimal


class CheckoutPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Placeholer = tk.Label(self, text="CHECKOUT PAGE")
        Placeholer.pack(side="top")
        self.gotonext=ttk.Button(self,text="Im done with my order",command=lambda:self.controller.show_frame("PayPage"))
        self.gotonext.pack(side="right")
        
        # ordertext has our menu in it
        self.ordertext = tk.Label(self, text="")
        self.ordertext.pack(side = "bottom")
        ThisIsPageText = tk.Label(self, text="This is your cart so far:",font=('Courier New',30))
        ThisIsPageText.pack(side="bottom")
        # get our order from the controller.
        self.Nogobacc = ttk.Button(self, text="Edit Cart",command= lambda: self.controller.show_frame("MenuPage"))
        self.Nogobacc.pack(side="left")

        # totol_price has the total price before tax
        self.totol_price_txt  = tk.Label(self,text = str(self.controller.total_price),font=('Courier New',30))
        self.totol_price_txt.pack(side="top")
        
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
    def next_page_ok(self):
        pass


        
            
   