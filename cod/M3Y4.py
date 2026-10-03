from customtkinter import *
from random import randint
from PIL import Image

def change_btn_pos():
    x_random = randint(0, win.winfo_width() - btn_no.winfo_width())
    y_random = randint(0, win.winfo_height() - btn_no.winfo_height())
    btn_no.place(x=x_random, y=y_random)

def show_win():
    win2 = CTk()
    win2.geometry('300x100')
    win2.title('Мої вітання')
    label_win = CTkLabel(win2, text='Твій iq висок', font=('Arial', 14, 'bold'))
    label_win.pack(pady=20)
    win2.mainloop()

win = CTk()
win.geometry('400x300')
win.title('Соціальне опитування')

image = Image.open('images (2).png')
image_ctk = CTkImage(light_image=image, size=(350, 200))
label_img = CTkLabel(win, text='', image=image_ctk)
label_img.pack(pady=100)

label = CTkLabel(win, text='Яке меню найкраще в кфс?', font=('Arial', 14, 'bold'))
label.pack(pady=40)

btn_no = CTkButton(win, text='Веган комбо (сміття)', command=change_btn_pos)
btn_no.place(x=50, y=200)
btn_no.configure(fg_color="#45c71a")
btn_yes = CTkButton(win, text='ФРЕНДС КОМБО ОРИГІНАЛЬНИЙ', command=show_win)
btn_yes.place(x=200, y=200)
btn_yes.configure(fg_color="#a83232")
win.mainloop()
