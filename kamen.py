from customtkinter import *

window = CTk ()
window.configure(fg_color="Lightgoldenrodyellow")
window.title("Kamen")
window.geometry("500x500")

text = CTkLabel(master=window,width=500,height=250, border_color="Mediumaquamarine", text="مرحبا بالعالم!", fg_color="Mediumspringgreen", bg_color="lightgoldenrodyellow")
text.pack()

window.mainloop()