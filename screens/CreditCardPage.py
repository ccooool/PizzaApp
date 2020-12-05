from pizzapy.customer import Customer
import tkinter as tk
from tkinter import font as tkfont # python 3
from tkinter import ttk
from pizzapy.payment import CreditCard


# Class representing our start page!
class CreditCardPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.error_label = None
        self.place_card_order = None
        # START MAKING YOUR LABELS, BUTTONS, ETC. FOR THE WELCOME PAGE HERE
        label = tk.Label(self, text="This is the Credit Card page", font = ('Impact',30) )
        label.pack(side="top", fill="x", pady=50)
        self.close_button = ttk.Button(self, text= "Quit", command=parent.quit,cursor='mouse')
        self.close_button.pack(pady="5")
        self.get_info()

        self.save_info_button = ttk.Button(self, text = "Finalize Card Info", command = lambda:self.save_info())
        self.save_info_button.pack()

    def get_info(self): 
        self.banana = tk.Label(self, text="Please enter your Credit Card information", font = ('MS Gothic',20))
        self.banana.pack(side="top")

        self.credit_entry = tk.Entry(self, textvariable = tk.StringVar(),cursor='mouse', width = 80)
        self.credit_entry.insert(0, "ENTER CREDIT CARD NUMBER HERE")
        self.credit_entry.pack()

        self.exp_entry = tk.Entry(self, textvariable = tk.StringVar(),cursor='mouse', width = 80)
        self.exp_entry.insert(0, "ENTER EXPIRATION DATE LIKE SO: MMYY(DO NOT PUT A SLASH!!!!!)")
        self.exp_entry.pack()

        self.cvv_entry = tk.Entry(self, textvariable = tk.StringVar(),cursor='mouse', width = 80)
        self.cvv_entry.insert(0, "ENTER 3 DIGIT CVV HERE")
        self.cvv_entry.pack()

        self.zip_entry = tk.Entry(self, textvariable = tk.StringVar(),cursor='mouse', width = 80)
        self.zip_entry.insert(0, "ENTER ZIPCODE HERE")
        self.zip_entry.pack()


    def save_info(self):
        # Extract the information to build a credit card
        card_number = self.credit_entry.get().strip()
        expiration = self.exp_entry.get().strip()
        cvv = self.cvv_entry.get().strip()
        thezip = self.zip_entry.get().strip()
        
        # Try to construct and validate the credit card
        try:
            saved_card = CreditCard(card_number,expiration,cvv,thezip)
            print("credit card valid")
            place_command = print("placing card order")
            # place_command = self.controller.customer.chosen_rst.place_order(self.controller.order, card=saved_card)
            if self.place_card_order == None:
                self.place_card_order = ttk.Button(self, text= "Place my order", command = place_command)
                self.place_card_order.pack()

        except Exception as error:
            print(error)
            if self.error_label == None:
                self.error_label = tk.Label(self, text = error)
                self.error_label.pack()
            else:
                self.error_label["text"] = error


        
