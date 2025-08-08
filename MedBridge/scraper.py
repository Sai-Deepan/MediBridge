from customtkinter import *
from tkinter import messagebox
from PIL import Image
from datetime import datetime

users = {"Test1":1234,"Test2":123}

def HOME():
    if 'Add_frame' in globals():
        Add_frame.pack_forget()
    if 'Delete_frame' in globals():
        Delete_frame.pack_forget()
    if 'Bill_Frame' in globals():
        Bill_Frame.pack_forget()
    if 'Inventory_Frame' in globals():
        Inventory_Frame.pack_forget()
    if 'patient_add_frame' in globals():
        patient_add_frame.pack_forget()
    if 'doctor_add_frame' in globals():
        doctor_add_frame.pack_forget()
    if 'staff_add_frame' in globals():
        staff_add_frame.pack_forget()
    if 'Del_frame' in globals():
        Del_frame.pack_forget()
    if 'supply1_frame' in globals():
        supply1_frame.pack_forget()
    if 'alert_frame' in globals():
        alert_frame.pack_forget()

    main_page()

def login():
    user_name = entry_name.get().lower()
    user_pass = entry_pas.get()

    if user_name not in users:
        login_message.configure(text="Invalid user, please try again.", text_color="red")
    else:
        try:
            if int(user_pass) == users[user_name]:
                login_message.configure(text="Logged IN", text_color="green")
                main_page()
            else:
                login_message.configure(text="Invalid passcode, please try again.", text_color="red")
        except ValueError:
            login_message.configure(text="Passcode must be a number.", text_color="red")

def Add_record():
    main_view.pack_forget()
    global Add_frame
    Add_frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
    Add_frame.pack_propagate(0)
    Add_frame.pack(expand=True, side="right")
