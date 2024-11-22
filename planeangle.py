import subprocess
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

# Conversion factors for plane angle units (relative to Radian)
angle_factors = {
    "Arcsecond": 4.84813681109536e-6,  # 1 arcsecond = 4.84813681109536 × 10^-6 radians
    "Degree": 0.017453292519943,  # 1 degree = π / 180 radians
    "Gradian": 0.015707963267949,  # 1 gradian = π / 200 radians
    "Milliradian": 0.001,  # 1 milliradian = 0.001 radians
    "Minute of arc": 0.0002908882086657216,  # 1 arcminute = 1/60 of a degree = π / 10800 radians
    "Radian": 1  # Base unit
}

# Function to perform the conversion
def convert_angle():
    try:
        input_value = float(entry_input.get())  # Get input value
        input_unit = combo_input.get()  # Get input unit
        output_unit = combo_output.get()  # Get output unit

        # Convert input to Radian (base unit)
        radian_value = input_value * angle_factors[input_unit]

        # Convert from Radian to the desired output unit
        converted_value = radian_value / angle_factors[output_unit]

        # Display the converted value
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, str(round(converted_value, 6)))

        # Display formula and conversion explanation
        label_formula.configure(text=f"Formula: {input_value} {input_unit} = {converted_value:.6f} {output_unit}")
        label_conversion.configure(
            text=f"Conversion: {input_value} {input_unit} → {converted_value:.6f} {output_unit}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for angle input.")

# Function to refresh the input and output fields
def refresh_fields():
    entry_input.delete(0, ctk.END)
    entry_output.delete(0, ctk.END)
    combo_input.set("Radian")
    combo_output.set("Degree")
    label_formula.configure(text="Formula: ")
    label_conversion.configure(text="Conversion: ")

# Function to exit and run the next file
def run():
    root.destroy()
    subprocess.run(['python', 'menu1.py'])

# Create the main window using customtkinter
ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue", "green", "dark-blue"

root = ctk.CTk()  # Use CTk instead of Tk
root.title("Plane Angle Converter")
root.geometry('1000x800')

# Resize the logo image using PIL and display it on the left
logo_image = Image.open("Background images/planebg.png")  # Adjust this path
logo_image = logo_image.resize((1000, 800), Image.Resampling.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

# Display the resized logo
logo_label = ctk.CTkLabel(root, image=logo_photo)
logo_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Frame with a distinct color
frame = ctk.CTkFrame(root, width=900, height=575, corner_radius=10, fg_color="#660066")  # Custom purple color
frame.pack(padx=10, pady=150)

# Label
label = ctk.CTkLabel(frame, text="Plane Angle Converter", font=("Helvetica", 30, 'bold'), text_color="white")
label.grid(column=2, row=0, pady=40)

# Angle units
angle_units = ["Arcsecond", "Degree", "Gradian", "Milliradian", "Minute of arc", "Radian"]

# Input Section
input_type_label = ctk.CTkLabel(frame, text="Input Type", text_color="white")
input_type_label.grid(row=1, column=0, padx=20, pady=10)

combo_input = ctk.CTkComboBox(frame, values=angle_units, state="readonly", button_color="#9900cc")
combo_input.grid(row=1, column=1, padx=10, pady=10)
combo_input.set("Radian")

input_label = ctk.CTkLabel(frame, text="Input Angle:", text_color="white")
input_label.grid(row=2, column=0, padx=10, pady=10)

entry_input = ctk.CTkEntry(frame)
entry_input.grid(row=2, column=1, padx=10, pady=10)

# Button to perform the conversion
convert_button = ctk.CTkButton(frame, text="Convert", command=convert_angle, fg_color="#ff00ff")
convert_button.grid(row=1, column=2, rowspan=2, pady=10)

# Output Section
output_type_label = ctk.CTkLabel(frame, text="Output Type", text_color="white")
output_type_label.grid(row=1, column=3, padx=10, pady=10)

combo_output = ctk.CTkComboBox(frame, values=angle_units, state="readonly", button_color="#9900cc")
combo_output.grid(row=1, column=4, padx=20, pady=10)
combo_output.set("Degree")

output_label = ctk.CTkLabel(frame, text="Output Angle:", text_color="white")
output_label.grid(row=2, column=3, padx=10, pady=10)

entry_output = ctk.CTkEntry(frame)
entry_output.grid(row=2, column=4, padx=10, pady=10)

# Labels to display the formula and conversion explanation
label_formula = ctk.CTkLabel(frame, text="Formula: ", anchor="w", text_color="white")
label_formula.grid(row=3, column=0, columnspan=4, sticky="w", padx=10)

label_conversion = ctk.CTkLabel(frame, text="Conversion: ", anchor="w", text_color="white")
label_conversion.grid(row=4, column=0, columnspan=4, sticky="w", padx=10)

# Refresh button
refresh_button = ctk.CTkButton(frame, text="Refresh", command=refresh_fields, fg_color="#4d0099")
refresh_button.grid(row=5, column=1, columnspan=2, padx=10)

# Exit button
exit_button = ctk.CTkButton(frame, text="Exit", command=run, fg_color="#cc0000")
exit_button.grid(row=5, column=2, padx=20, pady=50, columnspan=3)

# Run the customtkinter event loop
root.mainloop()