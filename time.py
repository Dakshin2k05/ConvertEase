import subprocess
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

# Conversion factors for time units (relative to 1 second)
time_conversion_factors = {
    "Nanosecond": 1e9,
    "Microsecond": 1e6,
    "Millisecond": 1e3,
    "Second": 1,
    "Minute": 1 / 60,
    "Hour": 1 / 3600,
    "Day": 1 / 86400,
    "Week": 1 / (86400 * 7),
    "Month": 1 / (86400 * 30.44),  # Approximate
    "Calendar year": 1 / (86400 * 365.25),  # Approximate
    "Decade": 1 / (86400 * 365.25 * 10),  # Approximate
    "Century": 1 / (86400 * 365.25 * 100)  # Approximate
}

# Function to perform the time conversion
def convert_time():
    try:
        input_value = float(entry_input.get())  # Get input value
        input_unit = combo_input.get()  # Get input unit
        output_unit = combo_output.get()  # Get output unit

        # Convert input to seconds
        seconds = input_value / time_conversion_factors[input_unit]

        # Convert seconds to the output unit
        converted_value = seconds * time_conversion_factors[output_unit]

        # Display the converted value
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, str(round(converted_value, 6)))

        # Display the formula
        label_formula.configure(
            text=f"Formula: {input_value} {input_unit} → {converted_value:.6f} {output_unit}"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for time conversion.")

# Function to refresh the input and output fields
def refresh_fields():
    entry_input.delete(0, ctk.END)
    entry_output.delete(0, ctk.END)
    combo_input.set("Second")
    combo_output.set("Minute")
    label_formula.configure(text="Formula:")

# Function to exit and run the next file
def run():
    root.destroy()
    subprocess.run(['python', 'menu1.py'])

# Create the main window using customtkinter
ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue", "green", "dark-blue"

root = ctk.CTk()  # Use CTk instead of Tk
root.title("Time Converter")
root.geometry('1000x800')

# Resize the logo image using PIL and display it on the left
logo_image = Image.open("Background images/time.png")  # Adjust this path
logo_image = logo_image.resize((1000, 800), Image.Resampling.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

# Display the resized logo
logo_label = ctk.CTkLabel(root, image=logo_photo)
logo_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Frame with a distinct color
frame = ctk.CTkFrame(root, width=900, height=575, corner_radius=10, fg_color="#001f3f")  # Dark blue color
frame.pack(padx=10, pady=150)

# Label
label = ctk.CTkLabel(frame, text="Time Converter", font=("Helvetica", 30, 'bold'), text_color="white")
label.grid(column=2, row=0, pady=40)

# Time units
time_units = [
    "Nanosecond", "Microsecond", "Millisecond", "Second", "Minute",
    "Hour", "Day", "Week", "Month", "Calendar year", "Decade", "Century"
]

# Input Section
input_type_label = ctk.CTkLabel(frame, text="Input Unit", text_color="white")
input_type_label.grid(row=1, column=0, padx=20, pady=10)

combo_input = ctk.CTkComboBox(frame, values=time_units, state="readonly", button_color="#003f7f")
combo_input.grid(row=1, column=1, padx=10, pady=10)
combo_input.set("Second")

input_label = ctk.CTkLabel(frame, text="Input Time:", text_color="white")
input_label.grid(row=2, column=0, padx=10, pady=10)

entry_input = ctk.CTkEntry(frame)
entry_input.grid(row=2, column=1, padx=10, pady=10)

# Button to perform the conversion
convert_button = ctk.CTkButton(frame, text="Convert", command=convert_time, fg_color="#0055aa")
convert_button.grid(row=1, column=2, rowspan=2, pady=10)

# Output Section
output_type_label = ctk.CTkLabel(frame, text="Output Unit", text_color="white")
output_type_label.grid(row=1, column=3, padx=10, pady=10)

combo_output = ctk.CTkComboBox(frame, values=time_units, state="readonly", button_color="#003f7f")
combo_output.grid(row=1, column=4, padx=20, pady=10)
combo_output.set("Minute")

output_label = ctk.CTkLabel(frame, text="Output Time:", text_color="white")
output_label.grid(row=2, column=3, padx=10, pady=10)

entry_output = ctk.CTkEntry(frame)
entry_output.grid(row=2, column=4, padx=10, pady=10)

# Label to display the formula
label_formula = ctk.CTkLabel(frame, text="Formula:", anchor="w", text_color="white", wraplength=800)
label_formula.grid(row=3, column=0, columnspan=5, sticky="w", padx=10, pady=20)

# Refresh button
refresh_button = ctk.CTkButton(frame, text="Refresh", command=refresh_fields, fg_color="#0066cc")
refresh_button.grid(row=4, column=1, columnspan=2, padx=10)

# Exit button
exit_button = ctk.CTkButton(frame, text="Exit", command=run, fg_color="#990000")
exit_button.grid(row=4, column=2, padx=20, pady=50, columnspan=3)

# Run the customtkinter event loop
root.mainloop()