import customtkinter as ctk
import subprocess
from PIL import Image, ImageTk

# Initialize the custom tkinter settings
ctk.set_appearance_mode("dark")  # Modes: "light", "dark", "system"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue", "dark-blue", "green"

root = ctk.CTk()  # Use CTk instead of Tk()
root.geometry('1000x800')
root.title("Main Menu")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.configure(bg='bisque4')


# Resize the logo image using PIL and display it on the left
logo_image = Image.open("Background images/encrypbg.png")  # Path to the logo image
logo_image = logo_image.resize((1000, 800), Image.Resampling.LANCZOS)  # Resize the image to 1000x600 pixels
logo_photo = ImageTk.PhotoImage(logo_image)

# Display the resized logo
logo_label = ctk.CTkLabel(root, image=logo_photo, bg_color='white')
logo_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Function to open the currency converter
def run1():
    root.destroy()
    subprocess.run(['python','encrypter.py'])

# Function to open the temperature converter
def run2():
    root.destroy()
    subprocess.run(['python', 'decrypt.py'])

# Function to logout and return to login screen
def logout():
    root.destroy()
    subprocess.run(['python', 'menu1.py'])

# Creating a frame with the color 'darkseagreen4'
frame = ctk.CTkFrame(root, width=900, height=600, fg_color='#030303')
frame.grid(column=0, row=0, padx=0, pady=60, columnspan=2)


# Creating label of main menu inside the frame
w = ctk.CTkLabel(frame, text='MAIN MENU', font=ctk.CTkFont(size=50, weight="bold"), bg_color='#030303', text_color='white')
w.grid(column=0, row=0, pady=30, padx=0, columnspan=2)

# Creating buttons inside the frame
button1_Currency = ctk.CTkButton(frame, text='Encrypt text', width=400, height=50, font=ctk.CTkFont(size=25, weight="bold"), text_color='white',fg_color="#030303",hover_color="#363636",command=run1)
button2_temperature = ctk.CTkButton(frame, text='Decrypt text', width=400, height=50, font=ctk.CTkFont(size=25, weight="bold"), text_color='white',fg_color="#030303",hover_color="#363636",command=run2)
button15_logout = ctk.CTkButton(frame, text='Exit', width=400, height=50, font=ctk.CTkFont(size=25, weight="bold"), text_color='white',fg_color="#030303",hover_color="#363636",command=logout)

# Use of grid layout for buttons inside the frame
button1_Currency.grid(column=0, row=1, pady=15,padx=30)
button2_temperature.grid(column=0, row=2, pady=15)
button15_logout.grid(column=0, row=5, pady=15)

root.mainloop()