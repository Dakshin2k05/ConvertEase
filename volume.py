import customtkinter as ctk
import subprocess
from tkinter import messagebox
from PIL import Image, ImageTk

def run():
    root.destroy()
    subprocess.run(['python', 'menu1.py'])


# Conversion factors (relative to cubic meters)
conversion_factors = {
    "Cubic Meter (m³)": 1,
    "Liter (L)": 1000,
    "Milliliter (mL)": 1e6,
    "US Gallon": 264.172,
    "Imperial Gallon": 219.969,
    "US Quart": 1056.69,
    "Imperial Quart": 879.877,
    "US Pint": 2113.38,
    "Imperial Pint": 1759.75,
    "US Cup": 4226.75,
    "Imperial Cup": 3519.51,
    "US Fluid Ounce": 33814,
    "Imperial Fluid Ounce": 35195.1,
    "Cubic Foot (ft³)": 35.3147,
    "Cubic Inch (in³)": 61023.7
}


def convert_volume():
    try:
        input_value = float(entry_input.get())
        input_unit = combo_input.get()
        output_unit = combo_output.get()

        # Convert the input value to cubic meters (base unit)
        value_in_cubic_meters = input_value / conversion_factors[input_unit]

        # Convert from cubic meters to the desired output unit
        converted_value = value_in_cubic_meters * conversion_factors[output_unit]

        # Display the result
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, str(round(converted_value, 5)))  # Round to 5 decimal places

        # Display the formula
        label_formula.config(text=f"Formula: {input_value} {input_unit} = {round(converted_value, 5)} {output_unit}")
        label_conversion.config(
            text=f"Conversion: 1 {input_unit} = {round(conversion_factors[output_unit] / conversion_factors[input_unit], 5)} {output_unit}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")


# Function to refresh all fields
def refresh_fields():
    combo_input.set("Milliliter (mL)")  # Reset input combo box to default
    combo_output.set("Liter (L)")  # Reset output combo box to default
    entry_input.delete(0, ctk.END)  # Clear input entry field
    entry_output.delete(0, ctk.END)  # Clear output entry field
    label_formula.config(text="Formula: ")  # Reset formula label
    label_conversion.config(text="Conversion: ")  # Reset conversion label


# Create the main window using customtkinter
ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()  # Use CTk instead of Tk
root.title("Volume Converter")
root.geometry('1000x800')

# Resize the logo image using PIL and display it on the left
logo_image = Image.open("Background images/volumebg.png")  # Path to the logo image
logo_image = logo_image.resize((1000, 800), Image.Resampling.LANCZOS)  # Resize the image to 1000x600 pixels
logo_photo = ImageTk.PhotoImage(logo_image)
# Display the resized logo
logo_label = ctk.CTkLabel(root, image=logo_photo)
logo_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Frame
frame = ctk.CTkFrame(root, width=900, height=575, corner_radius=10, fg_color='black')
frame.pack(padx=10, pady=150)

volume_units = ["Cubic Meter (m³)", "Liter (L)", "Milliliter (mL)", "US Gallon", "Imperial Gallon", "US Quart",
                "Imperial Quart",
                "US Pint", "Imperial Pint", "US Cup", "Imperial Cup", "US Fluid Ounce", "Imperial Fluid Ounce",
                "Cubic Foot (ft³)", "Cubic Inch (in³)"]

# Label
label = ctk.CTkLabel(frame, text="Volume Converter", font=("Helvetica", 30, 'bold'))
label.grid(column=2, row=0, pady=40)

# Input Section
input_label = ctk.CTkLabel(frame, text="Input Type")
input_label.grid(row=1, column=0, padx=10, pady=10)

combo_input = ctk.CTkComboBox(frame, values=volume_units, state="readonly")
combo_input.grid(row=1, column=1, padx=10, pady=10)
combo_input.set("Milliliter (mL)")  # Default to Milliliter

entry_input_label = ctk.CTkLabel(frame, text="Input Volume")
entry_input_label.grid(row=2, column=0, padx=10, pady=10)

entry_input = ctk.CTkEntry(frame)
entry_input.grid(row=2, column=1, padx=10, pady=10)

# Button to perform the conversion
convert_button = ctk.CTkButton(frame, text="Convert", font=("Helvetica", 15), command=convert_volume)
convert_button.grid(row=1, column=2, rowspan=2, pady=10)

# Output Section
output_label = ctk.CTkLabel(frame, text="Output Type")
output_label.grid(row=1, column=3, padx=10, pady=10)

combo_output = ctk.CTkComboBox(frame, values=volume_units, state="readonly")
combo_output.grid(row=1, column=4, padx=10, pady=10)
combo_output.set("Liter (L)")

entry_output_label = ctk.CTkLabel(frame, text="Output Volume")
entry_output_label.grid(row=2, column=3, padx=10, pady=10)

entry_output = ctk.CTkEntry(frame)
entry_output.grid(row=2, column=4, padx=10, pady=10)

# Refresh button with linked function
refresh_button = ctk.CTkButton(frame, text="Refresh", font=("Helvetica", 15), command=refresh_fields)
refresh_button.grid(row=5, column=0, padx=20, pady=20, columnspan=2)

# Exit button
exit_button = ctk.CTkButton(frame, text="Exit", command=run)
exit_button.grid(row=5, column=3, padx=20, pady=50, columnspan=2)

# Labels to display the formula and conversion explanation
label_formula = ctk.CTkLabel(frame, text="Formula: ", anchor="w")
label_formula.grid(row=3, column=0, columnspan=4, sticky="w", padx=10)

label_conversion = ctk.CTkLabel(frame, text="Conversion: ", anchor="w")
label_conversion.grid(row=4, column=0, columnspan=4, sticky="w", padx=10)

root.mainloop()