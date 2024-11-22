import subprocess
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

# Conversion factors
conversion_factors = {
    "ton": 1_000_000,         # ton to grams
    "kilogram": 1_000,        # kg to grams
    "gram": 1,                # gram to grams
    "milligram": 0.001,       # mg to grams
    "microgram": 0.000001,    # µg to grams
    "imperial ton": 1_016_046.9088,  # imperial ton to grams
    "US ton": 907_184.74,     # US ton to grams
    "stone": 6_350.29318,     # stone to grams
    "pound": 453.59237,       # pound to grams
    "ounce": 28.349523125     # ounce to grams
}

# Function to convert mass based on input and output types
def convert_mass():
    try:
        input_value = float(entry_input.get())
        input_type = combo_input.get()
        output_type = combo_output.get()

        # Convert input to grams
        grams = input_value * conversion_factors[input_type]

        # Convert grams to the desired output type
        result = grams / conversion_factors[output_type]

        # Display result
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, str(result))

        # Display formula and conversion explanation
        formula = f"{input_value} {input_type} = {result} {output_type}"
        label_formula.configure(text=f"Formula: {formula}")
        label_conversion.configure(text=f"Conversion: {input_value} {input_type} = {result} {output_type}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number and select valid options.")

# Function to refresh the input and output fields
def refresh_fields():
    entry_input.delete(0, ctk.END)
    entry_output.delete(0, ctk.END)
    combo_input.set("ton")  # Reset to ton
    combo_output.set("kilogram")  # Reset to kilogram
    label_formula.configure(text="Formula: ")
    label_conversion.configure(text="Conversion: ")

# Create the main window using customtkinter
ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()  # Use CTk instead of Tk
root.title("Mass & weight Converter")
root.geometry('1000x800')

# Resize the logo image using PIL and display it on the left
logo_image = Image.open("Background images/massBG.png")
logo_image = logo_image.resize((1000, 800), Image.Resampling.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)
# Display the resized logo
logo_label = ctk.CTkLabel(root, image=logo_photo)
logo_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)


# Frame
frame = ctk.CTkFrame(root, width=900, height=575, corner_radius=10)
frame.pack(padx=10, pady=150)

# Label
label = ctk.CTkLabel(frame, text="Mass & Weight Converter", font=("Helvetica", 30, 'bold'))
label.grid(column=2, row=0, pady=40)

# Mass options for the combobox
mass_options = ["ton", "kilogram", "gram", "milligram", "microgram",
                "imperial ton", "US ton", "stone", "pound", "ounce"]

def run():
    root.destroy()
    subprocess.run(['Python','menu1.py'])


# Input Section
input_type_label = ctk.CTkLabel(frame, text="Input Type")
input_type_label.grid(row=1, column=0, padx=20, pady=10)

combo_input = ctk.CTkComboBox(frame, values=mass_options, state="readonly")
combo_input.grid(row=1, column=1, padx=10, pady=10)
combo_input.set("ton")

input_label = ctk.CTkLabel(frame, text="Input:")
input_label.grid(row=2, column=0, padx=10, pady=10)

entry_input = ctk.CTkEntry(frame)
entry_input.grid(row=2, column=1, padx=10, pady=10)

# Button to perform the conversion
convert_button = ctk.CTkButton(frame, text="Convert", command=convert_mass)
convert_button.grid(row=1, column=2,rowspan=2, pady=10)

# Output Section
output_type_label = ctk.CTkLabel(frame, text="Output Type")
output_type_label.grid(row=1, column=3, padx=10, pady=10)

combo_output = ctk.CTkComboBox(frame, values=mass_options, state="readonly")
combo_output.grid(row=1, column=4, padx=20, pady=10)
combo_output.set("kilogram")  # Default to kilogram

output_label = ctk.CTkLabel(frame, text="Output:")
output_label.grid(row=2, column=3, padx=10, pady=10)

entry_output = ctk.CTkEntry(frame)
entry_output.grid(row=2, column=4, padx=10, pady=10)

# Labels to display the formula and conversion explanation
label_formula = ctk.CTkLabel(frame, text="Formula: ", anchor="w")
label_formula.grid(row=3, column=0,columnspan=4,sticky="w", padx=10)

label_conversion = ctk.CTkLabel(frame, text="Conversion: ", anchor="w")
label_conversion.grid(row=4, column=0, columnspan=4, sticky="w", padx=10)

# Refresh button
refresh_button = ctk.CTkButton(frame, text="Refresh", command=refresh_fields)
refresh_button.grid(row=5, column=1,columnspan=2,padx=10)

# Exit button
exit_button = ctk.CTkButton(frame, text="Exit", command=run)
exit_button.grid(row=5, column=2, padx=20, pady=50,columnspan=3)

# Run the customtkinter event loop
root.mainloop()