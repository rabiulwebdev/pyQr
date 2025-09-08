#!/bin/bash

# Colors
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}[*] Installing dependencies...${NC}"
pkg install -y python git

pip install --upgrade pip
pip install qrcode[pil] pillow pyfiglet colorama

echo -e "${GREEN}[*] Cloning QR Generator Tool...${NC}"
git clone https://github.com/rabiulwebdev/qr-generator-tool.git

cd qr-generator-tool

echo -e "${GREEN}[*] Installation complete!${NC}"
echo -e "${GREEN}Run the tool with: python qr_generator.py${NC}"
