import subprocess
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

# Conversion factors for fuel efficiency units (relative to Kilometer per Liter)
fuel_efficiency_factors = {
    "Mile per US gallon": 0.425144,  # 1 mile per US gallon = 0.425144 km per liter
    "Mile per UK gallon": 0.354006,  # 1 mile per UK gallon = 0.354006 km per liter
    "Kilometer per liter": 1,  # Base unit
    "Liter per 100 kilometers": 100  # Inverse, conversion will be handled differently
}

# Function to perform the conversion
def convert_fuel_efficiency():
    try:
        input_value = float(entry_input.get())  # Get input value
        input_unit = combo_input.get()  # Get input unit
        output_unit = combo_output.get()  # Get output unit

        # Special handling for "Liter per 100 kilometers"
        if input_unit == "Liter per 100 kilometers":
            km_per_liter = 100 / input_value  # Convert to Kilometer per Liter
        else:
            km_per_liter = input_value * fuel_efficiency_factors[input_unit]  # Convert to Kilometer per Liter

        if output_unit == "Liter per 100 kilometers":
            converted_value = 100 / km_per_liter  # Convert from Kilometer per Liter to Liter per 100 km
        else:
            converted_value = km_per_liter / fuel_efficiency_factors[output_unit]  # Convert to desired output unit

        # Display the converted value
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, str(round(converted_value, 6)))

        # Display formula and conversion explanation
        label_formula.configure(text=f"Formula: {input_value} {input_unit} = {converted_value:.6f} {output_unit}")
        label_conversion.configure(
            text=f"Conversion: {input_value} {input_unit} → {converted_value:.6f} {output_unit}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for fuel efficiency input.")

# Function to refresh the input and output fields
def refresh_fields():
    entry_input.delete(0, ctk.END)
    entry_output.delete(0, ctk.END)
    combo_input.set("Kilometer per liter")
    combo_output.set("Mile per US gallon")
    label_formula.configure(text="Formula: ")
    label_conversion.configure(text="Conversion: ")

# Function to exit and run the next file
def run():
    root.destroy()
    subprocess.run(['python', '/Users/dakshin/Documents/TERM-3/project python/menu1.py'])

# Create the main window using customtkinter
ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

root = ctk.CTk()  # Use CTk instead of Tk
root.title("Fuel Efficiency Converter")
root.geometry('1000x800')

# Resize the logo image using PIL and display it on the left
logo_image = Image.open("Background images/fuel efficiencybg.png")  # Adjust this path
logo_image = logo_image.resize((1000, 800), Image.Resampling.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

# Display the resized logo
logo_label = ctk.CTkLabel(root, image=logo_photo)
logo_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Frame
frame = ctk.CTkFrame(root, width=900, height=575, corner_radius=10)
frame.pack(padx=10, pady=150)

# Label
label = ctk.CTkLabel(frame, text="Fuel Efficiency Converter", font=("Helvetica", 30, 'bold'))
label.grid(column=2, row=0, pady=40)

# Fuel efficiency units
fuel_efficiency_units = ["Mile per US gallon", "Mile per UK gallon", "Kilometer per liter", "Liter per 100 kilometers"]

# Input Section
input_type_label = ctk.CTkLabel(frame, text="Input Type")
input_type_label.grid(row=1, column=0, padx=20, pady=10)

combo_input = ctk.CTkComboBox(frame, values=fuel_efficiency_units, state="readonly")
combo_input.grid(row=1, column=1, padx=10, pady=10)
combo_input.set("Kilometer per liter")

input_label = ctk.CTkLabel(frame, text="Input Efficiency:")
input_label.grid(row=2, column=0, padx=10, pady=10)

entry_input = ctk.CTkEntry(frame)
entry_input.grid(row=2, column=1, padx=10, pady=10)

# Button to perform the conversion
convert_button = ctk.CTkButton(frame, text="Convert", command=convert_fuel_efficiency)
convert_button.grid(row=1, column=2, rowspan=2, pady=10)

# Output Section
output_type_label = ctk.CTkLabel(frame, text="Output Type")
output_type_label.grid(row=1, column=3, padx=10, pady=10)

combo_output = ctk.CTkComboBox(frame, values=fuel_efficiency_units, state="readonly")
combo_output.grid(row=1, column=4, padx=20, pady=10)
combo_output.set("Mile per US gallon")

output_label = ctk.CTkLabel(frame, text="Output Efficiency:")
output_label.grid(row=2, column=3, padx=10, pady=10)

entry_output = ctk.CTkEntry(frame)
entry_output.grid(row=2, column=4, padx=10, pady=10)

# Labels to display the formula and conversion explanation
label_formula = ctk.CTkLabel(frame, text="Formula: ", anchor="w")
label_formula.grid(row=3, column=0, columnspan=4, sticky="w", padx=10)

label_conversion = ctk.CTkLabel(frame, text="Conversion: ", anchor="w")
label_conversion.grid(row=4, column=0, columnspan=4, sticky="w", padx=10)

# Refresh button
refresh_button = ctk.CTkButton(frame, text="Refresh", command=refresh_fields)
refresh_button.grid(row=5, column=1, columnspan=2, padx=10)

# Exit button
exit_button = ctk.CTkButton(frame, text="Exit", command=run)
exit_button.grid(row=5, column=2, padx=20, pady=50, columnspan=3)

# Run the customtkinter event loop
root.mainloop()