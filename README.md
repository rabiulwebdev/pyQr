# QR Generator Tool  

A Python-based **QR Code Generator** that works in **two modes**:  
- 🖼️ **GUI Mode** → Desktop application with a simple interface (Tkinter).  
- 💻 **CLI Mode** → Terminal tool with a cool ASCII banner (like hacking tools).  

Easily convert any text, number, or link into a QR code, preview it, and save it as a PNG file.  

---

## ✨ Features
- Generate QR codes from text, numbers, or URLs.  
- Dual mode: **GUI (desktop)** or **CLI (terminal)**.  
- Save QR codes in PNG format.  
- Beautiful ASCII banner in CLI mode.  
- Works on **Linux, Termux, and Windows**.  

---

## ⚙️ Installation  

### 🐧 Linux (Ubuntu/Debian)
1. **Install dependencies & run**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-tk -y
pip install qrcode[pil] pillow pyfiglet colorama
git clone https://github.com/rabiulwebdev/pyQr.git
cd pyQr
python3 pyQr.py
```

### 🪟 Windows (PowerShell)
1. **Install dependencies & run**
2. Install Python
Download from python.org
✅ Make sure to check "Add Python to PATH" during installation.

Install dependencies & run
```bash
pip install qrcode[pil] pillow pyfiglet colorama
git clone https://github.com/rabiulwebdev/pyQr.git
cd pyQr
python pyQr.py
```
🚀 **Usage**
When you run the tool, you will see:
Choose mode:
[1] GUI Mode (Desktop App)
[2] CLI Mode (Terminal Tool)

Press 1 → Opens the GUI app.
Press 2 → Runs CLI mode with banner & options.

📜 License
This project is licensed under the MIT License – free to use and share.

**Developed by Rabiulwebdev 🚀**
