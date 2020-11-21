
import tkinter as tk
from tkinter import font as tkfont # python 3
from tkinter import ttk
from PIL import ImageTk, Image




# 6026 Ashford Falls Lane, Houston, Texas, 77479
# Class representing our start page!
class StartPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # START MAKING YOUR LABELS, BUTTONS, ETC. FOR THE WELCOME PAGE HERE
        label = tk.Label(self, text="Pizza Gui™", font=('Courier New',30))
        label.pack(side="right", fill="x", pady=100)
        
        self.close_button = ttk.Button(self, text= "Quit", command=parent.quit,cursor='cross')
        self.close_button.pack(pady="5")
        self.next_button = ttk.Button(self,text="Next",command = lambda: controller.show_frame('InfoPage'),cursor='cross')
        self.next_button.pack(pady="10")
        

        # replace dominos.jpg with path towhatever image you want
        img = ImageTk.PhotoImage(Image.open('dominos.jpeg'))
        # img2 = ImageTk.PhotoImage(Image.open('images/cart.jpeg'))

        panel = tk.Label(self, image =img, text="hi")
        # panel = tk.Label(self, image =img2, text="hi")

        panel.image = img
        panel.pack(side = "top", fill="both")
        
