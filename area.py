import subprocess
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

area_factors = {
    "Square kilometre": 1_000_000,
    "Square metre": 1,  # Base unit
    "Square mile": 2_589_988.11,  # 1 square mile = 2,589,988.11 square meters
    "Square yard": 0.836127,  # 1 square yard = 0.836127 square meters
    "Square foot": 0.092903,  # 1 square foot = 0.092903 square meters
    "Square inch": 0.00064516,  # 1 square inch = 0.00064516 square meters
    "Hectare": 10_000,  # 1 hectare = 10,000 square meters
    "Acre": 4_046.8564224  # 1 acre = 4,046.8564224 square meters
}
def convert_area():
    try:
        input_value = float(entry_input.get())
        input_unit = combo_input.get()
        output_unit = combo_output.get()
        square_meter_value = input_value * area_factors[input_unit]
        converted_value = square_meter_value / area_factors[output_unit]

        # Display the converted value
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, str(round(converted_value, 6)))

        # Display formula and conversion explanation
        label_formula.configure(text=f"Formula: {input_value} {input_unit} = {converted_value:.6f} {output_unit}")
        label_conversion.configure(
            text=f"Conversion: {input_value} {input_unit} → {converted_value:.6f} {output_unit}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for area input.")

# Function to refresh the input and output fields
def refresh_fields():
    entry_input.delete(0, ctk.END)
    entry_output.delete(0, ctk.END)
    combo_input.set("Square metre")
    combo_output.set("Square foot")
    label_formula.configure(text="Formula: ")
    label_conversion.configure(text="Conversion: ")

# Function to exit and run the next file
def run():
    root.destroy()
    subprocess.run(['python', 'menu1.py'])

# Create the main window using customtkinter
ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("green")  # Themes: "blue", "green", "dark-blue"

root = ctk.CTk()  # Use CTk instead of Tk
root.title("Area Converter")
root.geometry('1000x800')

# Resize the logo image using PIL and display it on the left
logo_image = Image.open("Background images/areabg.png")  # Adjust this path
logo_image = logo_image.resize((1000, 800), Image.Resampling.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

# Display the resized logo
logo_label = ctk.CTkLabel(root, image=logo_photo)
logo_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Frame with a different color
frame = ctk.CTkFrame(root, width=900, height=575, corner_radius=10, fg_color="darkolivegreen2")  # Custom color for the frame
frame.pack(padx=10, pady=150)

# Label
label = ctk.CTkLabel(frame, text="Area Converter", font=("Helvetica", 30, 'bold'), text_color="white")
label.grid(column=2, row=0, pady=40)

# Area units
area_units = ["Square kilometre", "Square metre", "Square mile", "Square yard", "Square foot",
              "Square inch", "Hectare", "Acre"]

# Input Section
input_type_label = ctk.CTkLabel(frame, text="Input Type", text_color="white")
input_type_label.grid(row=1, column=0, padx=20, pady=10)

combo_input = ctk.CTkComboBox(frame, values=area_units, state="readonly", button_color="#00cc66")
combo_input.grid(row=1, column=1, padx=10, pady=10)
combo_input.set("Square metre")

input_label = ctk.CTkLabel(frame, text="Input Area:", text_color="white")
input_label.grid(row=2, column=0, padx=10, pady=10)

entry_input = ctk.CTkEntry(frame)
entry_input.grid(row=2, column=1, padx=10, pady=10)

# Button to perform the conversion
convert_button = ctk.CTkButton(frame, text="Convert", command=convert_area, fg_color="#ff6600")
convert_button.grid(row=1, column=2, rowspan=2, pady=10)

# Output Section
output_type_label = ctk.CTkLabel(frame, text="Output Type", text_color="white")
output_type_label.grid(row=1, column=3, padx=10, pady=10)

combo_output = ctk.CTkComboBox(frame, values=area_units, state="readonly", button_color="#00cc66")
combo_output.grid(row=1, column=4, padx=20, pady=10)
combo_output.set("Square foot")

output_label = ctk.CTkLabel(frame, text="Output Area:", text_color="white")
output_label.grid(row=2, column=3, padx=10, pady=10)

entry_output = ctk.CTkEntry(frame)
entry_output.grid(row=2, column=4, padx=10, pady=10)

# Labels to display the formula and conversion explanation
label_formula = ctk.CTkLabel(frame, text="Formula: ", anchor="w", text_color="white")
label_formula.grid(row=3, column=0, columnspan=4, sticky="w", padx=10)

label_conversion = ctk.CTkLabel(frame, text="Conversion: ", anchor="w", text_color="white")
label_conversion.grid(row=4, column=0, columnspan=4, sticky="w", padx=10)

# Refresh button
refresh_button = ctk.CTkButton(frame, text="Refresh", command=refresh_fields, fg_color="#0073e6")
refresh_button.grid(row=5, column=1, columnspan=2, padx=10)

# Exit button
exit_button = ctk.CTkButton(frame, text="Exit", command=run, fg_color="#ff1a1a")
exit_button.grid(row=5, column=2, padx=20, pady=50, columnspan=3)

# Run the customtkinter event loop
root.mainloop()