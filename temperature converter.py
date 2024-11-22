import subprocess
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

# Function to convert temperature based on input and output types
def convert_temperature():
    try:
        input_value = float(entry_input.get())
        input_type = combo_input.get()
        output_type = combo_output.get()

        formula = ""
        conversion_explanation = ""

        # Same unit, no conversion needed
        if input_type == output_type:
            result = input_value
            formula = "No conversion needed (same units)."
            conversion_explanation = f"{input_value} {input_type} = {result} {output_type}"

        # Celsius to other units
        elif input_type == "Celsius" and output_type == "Fahrenheit":
            result = (input_value * 9 / 5) + 32
            formula = "F = (C × 9/5) + 32"
            conversion_explanation = f"{input_value} Celsius = {result} Fahrenheit"
        elif input_type == "Celsius" and output_type == "Kelvin":
            result = input_value + 273.15
            formula = "K = C + 273.15"
            conversion_explanation = f"{input_value} Celsius = {result} Kelvin"

        # Fahrenheit to other units
        elif input_type == "Fahrenheit" and output_type == "Celsius":
            result = (input_value - 32) * 5 / 9
            formula = "C = (F - 32) × 5/9"
            conversion_explanation = f"{input_value} Fahrenheit = {result} Celsius"
        elif input_type == "Fahrenheit" and output_type == "Kelvin":
            result = (input_value - 32) * 5 / 9 + 273.15
            formula = "K = (F - 32) × 5/9 + 273.15"
            conversion_explanation = f"{input_value} Fahrenheit = {result} Kelvin"

        # Kelvin to other units
        elif input_type == "Kelvin" and output_type == "Celsius":
            result = input_value - 273.15
            formula = "C = K - 273.15"
            conversion_explanation = f"{input_value} Kelvin = {result} Celsius"
        elif input_type == "Kelvin" and output_type == "Fahrenheit":
            result = (input_value - 273.15) * 9 / 5 + 32
            formula = "F = (K - 273.15) × 9/5 + 32"
            conversion_explanation = f"{input_value} Kelvin = {result} Fahrenheit"

        else:
            raise ValueError("Invalid conversion")

        # Display result
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, str(result))

        # Display formula and conversion explanation
        label_formula.configure(text=f"Formula: {formula}")
        label_conversion.configure(text=f"Conversion: {conversion_explanation}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number and select valid options.")


# Function to refresh the input and output fields
def refresh_fields():
    entry_input.delete(0, ctk.END)
    entry_output.delete(0, ctk.END)
    combo_input.set("Celsius")  # Reset to Celsius
    combo_output.set("Fahrenheit")  # Reset to Fahrenheit
    label_formula.configure(text="Formula: ")
    label_conversion.configure(text="Conversion: ")

def run():
    root.destroy()
    subprocess.run(['python', '/Users/dakshin/Documents/TERM-3/project python/menu1.py'])


# Create the main window using customtkinter
ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()  # Use CTk instead of Tk
root.title("Temperature Converter")
root.geometry('1000x800')

# Resize the logo image using PIL and display it on the left
logo_image = Image.open("Background images/tempbg.png")  # Path to the logo image
logo_image = logo_image.resize((1000, 800), Image.Resampling.LANCZOS)  # Resize the image to 1000x600 pixels
logo_photo = ImageTk.PhotoImage(logo_image)
# Display the resized logo
logo_label = ctk.CTkLabel(root, image=logo_photo)
logo_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Frame
frame = ctk.CTkFrame(root, width=900, height=575, corner_radius=10,fg_color='#333333')
frame.pack(padx=10, pady=150)

# Label
label = ctk.CTkLabel(frame, text="Temperature Converter", font=("Helvetica", 30, 'bold'))
label.grid(column=2, row=0, pady=40)

temp_options = ["Celsius", "Fahrenheit", "Kelvin"]

# Input Section
input_label = ctk.CTkLabel(frame, text="Input Type")
input_label.grid(row=1, column=0, padx=10, pady=10)

combo_input = ctk.CTkComboBox(frame, values=temp_options, state="readonly")
combo_input.grid(row=1, column=1, padx=10, pady=10)
combo_input.set("Celsius")  # Default to Celsius

entry_input_label = ctk.CTkLabel(frame, text="Input Temperature")
entry_input_label.grid(row=2, column=0, padx=10, pady=10)

entry_input = ctk.CTkEntry(frame)
entry_input.grid(row=2, column=1, padx=10, pady=10)

# Button to perform the conversion
convert_button = ctk.CTkButton(frame, text="Convert", command=convert_temperature,font=("Helvetica", 15))
convert_button.grid(row=1, column=2, rowspan=2, pady=10)

# Output Section
output_label = ctk.CTkLabel(frame, text="Output Type")
output_label.grid(row=1, column=3, padx=10, pady=10)

combo_output = ctk.CTkComboBox(frame, values=temp_options, state="readonly")
combo_output.grid(row=1, column=4, padx=10, pady=10)
combo_output.set("Fahrenheit")  # Default to Fahrenheit

entry_output_label = ctk.CTkLabel(frame, text="Output Temperature")
entry_output_label.grid(row=2, column=3, padx=10, pady=10)

entry_output = ctk.CTkEntry(frame)
entry_output.grid(row=2, column=4, padx=10, pady=10)

# Refresh button
refresh_button = ctk.CTkButton(frame, text="Refresh", command=refresh_fields,font=("Helvetica", 15))
refresh_button.grid(row=5, column=0, padx=20, pady=20,columnspan=2)

# Exit button
exit_button = ctk.CTkButton(frame, text="Exit", command=run)
exit_button.grid(row=5, column=3, padx=20, pady=50,columnspan=2)

# Labels to display the formula and conversion explanation
label_formula = ctk.CTkLabel(frame, text="Formula: ", anchor="w")
label_formula.grid(row=3, column=0, columnspan=4, sticky="w", padx=10)

label_conversion = ctk.CTkLabel(frame, text="Conversion: ", anchor="w")
label_conversion.grid(row=4, column=0, columnspan=4, sticky="w", padx=10)

# Run the customtkinter event loop
root.mainloop()