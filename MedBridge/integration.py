from customtkinter import *
from PIL import Image
import cv2
import pytesseract
from deep_translator import GoogleTranslator

pytesseract.pytesseract.tesseract_cmd = r"C:\\Python_Libraries\\tesseract.exe"

def extract_text_from_image_cv2(image) -> str:
    if image is None:
        raise ValueError("Invalid image")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text.strip()

def write_text_to_file(text: str, output_path: str):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

def read_text_from_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def translate_text(text: str, dest_lang: str = "es") -> str:
    try:
        translated = GoogleTranslator(source='auto', target=dest_lang).translate(text)
        return translated
    except Exception as e:
        return f"Translation failed: {e}"

users = {"test1": 1234, "test2": 123}

def quit_program():
    app.destroy()

def login():
    user_name = entry_name.get().lower()
    user_pass = entry_pas.get()

    if user_name not in users:
        login_message.configure(text="Invalid user, please try again.", text_color="red")
        return

    try:
        if int(user_pass) == users[user_name]:
            login_message.configure(text="Logged IN", text_color="green")
            main_page()
        else:
            login_message.configure(text="Invalid passcode, please try again.", text_color="red")
    except ValueError:
        login_message.configure(text="Passcode must be a number.", text_color="red")

def main_page():
    frame.pack_forget()

    global main_view
    main_view = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
    main_view.pack_propagate(0)
    main_view.pack(expand=True, side="right")

    CTkLabel(master=main_view, text="Main Menu", text_color="#016dff",
             anchor="w", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))

    CTkButton(master=main_view, text="EchoCare", fg_color="#016dff",
              font=("Arial Bold", 12), text_color="#ffffff",
              width=225).pack(pady=12, padx=10)

    CTkButton(master=main_view, text="MedExtract", fg_color="#016dff",
              font=("Arial Bold", 12), text_color="#ffffff", width=225,
              command=medextract_window).pack(pady=12, padx=10)

    CTkButton(master=main_view, text="Quit", fg_color="transparent",
              font=("Arial Bold", 8), text_color="black", width=8,
              border_width=2, border_color='black', corner_radius=32,
              command=quit_program).pack(anchor="se", pady=(0, 20), padx=(0, 20))

def medextract_window():
    main_view.pack_forget()

    extract_view = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
    extract_view.pack_propagate(0)
    extract_view.pack(expand=True, side="right")

    def browse_image():
        path = filedialog.askopenfilename()
        if not path:
            return
        img = cv2.imread(path)
        text = extract_text_from_image_cv2(img)
        write_text_to_file(text, "output.txt")
        original_text_box.delete("0.0", END)
        translated_text_box.delete("0.0", END)
        original_text_box.insert("0.0", text)
        translated = translate_text(text, dest_lang="es")  # Change language as needed
        translated_text_box.insert("0.0", translated)

    CTkLabel(master=extract_view, text="OCR Translate", text_color="#016dff",
             anchor="w", font=("Arial Bold", 24)).pack(anchor="w", pady=(20, 5), padx=(25, 0))

    CTkButton(master=extract_view, text="Upload Image", fg_color="#016dff",
              font=("Arial Bold", 12), text_color="#ffffff", width=225,
              command=browse_image).pack(pady=12, padx=10)

    CTkLabel(master=extract_view, text="Original Text", text_color="#000000",
             anchor="w", font=("Arial", 12)).pack(anchor="w", padx=(25, 0))

    original_text_box = CTkTextbox(master=extract_view, width=250, height=100)
    original_text_box.pack(padx=20, pady=5)

    CTkLabel(master=extract_view, text="Translated Text", text_color="#000000",
             anchor="w", font=("Arial", 12)).pack(anchor="w", padx=(25, 0))

    translated_text_box = CTkTextbox(master=extract_view, width=250, height=100)
    translated_text_box.pack(padx=20, pady=5)

    CTkButton(master=extract_view, text="Back", fg_color="transparent",
              font=("Arial Bold", 10), text_color="black", width=100,
              border_width=2, border_color='black', corner_radius=8,
              command=lambda: [extract_view.pack_forget(), main_page()]).pack(pady=(10, 0))

# ========== GUI SETUP ==========
app = CTk()
app.geometry("600x480")
app.title("MedBridge_V1")
app.resizable(0, 0)

from tkinter import filedialog  # Needed for file browsing

side_img = CTkImage(Image.open("./Image/Doctor.jpg"), size=(300, 480))
user_icon = CTkImage(Image.open("./Logo/Email.jpg"), size=(20, 20))
password_icon = CTkImage(Image.open("./Logo/Lock.jpg"), size=(17, 17))

CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

CTkLabel(master=frame, text="Welcome Back!", text_color="#016dff",
         anchor="w", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(25, 0))

CTkLabel(master=frame, text="Sign into your Account.", text_color="#7E7E7E",
         anchor="w", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Username:", text_color="#016dff",
         anchor="w", font=("Arial Bold", 14), image=user_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))

entry_name = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#016dff",
                      border_width=1, text_color="#000000", placeholder_text="Ex: Mark")
entry_name.pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Password:", text_color="#016dff",
         anchor="w", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))

entry_pas = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#016dff",
                     border_width=1, text_color="#000000", show="*", placeholder_text="ex: 9624")
entry_pas.pack(anchor="w", padx=(25, 0))

login_message = CTkLabel(master=frame, text="", text_color="red",
                         anchor="w", font=("Arial Bold", 12))
login_message.pack(anchor="w", pady=(10, 0), padx=(25, 0))

CTkButton(master=frame, text="Login", fg_color="#016dff",
          font=("Arial Bold", 12), text_color="#ffffff", width=225,
          command=login).pack(anchor="w", pady=(25, 0), padx=(25, 0))

CTkButton(master=frame, text="Quit", fg_color="transparent",
          font=("Arial Bold", 8), text_color="black", width=8,
          border_width=2, border_color='black', corner_radius=32,
          command=quit_program).pack(anchor="se", pady=(30, 20), padx=(0, 50))

app.mainloop()
