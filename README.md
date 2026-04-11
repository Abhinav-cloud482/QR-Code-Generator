# Advanced QR Code Generator (GUI + Batch + PDF Export)

This is a simple Python script that generates a QR code from user-provided data (text or URL) and saves it as an image file.

## Features

- Generate QR codes from text or URLs
- GUI-based interface (Tkinter)
- Customize colors (foreground & background)
- Add logo to QR codes
- Save QR codes as PNG/JPG
- Auto-generate filenames with timestamps
- Export QR codes to PDF
- Bulk QR generation from CSV/JSON
- Drag-and-drop support (limited)
- Preview before saving

## Requirements

- Python 3.x
- qrcode
- Pillow
- fpdf

## Installation

Install the required package using pip :-

```
pip install qrcode[pil] fpdf
```

## Usage

Run the application :-

```
python qr_generator.py

Then:
- Enter text/URL
- Choose output file
- Customize colors
- (Optional) Add logo
- Click "Generate QR Code"
```

### Bulk QR Generation

- Import CSV or JSON file

- Automatically generates multiple QR codes

### Export to PDF

- Generate QR and save directly as a PDF file

### Logo Support

- Add a logo at the center of the QR code

## Example

Enter the data/URL to encode in QR: https://openai.com

Enter output file name (with .png): openai_qr.png

QR code saved as openai_qr.png

<img width="978" height="516" alt="1" src="https://github.com/user-attachments/assets/ce1f4cb9-c400-4c63-a81a-61c5b7ec3685" />

<img width="1007" height="514" alt="2" src="https://github.com/user-attachments/assets/27c9c1ba-88cd-40e5-add3-a5ac019e3e56" />



## Versions

- v1 : CLI-based QR generator

- v2 : GUI with customization

- v3 : Advanced features (logo, PDF, batch processing)

## License

This project is licensed under the MIT License.

## Author

Abhinav Dixit
