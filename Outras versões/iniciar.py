import tkinter  
import tkinter as tk
import customtkinter

def teste():
    dadasdas = input("insira um valor")
    

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()

root.geometry("800x600")

text_var = tkinter.StringVar(value="CTkLabel")

entry = customtkinter.CTkEntry(master=root, placeholder_text="CTkEntry")
entry.pack(padx=20, pady=10)

button = customtkinter.CTkButton(master=root, text="Botão", command=teste())
button.place(relx=0.5, rely=0.5, anchor="center")


root.mainloop()