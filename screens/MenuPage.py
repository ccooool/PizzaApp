import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
from pizzapy.customer import Customer
from pizzapy.menu import Menu, MenuItem
from pizzapy.order import Order
from PIL import ImageTk, Image
from decimal import Decimal


class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.order = None
        self.total_price = 0
        self.item_count = 0

     
         # self.cart_contents.pack(side="right", padx=10, pady=10)

        thingything = tk.Label(self,text="Menu Page \n Instructions: \n Enter your search in the search bar to find what you want")
        thingything.pack(side="top", fill="x", pady=10)
        no_item_no = ttk.Button(self, text="delete item", command=lambda: self.remove())
        no_item_no.pack(side ="right", fill = "x", pady="10")

        cart_image = ImageTk.PhotoImage(Image.open('thingythingy.jpg').resize((50,50),Image.ANTIALIAS))

        self.done = ttk.Button(self,text="DONE, VIEW CART", image = cart_image, compound = "left", command=lambda: self.move_to_checkout())
        self.done.image = cart_image
        self.done.pack(side="top")


        self.search_entry = ttk.Entry(self, textvariable = tk.StringVar())
        self.search_entry.bind('<Return>', lambda event: self.item_lookup())
        self.search_entry.pack(padx="10", pady="10")
        
        #TODO: add label to label the select_entry
        select_entry = ttk.Entry(self, textvariable=tk.StringVar())
        select_entry.bind("<Return>", lambda event: self.add_item_to_cart(select_entry.get()))
        select_entry.pack(pady=20)


       

        self.items_prompt = tk.Text(self, font=("Helvetica", 20), width = "70", padx = "3.0", height = "20")
        self.items_prompt.pack(side="left", pady="5")
        # cart_img = ImageTk.PhotoImage(Image.open('images/cart.jpeg'))

        self.cart_contents = tk.Label(self, text="Order so far: \n",font=controller.title_font)
        self.cart_contents.pack(side="right", padx= "10", pady="10")
        
        self.proicelebel = tk.Label(self,text="Total Price "+str (self.total_price))
        self.proicelebel.pack(side="right")
    
        self.add_cart_button = ttk.Entry(self,text="Add to cart")
        self.cart_button = tk.Label(self,text="Cart "+ str(self.item_count))
        self.cart_button.pack(side="top")

        self.item_strings = []


        
    def move_to_checkout(self):
        print("møving †ø checkøu†")
        self.controller.order = self.order
        self.controller.total_price = self.total_price
        # right now, our order (which is our cart) is in self.order
        # we want to give self.order to the controller
        self.controller.show_frame("CheckoutPage")
        
    def item_lookup(self):
        if not self.order:
            self.order = Order(self.controller.customer.chosen_rst, self.controller.customer)
            self.menu = self.controller.customer.chosen_rst.get_menu()
        item = self.search_entry.get().strip()
        print("\n ITEM IS HERE: " ,item)
        print(self.menu)
        results = self.menu.search(Name=item) # results is an array of MenuItems
        print(results)
        result_str = ""
        for result in results:
            result_str += result.name +" " + str(result.price)+ " " + result.code + "\n"
        self.items_prompt.insert("1.0", result_str)

    def remove(self):
        # Only the cart is no empty, just skip everything
        if len(self.order.data["Products"]) != 0:
            print("removing item start")
            # Updating price
            self.item_count -= 1
            print("last item  before delete price: ", self.order.data["Products"][-1], "\n")
            price = float(self.order.data["Products"][-1]["Price"])
            print("price before: ", self.total_price)
            self.total_price -= price
            print("price after: ", self.total_price)
            self.proicelebel["text"] = "Total Price: $" + str(self.total_price)
            print("updated price")
        
            # self.order.data["Products"] = [{Name: Carter_Pizza, Price: 10}, {Name: Colin_Pizza, Price: 5}]
            self.order.data["Products"].pop(-1)
            # self.order.data["Products"] = [{Name: Carter_Pizza, Price: 10}]
            item_string = ""
            for product in self.order.data["Products"]:
                item_string += product["Name"] +"\n"
            self.cart_contents["text"] = item_string


        
    def add_item_to_cart(self, item_code):
        self.order.add_item(item_code)
        print(self.order.data["Products"])
        items = self.order.data["Products"][-1:]
        item_string = ""
        self.total_price += float(items[-1]["Price"])
        self.proicelebel["text"] = "Total Price: $" + str(self.total_price)
                                                                                                                                       
        for item in items:
            item_string += item["Name"] + "\n" 
            self.item_count += 1    
            self.cart_button["text"] = "Cart " + str(self.item_count)
        
        self.cart_contents["text"] += item_string
        print(self.cart_contents['text'])
        # TODO: for loop to go through all of items, get the name, and add the name to item_string
        self.controller.total_price =  float(round(Decimal(self.total_price), 2))

    