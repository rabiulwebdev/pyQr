import tkinter as tk
from tkinter import filedialog, messagebox

import pyfiglet
import qrcode
from colorama import Fore, Style
from PIL import Image, ImageTk


# ------------------ CLI Mode ------------------
def cli_banner():
    print(Fore.CYAN + pyfiglet.figlet_format("QR Generator"))
    print(Fore.YELLOW + "Created by: rabiulwebdev")
    print(Fore.GREEN + "Generate QR codes easily from text, numbers, or links\n" + Style.RESET_ALL)


def cli_generate_qr(data, filename="qr.png"):
    qr = qrcode.make(data)
    qr.save(filename)
    print(Fore.GREEN + f"[+] QR Code saved as {filename}" + Style.RESET_ALL)


def cli_mode():
    cli_banner()
    while True:
        print(Fore.CYAN + "\n[1] Generate QR Code")
        print("[2] Exit" + Style.RESET_ALL)
        choice = input(Fore.YELLOW + "\nEnter choice: " + Style.RESET_ALL)

        if choice == "1":
            data = input(Fore.WHITE + "Enter text/link/number: " + Style.RESET_ALL)
            filename = input(Fore.WHITE + "Enter filename (default: qr.png): " + Style.RESET_ALL) or "qr.png"
            cli_generate_qr(data, filename)
        elif choice == "2":
            print(Fore.RED + "Exiting... Goodbye!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice! Try again." + Style.RESET_ALL)


# ------------------ GUI Mode ------------------
def gui_generate_qr():
    data = entry.get()
    if not data.strip():
        messagebox.showwarning("Input Error", "Please enter text, link, or number!")
        return

    qr = qrcode.make(data)
    qr.save("temp_qr.png")

    img = Image.open("temp_qr.png").resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk


def gui_save_qr():
    if qr_label.image is None:
        messagebox.showwarning("No QR", "Please generate a QR code first!")
        return

    filepath = filedialog.asksaveasfilename(defaultextension=".png",
                                            filetypes=[("PNG files", "*.png")])
    if filepath:
        qr = qrcode.make(entry.get())
        qr.save(filepath)
        messagebox.showinfo("Saved", f"QR Code saved as {filepath}")


def gui_mode():
    global entry, qr_label
    root = tk.Tk()
    root.title("QR Code Generator")
    root.geometry("400x500")

    tk.Label(root, text="Enter Text / Link / Number:", font=("Arial", 12)).pack(pady=10)
    entry = tk.Entry(root, width=40, font=("Arial", 12))
    entry.pack(pady=5)

    tk.Button(root, text="Generate QR", command=gui_generate_qr,
              bg="blue", fg="white", font=("Arial", 12)).pack(pady=10)
    tk.Button(root, text="Save QR", command=gui_save_qr,
              bg="green", fg="white", font=("Arial", 12)).pack(pady=5)

    qr_label = tk.Label(root)
    qr_label.pack(pady=20)

    root.mainloop()


# ------------------ MAIN ------------------
if __name__ == "__main__":
    print(Fore.MAGENTA + "\nChoose mode:")
    print("[1] GUI Mode (Desktop App)")
    print("[2] CLI Mode (Terminal Tool)\n" + Style.RESET_ALL)
    mode = input(Fore.YELLOW + "Enter choice: " + Style.RESET_ALL)

    if mode == "1":
        gui_mode()
    elif mode == "2":
        cli_mode()
    else:
        print(Fore.RED + "Invalid choice! Exiting..." + Style.RESET_ALL)
        print(Fore.RED + "Invalid choice! Exiting..." + Style.RESET_ALL)
        print(Fore.RED + "Invalid choice! Exiting..." + Style.RESET_ALL)
