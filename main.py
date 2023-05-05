from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.title('Image Viewer')
root.geometry("400x450")
# root.iconbitmap('images/frankenstein.ico')

def showimage():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title = "Select image file", filetype=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All Files", "*.*")))
    img = Image.open(filename)
    # this is to resize the image as per the size of the canvas
    img = img.resize((350, 350), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img

frame =  Frame(root)
frame.pack(side="bottom", padx=15, pady=15)

lbl = Label(root)
lbl.pack()

btn = Button(frame, text="Select Image", command=showimage)
btn.pack(side="left")

btn2 = Button(frame, text="Exit", command=lambda:exit())
btn2.pack(side="left", padx=12)

root.mainloop()
