from pizzapy.customer import Customer
import tkinter as tk
from tkinter import font as tkfont # python 3
from tkinter import ttk


# Class representing our start page!
class InfoPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # START MAKING YOUR LABELS, BUTTONS, ETC. FOR THE WELCOME PAGE HERE
        label = tk.Label(self, text="This is the info page", font = ('Impact',30) )
        label.pack(side="top", fill="x", pady=50)
        self.close_button = tk.Button(self, text= "Quit", command=parent.quit,cursor='mouse')
        self.close_button.pack()
        self.close_button.place(x = 0, y = 0)
        self.get_name()
        self.error_msg = tk.Label(self, text = "")
        self.error_msg.pack(side = "bottom", pady=50)

        
    def get_name(self): 
        self.banana = tk.Label(self, text="Please enter your first and last name", font = ('MS Gothic',20))
        self.banana.pack(side="left")
        self.entry = tk.Entry(self, textvariable = tk.StringVar(),cursor='mouse')
        self.entry.bind('<Return>', (lambda event: self.save_name()))
        self.entry.pack(side="left")

    def save_name(self):
        self.name = self.entry.get()
        if len(self.name.split(" ")) == 2:
            self.first_name = self.name.split(" ")[0]
            self.last_name = self.name.split(" ")[1]
            self.get_phone()
        else:
            self.error_msg['text'] = "Please enter a VaLiD first AND last name"

    def get_phone(self):
        self.banana['text'] = "Hello," +self.first_name+ " "+self.last_name +" could you please enter your phone number?"
        self.entry.bind('<Return>',(lambda event: self.save_phone()))
    def save_phone(self):
        self.p_number = self.entry.get()
        if self.p_number.isnumeric():
            self.get_email()
        else:
            self.error_msg['text'] = "Enter a VaLiD phone number"
    def get_email(self):
        self.banana['text'] = "Now "+self.first_name+ " can you enter your email address?"
        self.entry.bind('<Return>',(lambda event: self.save_mail()))
    def save_mail(self):
        self.mail_address = self.entry.get()
        if '@' in self.mail_address and "." in self.mail_address:
            print(self.mail_address)
            self.get_address()
        else:
            self.error_msg['text'] = "enter a VaLiD email adress like this one: example@xyz.com"
            
    """Create an address, for finding stores and placing orders.

    The Address object describes a street address in North America (USA or
    Canada, for now). Callers can use the Address object's methods to find
    the closest or nearby stores from the API. 

    Attributes:
        street (String): Street address
        city (String): North American city
        region (String): North American region (state, province, territory)
        zip (String): North American ZIP code
        urls (String): Country-specific URLs 
        country (String): Country

        5151 Edloe Street, Houston, Texas, 77005

    """
    def get_address(self):
        self.banana['text'] = "Now, please enter your address with this format: \n" \
            + 'Full Street Name, City, State/Province, ZIP/Postal Code \n' \
            + 'EXAMPLE: 700 Pennsylvania Avenue NW, Washington, DC, 20408'
        self.entry.bind('<Return>',(lambda event: self.save_address()))
    def save_address(self):
        self.address = self.entry.get()
        print(self.address)
        self.save_customer()
    
    def save_customer(self):
        self.customer = Customer(self.first_name, self.last_name, self.mail_address,self.p_number,self.address)
        print("saved customer successfully")
        self.controller.customer =  self.customer
        print("ADDRESSS IS HERE \n\n" + str(self.controller.customer.address))
        self.next_button = ttk.Button(self,text="NEXT",command = lambda: self.controller.show_frame('RestPage'),cursor='cross')
        self.next_button.pack(side='bottom')