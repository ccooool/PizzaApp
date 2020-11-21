import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from pizzapy.customer import Customer
from pizzapy.menu import Menu, MenuItem
from pizzapy.order import Order
from PIL import ImageTk, Image


class PayPage(tk.Frame):
    def __init__(self,parent,controller):
        
        tk.Frame.__init__(self,parent)
        cash_image = ImageTk.PhotoImage(Image.open('moolah.jpg').resize((200,250),Image.ANTIALIAS))
        credit_image = ImageTk.PhotoImage(Image.open('credit.png').resize((200,250),Image.ANTIALIAS))
        self.controller = controller
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
        
    def pay_with_credit(self):
        print("paying with credit")
    def pay_with_cash(self):
        print("paying wiht cash")