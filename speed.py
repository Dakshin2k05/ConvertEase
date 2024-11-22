import subprocess
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

# Conversion factors for speed units (relative to Meter per Second)
speed_factors = {
    "Mile per hour": 0.44704,  # 1 mile per hour = 0.44704 m/s
    "Foot per second": 0.3048,  # 1 foot per second = 0.3048 m/s
    "Metre per second": 1,  # Base unit
    "Kilometre per hour": 0.277778,  # 1 km/h = 0.277778 m/s
    "Knot": 0.514444  # 1 knot = 0.514444 m/s
}

# Function to perform the conversion
def convert_speed():
    try:
        input_value = float(entry_input.get())  # Get input value
        input_unit = combo_input.get()  # Get input unit
        output_unit = combo_output.get()  # Get output unit

        # Convert input to Meter per Second (base unit)
        mps_value = input_value * speed_factors[input_unit]

        # Convert from Meter per Second to the desired output unit
        converted_value = mps_value / speed_factors[output_unit]

        # Display the converted value
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, str(round(converted_value, 6)))

        # Display formula and conversion explanation
        label_formula.configure(text=f"Formula: {input_value} {input_unit} = {converted_value:.6f} {output_unit}")
        label_conversion.configure(
            text=f"Conversion: {input_value} {input_unit} → {converted_value:.6f} {output_unit}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for speed input.")

# Function to refresh the input and output fields
def refresh_fields():
    entry_input.delete(0, ctk.END)
    entry_output.delete(0, ctk.END)
    combo_input.set("Metre per second")
    combo_output.set("Kilometre per hour")
    label_formula.configure(text="Formula: ")
    label_conversion.configure(text="Conversion: ")

# Function to exit and run the next file
def run():
    root.destroy()
    subprocess.run(['python', 'menu1.py'])

# Create the main window using customtkinter
ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

root = ctk.CTk()  # Use CTk instead of Tk
root.title("Speed Converter")
root.geometry('1000x800')

# Resize the logo image using PIL and display it on the left
logo_image = Image.open("Background images/speedbg.png")  # Adjust this path
logo_image = logo_image.resize((1000, 800), Image.Resampling.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

# Display the resized logo
logo_label = ctk.CTkLabel(root, image=logo_photo)
logo_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Frame
frame = ctk.CTkFrame(root, width=900, height=575, corner_radius=10)
frame.pack(padx=10, pady=150)

# Label
label = ctk.CTkLabel(frame, text="Speed Converter", font=("Helvetica", 30, 'bold'))
label.grid(column=2, row=0, pady=40)

# Speed units
speed_units = ["Mile per hour", "Foot per second", "Metre per second", "Kilometre per hour", "Knot"]

# Input Section
input_type_label = ctk.CTkLabel(frame, text="Input Type")
input_type_label.grid(row=1, column=0, padx=20, pady=10)

combo_input = ctk.CTkComboBox(frame, values=speed_units, state="readonly")
combo_input.grid(row=1, column=1, padx=10, pady=10)
combo_input.set("Metre per second")

input_label = ctk.CTkLabel(frame, text="Input Speed:")
input_label.grid(row=2, column=0, padx=10, pady=10)

entry_input = ctk.CTkEntry(frame)
entry_input.grid(row=2, column=1, padx=10, pady=10)

# Button to perform the conversion
convert_button = ctk.CTkButton(frame, text="Convert", command=convert_speed)
convert_button.grid(row=1, column=2, rowspan=2, pady=10)

# Output Section
output_type_label = ctk.CTkLabel(frame, text="Output Type")
output_type_label.grid(row=1, column=3, padx=10, pady=10)

combo_output = ctk.CTkComboBox(frame, values=speed_units, state="readonly")
combo_output.grid(row=1, column=4, padx=20, pady=10)
combo_output.set("Kilometre per hour")

output_label = ctk.CTkLabel(frame, text="Output Speed:")
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