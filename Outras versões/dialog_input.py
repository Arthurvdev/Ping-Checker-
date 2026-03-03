import customtkinter
import tkinter

customtkinter.set_appearance_mode("dark")

app = customtkinter.CTk()
app.geometry("400x300")


def button_click_event():
    dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="Test")
    print("Number:", dialog.get_input())


button = customtkinter.CTkButton(app, text="Open Dialog", command=button_click_event)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()