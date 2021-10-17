import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
root.title("Image Converter")
container = tk.Canvas(root, width=300, height=250, bg='LightBlue', relief='raised')
container.pack()

label = tk.Label(root, text="Image Converter", bg='LightPink')
label.config(font=('Hack', 20))
container.create_window(150, 60, window=label)

def uploadImage():
    global image
    file_path = filedialog.askopenfilename()
    image = Image.open(file_path)
    tk.messagebox.showinfo("info", "Image uploaded sucessfully")

upload_btn = tk.Button(text="Select JPG Image", command=uploadImage, bg="MediumAquaMarine", fg='black', font=('Hack', 12))
container.create_window(150, 130, window=upload_btn)


def convertImage():
    global image
    export_path = filedialog.asksaveasfilename(defaultextension='.png')
    image.save(export_path)
    tk.messagebox.showinfo("info", "Image converted into PNG sucessfully")

save_btn = tk.Button(text="Save Image as PNG", command=convertImage, bg='MediumAquaMarine', fg='black', font=('Hack', 12))
container.create_window(150, 180, window=save_btn)
root.mainloop()
