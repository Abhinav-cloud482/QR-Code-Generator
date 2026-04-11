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

# Updated 1

<img width="403" height="383" alt="Update 1" src="https://github.com/user-attachments/assets/a03e2f99-611d-4d8a-8da2-ffac13a82a3a" />

# Updated 2

<img width="447" height="528" alt="Updated 2" src="https://github.com/user-attachments/assets/40966420-4c22-4ba7-bb5e-618db83a37ed" />
<img width="459" height="535" alt="Updated 2 Output 2" src="https://github.com/user-attachments/assets/d403ffa2-4627-4595-99ff-9dd05a8ff6f1" />
<img width="364" height="181" alt="Updated 2 Outpput" src="https://github.com/user-attachments/assets/27d007a1-38fb-4472-8316-faabbfa4984e" />
<img width="370" height="370" alt="Openai" src="https://github.com/user-attachments/assets/f2d47626-8431-4060-8868-86e54632da01" />


## Versions

- v1 : CLI-based QR generator

- v2 : GUI with customization

- v3 : Advanced features (logo, PDF, batch processing)

## License

This project is licensed under the MIT License.

## Author

Abhinav Dixit
