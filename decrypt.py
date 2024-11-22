import subprocess
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk
def decrypt_message():
    try:
        input_text = entry_input.get()
        shift_value = int(entry_shift.get())
        decrypted_text = ''.join(
            [chr((ord(char) - shift_value - 65) % 26 + 65) if char.isupper() else
            chr((ord(char) - shift_value - 97) % 26 + 97) if char.islower() else char
            for char in input_text]
        )
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, decrypted_text)
        label_formula.configure(text=f"Formula: Shift each letter by -{shift_value} for decryption")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid shift value.")
def refresh_fields():
    entry_input.delete(0, ctk.END)
    entry_output.delete(0, ctk.END)
    entry_shift.delete(0, ctk.END)
    label_formula.configure(text="Formula:")
def run():
    root.destroy()
    subprocess.run(['python', 'encrptmenu.py'])
def encrypt():
    root.destroy()
    subprocess.run(['python', 'encrypter.py'])
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")
root = ctk.CTk()
root.title("Text Decrypter")
root.geometry('1000x800')
logo_image = Image.open("Background images/encrypbg.png")
logo_image = logo_image.resize((1000, 800), Image.Resampling.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = ctk.CTkLabel(root, image=logo_photo)
logo_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
frame = ctk.CTkFrame(root, width=900, height=575, corner_radius=10,fg_color='black')
frame.pack(padx=10, pady=150)
label = ctk.CTkLabel(frame, text="Text Decrypter", font=("Helvetica", 30, 'bold'))
label.grid(column=1, row=0, pady=40)
input_label = ctk.CTkLabel(frame, text="Enter Encrypted Text:")
input_label.grid(row=1, column=0, padx=20, pady=10)
entry_input = ctk.CTkEntry(frame)
entry_input.grid(row=1, column=1, padx=10, pady=10)
shift_label = ctk.CTkLabel(frame, text="Enter Shift Value:")
shift_label.grid(row=2, column=0, padx=20, pady=10)
entry_shift = ctk.CTkEntry(frame)
entry_shift.grid(row=2, column=1, padx=10, pady=10)
decrypt_button = ctk.CTkButton(frame, text="Decrypt", command=decrypt_message,fg_color='crimson')
decrypt_button.grid(row=3, column=1, pady=20)
output_label = ctk.CTkLabel(frame, text="Decrypted Message:")
output_label.grid(row=4, column=0, padx=10, pady=10)
entry_output = ctk.CTkEntry(frame)
entry_output.grid(row=4, column=1, padx=10, pady=10)
label_formula = ctk.CTkLabel(frame, text="Formula:", anchor="w")
label_formula.grid(row=5, column=0, columnspan=2, sticky="w", padx=10, pady=20)
encrypt_button = ctk.CTkButton(frame, text="Encrypt", command=encrypt,fg_color='red',hover_color='firebrick4')
encrypt_button.grid(row=6, column=0, padx=20, pady=50)
refresh_button = ctk.CTkButton(frame, text="Refresh", command=refresh_fields,fg_color='red',hover_color='firebrick4')
refresh_button.grid(row=6, column=1, padx=10)
exit_button = ctk.CTkButton(frame, text="Exit", command=run,fg_color='red',hover_color='firebrick4')
exit_button.grid(row=6, column=2, padx=20, pady=50, columnspan=2)

root.mainloop()