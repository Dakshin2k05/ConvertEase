import customtkinter as ctk
import subprocess
from tkinter import messagebox
from PIL import Image, ImageTk

def run():
    root.destroy()
    subprocess.run(['python', '/Users/dakshin/Documents/TERM-3/project python/menu1.py'])

# Conversion factors (relative to Bit)
storage_units = {
    "Bit": 1,
    "Kilobit": 10**3,
    "Kibibit": 2**10,
    "Megabit": 10**6,
    "Mebibit": 2**20,
    "Gigabit": 10**9,
    "Gibibit": 2**30,
    "Terabit": 10**12,
    "Tebibit": 2**40,
    "Petabit": 10**15,
    "Pebibit": 2**50,
    "Byte": 8,
    "Kilobyte": 10**3 * 8,
    "Kibibyte": 2**10 * 8,
    "Megabyte": 10**6 * 8,
    "Mebibyte": 2**20 * 8,
    "Gigabyte": 10**9 * 8,
    "Gibibyte": 2**30 * 8,
    "Terabyte": 10**12 * 8,
    "Tebibyte": 2**40 * 8,
    "Petabyte": 10**15 * 8,
    "Pebibyte": 2**50 * 8
}

# Function to refresh all fields
def refresh_fields():
    combo_input.set("Byte")  # Reset input combo box to default
    combo_output.set("Bit")  # Reset output combo box to default
    entry_input.delete(0, ctk.END)  # Clear input entry field
    entry_output.delete(0, ctk.END)  # Clear output entry field

# Conversion function
def perform_conversion():
    try:
        input_value = float(entry_input.get())  # Get the input value
        input_unit = combo_input.get()  # Get selected input unit
        output_unit = combo_output.get()  # Get selected output unit

        # Convert the input value to bits
        input_in_bits = input_value * storage_units[input_unit]

        # Convert from bits to the target output unit
        output_value = input_in_bits / storage_units[output_unit]

        # Display the result in the output entry field
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, f"{output_value:.6f}")  # Display the result with 6 decimal places
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

# Create the main window using customtkinter
ctk.set_appearance_mode("dark-blue")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()  # Use CTk instead of Tk
root.title("Digital Storage Converter")
root.geometry('1000x800')

# Resize the logo image using PIL and display it on the left
logo_image = Image.open("Background images/data storebg.png")  # Path to the logo image
logo_image = logo_image.resize((1000, 800), Image.Resampling.LANCZOS)  # Resize the image to 1000x600 pixels
logo_photo = ImageTk.PhotoImage(logo_image)
# Display the resized logo
logo_label = ctk.CTkLabel(root, image=logo_photo)
logo_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Frame
frame = ctk.CTkFrame(root, width=900, height=575, corner_radius=10, fg_color='black')
frame.pack(padx=10, pady=150)

digital_storage = ["Bit", "Kilobit", "Kibibit", "Megabit", "Mebibit", "Gigabit", "Gibibit", "Terabit", "Tebibit",
                   "Petabit", "Pebibit", "Byte", "Kilobyte", "Kibibyte", "Megabyte", "Mebibyte", "Gigabyte",
                   "Gibibyte", "Terabyte", "Tebibyte", "Petabyte", "Pebibyte"]

# Label
label = ctk.CTkLabel(frame, text="Data Transfer Rate", font=("Helvetica", 30, 'bold'))
label.grid(column=2, row=0, pady=40)

# Input Section
input_label = ctk.CTkLabel(frame, text="Input Type")
input_label.grid(row=1, column=0, padx=10, pady=10)

combo_input = ctk.CTkComboBox(frame, values=digital_storage, state="readonly")
combo_input.grid(row=1, column=1, padx=10, pady=10)
combo_input.set("Byte")  # Default to Byte

entry_input_label = ctk.CTkLabel(frame, text="Input Value")
entry_input_label.grid(row=2, column=0, padx=10, pady=10)

entry_input = ctk.CTkEntry(frame)
entry_input.grid(row=2, column=1, padx=10, pady=10)

# Button to perform the conversion
convert_button = ctk.CTkButton(frame, text="Convert", font=("Helvetica", 15), command=perform_conversion)
convert_button.grid(row=1, column=2, rowspan=2, pady=10)

# Output Section
output_label = ctk.CTkLabel(frame, text="Output Type")
output_label.grid(row=1, column=3, padx=10, pady=10)

combo_output = ctk.CTkComboBox(frame, values=digital_storage, state="readonly")
combo_output.grid(row=1, column=4, padx=10, pady=10)
combo_output.set("Bit")

entry_output_label = ctk.CTkLabel(frame, text="Output Value")
entry_output_label.grid(row=2, column=3, padx=10, pady=10)

entry_output = ctk.CTkEntry(frame)
entry_output.grid(row=2, column=4, padx=10, pady=10)

# Refresh button with linked function
refresh_button = ctk.CTkButton(frame, text="Refresh", font=("Helvetica", 15), command=refresh_fields)
refresh_button.grid(row=5, column=0, padx=20, pady=20, columnspan=2)

# Exit button
exit_button = ctk.CTkButton(frame, text="Exit", command=run)
exit_button.grid(row=5, column=3, padx=20, pady=50, columnspan=2)

root.mainloop()