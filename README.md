# QR-Code-Generator

QR Code Generator

This is a simple Python script that generates a QR code from user-provided data (text or URL) and saves it as an image file.

Features

- Generates QR codes from any text or URL

- High error correction level (H)

- Customizable output filename

- Saves QR codes as PNG images

Requirements
- Python 3.x

- qrcode

- Pillow (installed automatically with qrcode)

Installation

Install the required package using pip :

pip install qrcode[pil]

Usage

Run the script from the command line :

python qr_generator.py

You'll be prompted to enter :

- The data or URL to encode

- The output file name (e.g., mycode.png)

Example

Enter the data/URL to encode in QR: https://openai.com

Enter output file name (with .png): openai_qr.png

QR code saved as openai_qr.png

License

This project is licensed under the MIT License.

Author

Abhinav Dixit
