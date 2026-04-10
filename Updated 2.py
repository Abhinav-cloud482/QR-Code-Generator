import os
import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser
from datetime import datetime
import csv
import json
from fpdf import FPDF

def generate_qr(data, filename="my_qrcode.png", fill_color="black", back_color="white", logo_path=None):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

    if logo_path and os.path.exists(logo_path):
        logo = Image.open(logo_path)
        box = (img.size[0] // 3, img.size[1] // 3, img.size[0] * 2 // 3, img.size[1] * 2 // 3)
        logo = logo.resize((box[2] - box[0], box[3] - box[1]))
        img.paste(logo, box, logo if logo.mode == 'RGBA' else None)

    img.save(filename)
    return img

def browse_file(entry):
    filename = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"), ("JPEG", "*.jpg"), ("All files", "*.*")])
    if filename:
        entry.delete(0, tk.END)
        entry.insert(0, filename)

def choose_color(entry):
    color_code = colorchooser.askcolor(title="Choose Color")[1]
    if color_code:
        entry.delete(0, tk.END)
        entry.insert(0, color_code)

def browse_logo(entry):
    path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if path:
        entry.delete(0, tk.END)
        entry.insert(0, path)

def auto_filename():
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join("qr_outputs", f"qr_{now}.png")

def show_preview():
    data = data_entry.get()
    if not data:
        messagebox.showwarning("Missing Data", "Please enter some data or a URL.")
        return

    filename = file_entry.get() or auto_filename()
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    fill = fill_entry.get()
    back = back_entry.get()
    logo = logo_entry.get()

    img = generate_qr(data, filename, fill, back, logo)

    preview = tk.Toplevel()
    preview.title("QR Code Preview")
    img.thumbnail((300, 300))
    tk_img = ImageTk.PhotoImage(img)
    img_label = tk.Label(preview, image=tk_img)
    img_label.image = tk_img
    img_label.pack()

    messagebox.showinfo("Saved", f"QR code saved as {filename}")

def export_to_pdf():
    data = data_entry.get()
    if not data:
        messagebox.showwarning("Missing Data", "Please enter some data.")
        return

    filename = auto_filename().replace(".png", ".pdf")
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    img_path = filename.replace(".pdf", ".png")
    generate_qr(data, img_path, fill_entry.get(), back_entry.get(), logo_entry.get())

    pdf = FPDF()
    pdf.add_page()
    pdf.image(img_path, x=50, y=50, w=100)
    pdf.output(filename)
    messagebox.showinfo("Exported", f"QR code exported to PDF as {filename}")

def import_csv_or_json():
    path = filedialog.askopenfilename(filetypes=[("CSV or JSON", "*.csv;*.json")])
    if not path:
        return

    output_dir = os.path.join("qr_outputs", datetime.now().strftime("%Y%m%d_%H%M%S"))
    os.makedirs(output_dir, exist_ok=True)

    try:
        items = []
        if path.endswith(".csv"):
            with open(path, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                items = [row[0] for row in reader if row]
        elif path.endswith(".json"):
            with open(path, encoding='utf-8') as jsonfile:
                items = json.load(jsonfile)
                if isinstance(items, dict):
                    items = list(items.values())

        for i, data in enumerate(items):
            fname = os.path.join(output_dir, f"qr_{i+1}.png")
            generate_qr(data, fname, fill_entry.get(), back_entry.get(), logo_entry.get())

        messagebox.showinfo("Done", f"Generated {len(items)} QR codes in:\n{output_dir}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def drop(event):
    try:
        dropped_data = root.tk.splitlist(event.data)[0]
        data_entry.delete(0, tk.END)
        data_entry.insert(0, dropped_data)
    except Exception:
        pass

# GUI Setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("450x500")
root.resizable(False, False)

tk.Label(root, text="Data / URL:").pack()
data_entry = tk.Entry(root, width=50)
data_entry.pack(pady=5)

tk.Label(root, text="Output File Name:").pack()
file_frame = tk.Frame(root)
file_entry = tk.Entry(file_frame, width=35)
file_entry.pack(side=tk.LEFT)
tk.Button(file_frame, text="Browse", command=lambda: browse_file(file_entry)).pack(side=tk.RIGHT)
file_frame.pack()

tk.Label(root, text="Fill Color:").pack()
fill_frame = tk.Frame(root)
fill_entry = tk.Entry(fill_frame, width=30)
fill_entry.insert(0, "black")
fill_entry.pack(side=tk.LEFT)
tk.Button(fill_frame, text="Pick", command=lambda: choose_color(fill_entry)).pack(side=tk.RIGHT)
fill_frame.pack()

tk.Label(root, text="Background Color:").pack()
back_frame = tk.Frame(root)
back_entry = tk.Entry(back_frame, width=30)
back_entry.insert(0, "white")
back_entry.pack(side=tk.LEFT)
tk.Button(back_frame, text="Pick", command=lambda: choose_color(back_entry)).pack(side=tk.RIGHT)
back_frame.pack()

tk.Label(root, text="Logo (Optional):").pack()
logo_frame = tk.Frame(root)
logo_entry = tk.Entry(logo_frame, width=30)
logo_entry.pack(side=tk.LEFT)
tk.Button(logo_frame, text="Browse", command=lambda: browse_logo(logo_entry)).pack(side=tk.RIGHT)
logo_frame.pack()

tk.Button(root, text="Generate QR Code", command=show_preview, bg="#4CAF50", fg="white").pack(pady=10)
tk.Button(root, text="Export to PDF", command=export_to_pdf, bg="#2196F3", fg="white").pack(pady=5)
tk.Button(root, text="Generate from CSV/JSON", command=import_csv_or_json, bg="#FF9800", fg="white").pack(pady=5)

# Drag-and-drop support (Windows + Mac/Linux tkinterDnD support is limited)
try:
    root.drop_target_register(DND_FILES)
    root.dnd_bind('<<Drop>>', drop)
except:
    pass

tk.Label(root, text="Drag a file or URL onto the input box if supported").pack(pady=5)

root.mainloop()
