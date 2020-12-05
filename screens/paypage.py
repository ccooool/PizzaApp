import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from pizzapy.customer import Customer
from pizzapy.menu import Menu, MenuItem
from pizzapy.order import Order
from pizzapy.store import Store
from PIL import ImageTk, Image

"""
phone: 3468748803
email: cbk1@rice.edu
address: 5151 Edloe Street, Houston, TX, 77005

"""
class PayPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        cash_image = ImageTk.PhotoImage(Image.open('moolah.jpg').resize((350,300),Image.ANTIALIAS))
        credit_image = ImageTk.PhotoImage(Image.open('credit.png').resize((350,300),Image.ANTIALIAS))
        self.controller = controller
        self.close_button = ttk.Button(self, text= "Quit", command=parent.quit)
        self.close_button.pack(pady="5")
        self.placeholder = tk.Label(self,text="Welcome to the pay page! Please select your payment method")
        self.placeholder.pack(side="top")
        self.Credit = ttk.Button(self,text="Credit Card",image = credit_image, command = lambda:self.pay_with_credit())
        self.Credit.image=credit_image
        self.Credit.pack(side="right")
        self.Cash = ttk.Button(self,text="Cash",image = cash_image,  command = lambda:self.pay_with_cash())
        self.Cash.image=cash_image
        self.Cash.pack(side="left")
        self.Back = ttk.Button(self,text="Go Back",command=lambda:controller.show_frame("CheckoutPage"))
        self.Back.pack(side="top")
        self.ryousure = None

    
    def pay_with_cash(self):
        place_command=print("hello")
        # place_command = self.controller.customer.chosen_rst.place_order(self.controller.order, card=False)
        
        # TODO : implement this type of control on the other buttons, so they don't pop up so many times
        if self.ryousure == None:
            self.ryousure = ttk.Button(self,text="Proceed with cash",command=place_command)
            self.ryousure.pack(side="top")
        
        print("¡Call warning!")
        
    def pay_with_credit(self):
        print("paying with credit")
        self.controller.show_frame("CreditCardPage")
