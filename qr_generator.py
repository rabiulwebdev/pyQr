import tkinter as tk
from tkinter import filedialog, messagebox

import qrcode
from PIL import Image, ImageTk


def generate_qr():
    data = entry.get()
    if not data.strip():
        messagebox.showwarning("Input Error", "Please enter text, link, or number!")
        return
    
    # Generate QR code
    qr = qrcode.make(data)
    
    # Save temporary QR
    qr.save("temp_qr.png")

    # Display QR in GUI
    img = Image.open("temp_qr.png")
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

def save_qr():
    if qr_label.image is None:
        messagebox.showwarning("No QR", "Please generate a QR code first!")
        return
    
    filepath = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG files", "*.png")])
    if filepath:
        qr = qrcode.make(entry.get())
        qr.save(filepath)
        messagebox.showinfo("Saved", f"QR Code saved as {filepath}")

# GUI Setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")

tk.Label(root, text="Enter Text / Link / Number:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Generate QR", command=generate_qr, bg="blue", fg="white", font=("Arial", 12)).pack(pady=10)
tk.Button(root, text="Save QR", command=save_qr, bg="green", fg="white", font=("Arial", 12)).pack(pady=5)

qr_label = tk.Label(root)
qr_label.pack(pady=20)

root.mainloop()
