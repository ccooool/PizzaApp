from pizzapy.customer import Customer
import tkinter as tk
from tkinter import font as tkfont # python 3
from tkinter import ttk
from pizzapy.store import StoreLocator

class RestPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.bacc_button = ttk.Button(self, text= "Back", command=lambda: controller.show_frame("StartPage"),cursor='mouse')
        self.bacc_button.pack(pady="5")
        self.close_button = ttk.Button(self, text= "Quit", command=parent.quit)
        self.close_button.pack(pady="5")
        self.close_button.place(x = 0, y = 0)

        label = tk.Label(self, text="This is the Restaurant page", font = ('Impact',30))
        label.pack(side="top", fill="x", pady=50)
        self.find_teh_closest_store = ttk.Button(self,text="Find stores nearby now!",command=lambda: self.show_the_stores_now(controller.customer.address))
        self.find_teh_closest_store.pack(side="bottom")
        self.labbell = None
        self.confirm_add = None
        
        
    def show_the_stores_now(self, addr): 
        print("address second location: "  + str(addr))
        stores = StoreLocator.nearby_stores(addr) #give us an array of stores
        if len(stores) == 0:
            message = "please enter a valid address; no stores found near you"
        message = str(stores[0])
        self.labbell = tk.Label(self,text = "we have found this store closest to you: \n" + message)
        self.labbell.pack(side = "bottom")
        
        if self.confirm_add == None:
            self.confirm_add=ttk.Button(self,text="Use this store",command= lambda:self.confirm_rest(stores[0]))
            self.confirm_add.pack(side="top")

    def confirm_rest(self, chosen_rest):
        self.controller.customer.chosen_rst = chosen_rest
        self.controller.show_frame("MenuPage")
        