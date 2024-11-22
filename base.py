import subprocess
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to convert bases and display formula
def convert_base():
    try:
        input_value = entry_input.get()  # Get input value
        input_unit = combo_input.get()  # Get input base
        output_unit = combo_output.get()  # Get output base

        # Determine the base for the input
        base_map = {
            "Binary": 2,
            "Octal": 8,
            "Decimal": 10,
            "Hexadecimal": 16
        }
        input_base = base_map[input_unit]
        output_base = base_map[output_unit]

        # Conversion
        if input_base == 10:
            # If input is decimal, convert directly to target base
            decimal_value = int(input_value)
        else:
            # Convert input from the given base to decimal
            decimal_value = int(input_value, input_base)

        # Convert decimal to the target base
        if output_base == 2:
            converted_value = bin(decimal_value)[2:]  # Binary
        elif output_base == 8:
            converted_value = oct(decimal_value)[2:]  # Octal
        elif output_base == 16:
            converted_value = hex(decimal_value)[2:].upper()  # Hexadecimal
        else:
            converted_value = str(decimal_value)  # Decimal

        # Display the converted value
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, converted_value)

        # Display the formula
        label_formula.configure(
            text=f"Formula: Convert {input_value} ({input_unit}) → {converted_value} ({output_unit})"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for the selected base.")

# Function to refresh the input and output fields
def refresh_fields():
    entry_input.delete(0, ctk.END)
    entry_output.delete(0, ctk.END)
    combo_input.set("Decimal")
    combo_output.set("Binary")
    label_formula.configure(text="Formula:")

# Function to exit and run the next file
def run():
    root.destroy()
    subprocess.run(['python', 'menu1.py'])

# Create the main window using customtkinter
ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue", "green", "dark-blue"

root = ctk.CTk()  # Use CTk instead of Tk
root.title("Base Converter")
root.geometry('1000x800')

# Resize the logo image using PIL and display it on the left
logo_image = Image.open("Background images/basebg.png")  # Adjust this path
logo_image = logo_image.resize((1000, 800), Image.Resampling.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

# Display the resized logo
logo_label = ctk.CTkLabel(root, image=logo_photo)
logo_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Frame with a distinct color
frame = ctk.CTkFrame(root, width=900, height=575, corner_radius=10, fg_color="#004d00")  # Dark green color
frame.pack(padx=10, pady=150)

# Label
label = ctk.CTkLabel(frame, text="Base Converter", font=("Helvetica", 30, 'bold'), text_color="white")
label.grid(column=2, row=0, pady=40)

# Base options
base_units = ["Binary", "Octal", "Decimal", "Hexadecimal"]

# Input Section
input_type_label = ctk.CTkLabel(frame, text="Input Base", text_color="white")
input_type_label.grid(row=1, column=0, padx=20, pady=10)

combo_input = ctk.CTkComboBox(frame, values=base_units, state="readonly", button_color="#008000")
combo_input.grid(row=1, column=1, padx=10, pady=10)
combo_input.set("Decimal")

input_label = ctk.CTkLabel(frame, text="Input Value:", text_color="white")
input_label.grid(row=2, column=0, padx=10, pady=10)

entry_input = ctk.CTkEntry(frame)
entry_input.grid(row=2, column=1, padx=10, pady=10)

# Button to perform the conversion
convert_button = ctk.CTkButton(frame, text="Convert", command=convert_base, fg_color="#33cc33")
convert_button.grid(row=1, column=2, rowspan=2, pady=10)

# Output Section
output_type_label = ctk.CTkLabel(frame, text="Output Base", text_color="white")
output_type_label.grid(row=1, column=3, padx=10, pady=10)

combo_output = ctk.CTkComboBox(frame, values=base_units, state="readonly", button_color="#008000")
combo_output.grid(row=1, column=4, padx=20, pady=10)
combo_output.set("Binary")

output_label = ctk.CTkLabel(frame, text="Output Value:", text_color="white")
output_label.grid(row=2, column=3, padx=10, pady=10)

entry_output = ctk.CTkEntry(frame)
entry_output.grid(row=2, column=4, padx=10, pady=10)

# Label to display the formula
label_formula = ctk.CTkLabel(frame, text="Formula:", anchor="w", text_color="white", wraplength=800)
label_formula.grid(row=3, column=0, columnspan=5, sticky="w", padx=10, pady=20)

# Refresh button
refresh_button = ctk.CTkButton(frame, text="Refresh", command=refresh_fields, fg_color="#009900")
refresh_button.grid(row=4, column=1, columnspan=2, padx=10)

# Exit button
exit_button = ctk.CTkButton(frame, text="Exit", command=run, fg_color="#cc0000")
exit_button.grid(row=4, column=2, padx=20, pady=50, columnspan=3)

# Run the customtkinter event loop
root.mainloop()