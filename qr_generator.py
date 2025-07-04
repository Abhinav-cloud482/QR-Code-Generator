import qrcode

def generate_qr(data, filename="my_qrcode.png"):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,  # controls size (1 to 40)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # L, M, Q, H
        box_size=10,
        border=4
    )

    # Add data to QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save it
    img.save(filename)
    print(f" QR code saved as {filename}")

if __name__ == "__main__":
    user_data = input("Enter the data/URL to encode in QR: ")
    file_name = input("Enter output file name (with .png): ")
    generate_qr(user_data, file_name or "my_qrcode.png")
