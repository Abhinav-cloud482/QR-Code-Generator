import qrcode
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser

def generate_qr(data, filename="my_qrcode.png", fill_color="black", back_color="white"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color=fill_color, back_color=back_color).convert('RGB')
    img.save(filename)
    return img

def choose_color(entry):
    color_code = colorchooser.askcolor(title="Choose Color")[1]
    if color_code:
        entry.delete(0, tk.END)
        entry.insert(0, color_code)

def browse_file(entry):
    filename = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"), ("JPEG", "*.jpg"), ("All files", "*.*")])
    if filename:
        entry.delete(0, tk.END)
        entry.insert(0, filename)

def show_preview():
    data = data_entry.get()
    filename = file_entry.get() or "preview.png"
    fill = fill_entry.get()
    back = back_entry.get()

    if not data:
        messagebox.showwarning("Missing Data", "Please enter some data or a URL.")
        return

    img = generate_qr(data, filename, fill, back)

    preview = tk.Toplevel()
    preview.title("QR Code Preview")

    img.thumbnail((300, 300))
    tk_img = ImageTk.PhotoImage(img)

    img_label = tk.Label(preview, image=tk_img)
    img_label.image = tk_img
    img_label.pack()

    messagebox.showinfo("Saved", f"QR code saved as {filename}")

# GUI Setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x350")
root.resizable(False, False)

tk.Label(root, text="Data / URL:").pack()
data_entry = tk.Entry(root, width=50)
data_entry.pack()

tk.Label(root, text="Output File Name:").pack()
file_frame = tk.Frame(root)
file_entry = tk.Entry(file_frame, width=40)
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

tk.Button(root, text="Generate QR Code", command=show_preview, bg="#4CAF50", fg="white").pack(pady=20)

root.mainloop()
