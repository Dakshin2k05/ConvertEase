import customtkinter as ctk
import subprocess
from tkinter import messagebox
from PIL import Image, ImageTk

def run():
    root.destroy()
    subprocess.run(['python', '/Users/dakshin/Documents/TERM-3/project python/menu1.py'])


# Conversion factors (relative to Bit per second)
conversion_factors = {
    "Bit per second": 1,
    "Kilobit per second": 1e3,
    "Kilobyte per second": 8e3,
    "Kibibit per second": 1024,
    "Megabit per second": 1e6,
    "Megabyte per second": 8e6,
    "Mebibit per second": 1024**2,
    "Gigabit per second": 1e9,
    "Gigabyte per second": 8e9,
    "Gibibit per second": 1024**3,
    "Terabit per second": 1e12,
    "Terabyte per second": 8e12,
    "Tebibit per second": 1024**4
}

# Function to perform the conversion
def convert_rate():
    try:
        # Get the input value, input type, and output type
        input_value = float(entry_input.get())
        input_unit = combo_input.get()
        output_unit = combo_output.get()

        # Convert the input value to bits per second (base unit)
        value_in_bits = input_value * conversion_factors[input_unit]

        # Convert from bits per second to the desired output unit
        converted_value = value_in_bits / conversion_factors[output_unit]

        # Display the result in the output entry field
        entry_output.delete(0, ctk.END)
        entry_output.insert(0, str(round(converted_value, 5)))  # Round to 5 decimal places

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

# Function to refresh all fields
def refresh_fields():
    combo_input.set("Bit per second")  # Reset input combo box to default
    combo_output.set("Megabyte per second")  # Reset output combo box to default
    entry_input.delete(0, ctk.END)  # Clear input entry field
    entry_output.delete(0, ctk.END)  # Clear output entry field

# Create the main window using customtkinter
ctk.set_appearance_mode("dark-blue")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (default), "green", "dark-blue"

root = ctk.CTk()  # Use CTk instead of Tk
root.title("Data Transfer Rate Converter")
root.geometry('1000x800')

# Resize the logo image using PIL and display it on the left
logo_image = Image.open("Background images/data tranferbg.png")  # Path to the logo image
logo_image = logo_image.resize((1000, 800), Image.Resampling.LANCZOS)  # Resize the image to 1000x600 pixels
logo_photo = ImageTk.PhotoImage(logo_image)
# Display the resized logo
logo_label = ctk.CTkLabel(root, image=logo_photo)
logo_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Frame
frame = ctk.CTkFrame(root, width=900, height=575, corner_radius=10, fg_color='black')
frame.pack(padx=10, pady=150)

data_transfer = ["Bit per second", "Kilobit per second", "Kilobyte per second", "Kibibit per second", "Megabit per second",
                 "Megabyte per second", "Mebibit per second", "Gigabit per second", "Gigabyte per second", "Gibibit per second",
                 "Terabit per second", "Terabyte per second", "Tebibit per second"]

# Label
label = ctk.CTkLabel(frame, text="Data Transfer Rate", font=("Helvetica", 30, 'bold'))
label.grid(column=2, row=0, pady=40)

# Input Section
input_label = ctk.CTkLabel(frame, text="Input Type")
input_label.grid(row=1, column=0, padx=10, pady=10)

combo_input = ctk.CTkComboBox(frame, values=data_transfer, state="readonly")
combo_input.grid(row=1, column=1, padx=10, pady=10)
combo_input.set("Bit per second")  # Default to Bit per second

entry_input_label = ctk.CTkLabel(frame, text="Input Value")
entry_input_label.grid(row=2, column=0, padx=10, pady=10)

entry_input = ctk.CTkEntry(frame)
entry_input.grid(row=2, column=1, padx=10, pady=10)

# Button to perform the conversion
convert_button = ctk.CTkButton(frame, text="Convert", font=("Helvetica", 15), command=convert_rate)
convert_button.grid(row=1, column=2, rowspan=2, pady=10)

# Output Section
output_label = ctk.CTkLabel(frame, text="Output Type")
output_label.grid(row=1, column=3, padx=10, pady=10)

combo_output = ctk.CTkComboBox(frame, values=data_transfer, state="readonly")
combo_output.grid(row=1, column=4, padx=10, pady=10)
combo_output.set("Megabyte per second")

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