import customtkinter

from random import choice
from string import ascii_uppercase, digits


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")

        self.title("Password Generator")
        self.geometry("400x300")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.textbox = customtkinter.CTkTextbox(master=self)
        self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 0), sticky="nsew")

        self.button = customtkinter.CTkButton(master=self, text="Generate!", command=self.generate_password)
        self.button.grid(row=1, column=1, padx=20, pady=20, sticky="ew")


    def generate_password(self):
        for i in range(5):
            password = ''.join(choice(ascii_uppercase + digits) for _ in range(10)) + "\n"
            self.textbox.insert("insert", password)
