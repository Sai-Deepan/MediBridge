from customtkinter import *
from tkinter import messagebox
from PIL import Image
from datetime import datetime


users = {"test1":1234,"test2":123}
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


    def add_patient():
        Add_frame.forget()
        global patient_add_frame
        patient_add_frame = CTkScrollableFrame(master=app, width=300, height=480, fg_color="#ffffff")
        patient_add_frame.pack(expand=True, side="right", fill="both")  # Ensure the frame fills the space


        CTkLabel(master=patient_add_frame, text="Add New Records", text_color="#016dff", anchor="w", justify="left",
                 font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))

        CTkLabel(master=patient_add_frame, text="Patient ID:", text_color="#016dff", anchor="w", justify="left",
                 font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        patient_id_add = CTkEntry(master=patient_add_frame, width=225, fg_color="#EEEEEE", border_color="#016dff",
                                  border_width=1, text_color="#000000", placeholder_text="Enter Patient ID:")
        patient_id_add.pack(anchor="w", padx=(25, 0))

        CTkLabel(master=patient_add_frame, text="Patient Name:", text_color="#016dff", anchor="w", justify="left",
                 font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        patient_name_add = CTkEntry(master=patient_add_frame, width=225, fg_color="#EEEEEE", border_color="#016dff",
                                    border_width=1, text_color="#000000", placeholder_text="Enter Patient Name:")
        patient_name_add.pack(anchor="w", padx=(25, 0))

        CTkLabel(master=patient_add_frame, text="Patient Age:", text_color="#016dff", anchor="w", justify="left",
                 font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        patient_age_add = CTkEntry(master=patient_add_frame, width=225, fg_color="#EEEEEE", border_color="#016dff",
                                   border_width=1, text_color="#000000", placeholder_text="Enter Patient Age:")
        patient_age_add.pack(anchor="w", padx=(25, 0))

        CTkLabel(master=patient_add_frame, text="Patient Phone Number:", text_color="#016dff", anchor="w",
                 justify="left",
                 font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        patient_phone_add = CTkEntry(master=patient_add_frame, width=225, fg_color="#EEEEEE", border_color="#016dff",
                                     border_width=1, text_color="#000000",
                                     placeholder_text="Enter Patient Phone Number:")
        patient_phone_add.pack(anchor="w", padx=(25, 0))

        CTkLabel(master=patient_add_frame, text="Patient Address:", text_color="#016dff", anchor="w", justify="left",
                 font=("Arial Bold", 14), compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
        patient_address_add = CTkEntry(master=patient_add_frame, width=225, fg_color="#EEEEEE", border_color="#016dff",
                                       border_width=1, text_color="#000000", placeholder_text="Enter Patient Address:")
        patient_address_add.pack(anchor="w", padx=(25, 0))
        CTkButton(master=patient_add_frame, text="Save", fg_color="#016dff", font=("Arial Bold", 12), text_color="#ffffff",
                  width=225,command=lambda: save_add('patient', {
                'Patient_id': patient_id_add.get(),
                'Name': patient_name_add.get(),
                'Age': patient_age_add.get(),
                'Phone_no': patient_phone_add.get(),
                'Address': patient_address_add.get()
                })).pack(anchor="w", pady=(25, 0), padx=(25, 0))

        CTkButton(master=patient_add_frame, text="Main Menu", fg_color="transparent",
                  font=("Arial Bold", 8), text_color="black", width=8, border_width=2,
                  border_color='black', corner_radius=32, command=HOME).pack(
            anchor="se", pady=(30, 20), padx=(0, 50))

def quit_program():
    cursor.close()
    connection.close()
    app.destroy()

app = CTk()
app.geometry("600x480")
app.title("Hospital-Management_V3")
app.resizable(0, 0)

side_img_data = Image.open("./Image/Doctor.jpg")
email_icon_data = Image.open("./Logo/Email.jpg")
password_icon_data = Image.open("./Logo/Lock.jpg")

side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
user_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20, 20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")
frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

CTkLabel(master=frame, text="Welcome Back!", text_color="#016dff", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))
CTkLabel(master=frame, text="Sign into your Account.", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Username:", text_color="#016dff",     anchor="w", justify="left", font=("Arial Bold", 14), image=user_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
entry_name = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#016dff", border_width=1, text_color="#000000", placeholder_text="Ex: Mark")
entry_name.pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Password:", text_color="#016dff", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
entry_pas = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#016dff", border_width=1, text_color="#000000", show="*", placeholder_text="ex: 9624")
entry_pas.pack(anchor="w", padx=(25, 0))

login_message = CTkLabel(master=frame, text="", text_color="red", anchor="w", justify="left", font=("Arial Bold", 12))
login_message.pack(anchor="w", pady=(10, 0), padx=(25, 0))

CTkButton(master=frame, text="Login", fg_color="#016dff",  font=("Arial Bold", 12), text_color="#ffffff", width=225,command=login).pack(anchor="w", pady=(25, 0), padx=(25, 0))
CTkButton(master=frame, text="Quit", fg_color="transparent",
              font=("Arial Bold", 8), text_color="black", width=8 ,border_width=2,
              border_color='black', corner_radius=32).pack(
            anchor="se", pady=(30, 20), padx=(0, 50))

app.mainloop()
