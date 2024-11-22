import subprocess
import customtkinter as ctk
from PIL import Image, ImageTk

#getstarted button command function
def getstart():
    root.destroy()
    subprocess.run(['python', 'login.py'])

root = ctk.CTk()
root.title('ConvertEase')
root.geometry('1000x800')

#background image
bg_image = Image.open("Background images/homebg.png")
bg_image = bg_image.resize((1000, 800), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(bg_image)
ph_label = ctk.CTkLabel(root, image=photo)
ph_label.place(relx=0.5, rely=0.5, anchor='center')

#frame
frame = ctk.CTkFrame(root, width=500, height=500, corner_radius=0,border_width=10,border_color='#00008B',fg_color="#030303")
frame.pack(side='top', anchor='center', pady=100)

#titles
title0 = ctk.CTkLabel(frame, text="WELCOME", font=("Helvetica", 90),text_color="LightCyan2", justify="center")
title1 = ctk.CTkLabel(frame, text="TO", font=("Helvetica", 90),text_color="LightCyan2", justify="center")
title2 = ctk.CTkLabel(frame, text="ConvertEase", font=("Helvetica", 90,'bold'), text_color="LightCyan2", justify="center")
title3 = ctk.CTkLabel(frame, text="Effortless. Accurate. Fast.", font=("Helvetica", 40),
                      text_color="LightCyan2", justify="center")
title0.grid(column=0, row=0, pady=10, padx=60)
title1.grid(column=0, row=1, pady=10, padx=60)
title2.grid(column=0, row=2, pady=0,padx=60)
title3.grid(column=0, row=3, pady=5)

#button
started = ctk.CTkButton(frame, text="Get started", font=("Helvetica", 30), command=getstart,
                        corner_radius=20,fg_color='#00008B',hover_color=('#00008B','#1E90FF'))
started.grid(column=0, row=4, pady=20)

root.mainloop()