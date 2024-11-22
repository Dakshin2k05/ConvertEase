import subprocess
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to encrypt the message using Caesar Cipher
def encrypt_message():
    try:
        # Get the input text and shift value
        input_text = entry_input.get()
        shift_value = int(entry_shift.get())  # Get the shift value for Caesar Cipher

        # Encrypt the message
        encrypted_text = ''.join(
            [chr((ord(char) + shift_value - 65) % 26 + 65) if char.isupper() else
            chr((ord(char) + shift_value - 97) % 26 + 97) if char.islower() else char
            for char in input_text]
        )

        # Display the encrypted message
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, encrypted_text)

        # Display the formula
        label_formula.configure(text=f"Formula: Shift each letter by {shift_value}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid shift value.")

# Function to refresh the input and output fields
def refresh_fields():
    entry_input.delete(0, ctk.END)
    entry_output.delete(0, ctk.END)
    entry_shift.delete(0, ctk.END)
    label_formula.configure(text="Formula:")

# Function to exit and run the next file
def run():
    root.destroy()
    subprocess.run(['python', 'encrptmenu.py'])
def encrypt():
    root.destroy()
    subprocess.run(['python', 'decrypt.py'])

# Create the main window using customtkinter
ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

root = ctk.CTk()  # Use CTk instead of Tk
root.title("Text Encrypter")
root.geometry('1000x800')

# Resize the logo image using PIL and display it on the left
logo_image = Image.open("Background images/encrypbg.png")  # Path to the logo image
logo_image = logo_image.resize((1000, 800), Image.Resampling.LANCZOS)  # Resize the image to 1000x600 pixels
logo_photo = ImageTk.PhotoImage(logo_image)
# Display the resized logo
logo_label = ctk.CTkLabel(root, image=logo_photo)
logo_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Frame with a distinct color
frame = ctk.CTkFrame(root, width=900, height=575, corner_radius=10,fg_color='black')
frame.pack(padx=10, pady=150)

# Label
label = ctk.CTkLabel(frame, text="Text Encrypter", font=("Helvetica", 30, 'bold'))
label.grid(column=1, row=0, pady=40)

# Input Section
input_label = ctk.CTkLabel(frame, text="Enter Text:")
input_label.grid(row=1, column=0, padx=20, pady=10)

entry_input = ctk.CTkEntry(frame)
entry_input.grid(row=1, column=1, padx=10, pady=10)

shift_label = ctk.CTkLabel(frame, text="Enter Shift Value:")
shift_label.grid(row=2, column=0, padx=20, pady=10)

entry_shift = ctk.CTkEntry(frame)
entry_shift.grid(row=2, column=1, padx=10, pady=10)

# Button to perform the encryption
encrypt_button = ctk.CTkButton(frame, text="Encrypt", command=encrypt_message,fg_color='crimson')
encrypt_button.grid(row=3, column=1, pady=20)

# Output Section
output_label = ctk.CTkLabel(frame, text="Encrypted Message:")
output_label.grid(row=4, column=0, padx=10, pady=10)

entry_output = ctk.CTkEntry(frame)
entry_output.grid(row=4, column=1, padx=10, pady=10)

# Label to display the formula
label_formula = ctk.CTkLabel(frame, text="Formula:", anchor="w")
label_formula.grid(row=5, column=0, columnspan=2, sticky="w", padx=10, pady=20)

encrypt_button = ctk.CTkButton(frame, text="Decrypt", command=encrypt,fg_color='red',hover_color='firebrick4')
encrypt_button.grid(row=6, column=0, padx=20, pady=50)

# Refresh button
refresh_button = ctk.CTkButton(frame, text="Refresh", command=refresh_fields,fg_color='red',hover_color='firebrick4')
refresh_button.grid(row=6, column=1, padx=10)

# Exit button
exit_button = ctk.CTkButton(frame, text="Exit", command=run,fg_color='red',hover_color='firebrick4')
exit_button.grid(row=6, column=2, padx=20, pady=50, columnspan=2)

# Run the customtkinter event loop
root.mainloop()