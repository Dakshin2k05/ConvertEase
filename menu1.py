import customtkinter as ctk
import subprocess
from PIL import Image, ImageTk
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")
root = ctk.CTk()
root.geometry('1000x800')
root.title("Main Menu")
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.configure(bg='bisque4')
logo_image = Image.open("Background images/menubarbg.png")
logo_image = logo_image.resize((1000, 800), Image.Resampling.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)
logo_label = ctk.CTkLabel(root, image=logo_photo, bg_color='white')
logo_label.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
def Currency():
    root.destroy()
    subprocess.run(['python','currency coverter.py'])
def run2():
    root.destroy()
    subprocess.run(['python', 'temperature converter.py'])
def run3():
    root.destroy()
    subprocess.run(['python', 'mass and weight converter.py'])
def run4():
    root.destroy()
    subprocess.run(['python', 'digital storage.py'])
def run5():
    root.destroy()
    subprocess.run(['python', 'Energy.py'])
def run6():
    root.destroy()
    subprocess.run(['python', 'fuel economy.py'])
def run7():
    root.destroy()
    subprocess.run(['python', 'volume.py'])
def run8():
    root.destroy()
    subprocess.run(['python', 'encrptmenu.py'])
def run9():
    root.destroy()
    subprocess.run(['python', 'speed.py'])
def run10():
    root.destroy()
    subprocess.run(['python', 'area.py'])
def run11():
    root.destroy()
    subprocess.run(['python', 'planeangle.py'])
def run12():
    root.destroy()
    subprocess.run(['python', 'base.py'])
def run13():
    root.destroy()
    subprocess.run(['python', 'time.py'])
def logout():
    root.destroy()
    subprocess.run(['python', 'login.py'])
frame = ctk.CTkFrame(root, width=900, height=600, fg_color='#030303')
frame.grid(column=0, row=0, padx=0, pady=60, columnspan=2)
w = ctk.CTkLabel(frame, text='MAIN MENU', font=ctk.CTkFont(size=50, weight="bold"), bg_color='#030303', text_color='white')
w.grid(column=0, row=0, pady=30, padx=0, columnspan=2)
button1_Currency = ctk.CTkButton(frame, text='Currency Converter', width=400, height=50, font=ctk.CTkFont(size=25, weight="bold"), text_color='gray5',fg_color="#B5B5B5",command=Currency)
button2_temperature = ctk.CTkButton(frame, text='Temperature Converter', width=400, height=50, font=ctk.CTkFont(size=25, weight="bold"), text_color='gray5',fg_color="#B5B5B5",command=run2)
button3_weightmass = ctk.CTkButton(frame, text='Weight and Mass Converter', width=400, height=50, font=ctk.CTkFont(size=25, weight="bold"), text_color='gray5',fg_color="#B5B5B5", command=run3)
button4_volume = ctk.CTkButton(frame, text='Volume Converter', width=400, height=50, font=ctk.CTkFont(size=25, weight="bold"), text_color='gray5',fg_color="#B5B5B5",command=run7)
button5_speed = ctk.CTkButton(frame, text='Speed Converter', width=400, height=50, font=ctk.CTkFont(size=25, weight="bold"), text_color='gray5',fg_color="#B5B5B5",command=run9)
button6_encrypt = ctk.CTkButton(frame, text='Encrypter/Decrypter', width=400, height=50, font=ctk.CTkFont(size=25, weight="bold"), text_color='gray5',fg_color="#B5B5B5",command=run8)
button7_area = ctk.CTkButton(frame, text='Area Converter', width=400, height=50, font=ctk.CTkFont(size=25, weight="bold"), text_color='gray5',fg_color="#B5B5B5",command=run10)
button8_DataTransferRate = ctk.CTkButton(frame, text='Data Transfer Rate', width=400, height=50, font=ctk.CTkFont(size=25, weight="bold"), text_color='gray5',fg_color="#B5B5B5")
button9_DigitalStorage = ctk.CTkButton(frame, text='Digital Storage', width=400, height=50, font=ctk.CTkFont(size=25, weight="bold"), text_color='gray5',command=run4,fg_color="#B5B5B5")
button10_energy = ctk.CTkButton(frame, text='Energy Converter', width=400, height=50, font=ctk.CTkFont(size=25, weight="bold"), text_color='gray5',command=run5,fg_color="#B5B5B5")
button11_FuelEconomy = ctk.CTkButton(frame, text='Fuel Economy Calculator', width=400, height=50, font=ctk.CTkFont(size=25, weight="bold"), text_color='gray5',fg_color="#B5B5B5",command=run6)
button12_PlaneAngle = ctk.CTkButton(frame, text='Plane Angle Converter', width=400, height=50, font=ctk.CTkFont(size=25, weight="bold"), text_color='gray5',fg_color="#B5B5B5",command=run11)
button13_BaseConverter = ctk.CTkButton(frame, text='Base Converter', width=400, height=50, font=ctk.CTkFont(size=25, weight="bold"), text_color='gray5',fg_color="#B5B5B5",command=run12)
button14_timeconverter = ctk.CTkButton(frame, text='Time Converter', width=400, height=50, font=ctk.CTkFont(size=25, weight="bold"), text_color='gray5',fg_color="#B5B5B5",command=run13)
button15_logout = ctk.CTkButton(frame, text='Logout', width=400, height=50, font=ctk.CTkFont(size=25, weight="bold"), text_color='gray5',fg_color="#B5B5B5", command=logout)
button1_Currency.grid(column=0, row=1, pady=5,padx=30)
button2_temperature.grid(column=0, row=2, pady=5)
button3_weightmass.grid(column=0, row=3, pady=5)
button4_volume.grid(column=0, row=4, pady=5)
button5_speed.grid(column=0, row=5, pady=5)
button6_encrypt.grid(column=0, row=6, pady=5)
button7_area.grid(column=0, row=7, pady=5)
button8_DataTransferRate.grid(column=1, row=1, pady=5)
button9_DigitalStorage.grid(column=1, row=2, pady=5)
button10_energy.grid(column=1, row=3, pady=5)
button11_FuelEconomy.grid(column=1, row=4, pady=5)
button12_PlaneAngle.grid(column=1, row=5, pady=5)
button13_BaseConverter.grid(column=1, row=6, pady=5)
button14_timeconverter.grid(column=1, row=7, pady=5,padx=30)
button15_logout.grid(column=0, row=8, pady=30, columnspan=2)

root.mainloop()