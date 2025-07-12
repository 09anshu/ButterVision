import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

img = None
img_display = None
# Function to create a Butterworth high-pass filter
def butterworth_highpass(shape, cutoff, order):
    rows, cols = shape
    u = np.arange(rows) - rows // 2
    v = np.arange(cols) - cols // 2
    U, V = np.meshgrid(v, u)
    D = np.sqrt(U**2 + V**2) + 1e-5  # Avoid division by zero
    H = 1 - 1 / (1 + (cutoff / D)**(2 * order))
    return np.fft.ifftshift(H)

# Function to apply Butterworth filter in real-time
def apply_filter(event=None):
    global img, img_display

    if img is None:
        return

    cutoff = int(cutoff_slider.get())
    order = int(order_slider.get())

    # Convert image to frequency domain
    fft_image = np.fft.fft2(img)
    fft_shift = np.fft.fftshift(fft_image)

    # Apply Butterworth high-pass filter
    butterworth_hp = butterworth_highpass(img.shape, cutoff, order)
    filtered_fft = fft_shift * butterworth_hp

    # Inverse FFT to get the filtered image
    ifft_shift = np.fft.ifftshift(filtered_fft)
    filtered_image = np.fft.ifft2(ifft_shift)
    filtered_image = np.abs(filtered_image)

    # Normalize to 8-bit (0-255)
    filtered_image = (filtered_image / np.max(filtered_image) * 255).astype(np.uint8)

    # Resize image to fit canvas
    filtered_pil = Image.fromarray(filtered_image).resize((300, 300), Image.Resampling.LANCZOS)
    img_display = ImageTk.PhotoImage(filtered_pil)

    canvas.create_image(0, 0, anchor=tk.NW, image=img_display)

# Function to upload an image
def upload_image():
    global img, img_display

    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)

    # Resize image to fit 300x300 frame
    img_resized = cv2.resize(img, (300, 300))
    img = img_resized  # Update global img

    img_pil = Image.fromarray(img_resized)
    img_display = ImageTk.PhotoImage(img_pil)

    canvas.create_image(0, 0, anchor=tk.NW, image=img_display)
    
    # Apply filter automatically after loading image
    apply_filter()

# GUI setup
root = tk.Tk()
root.title("🔍 Real-Time Butterworth High-Pass Filter")
root.configure(bg="#2c3e50")

# Title
title_label = tk.Label(root, text="Real-Time Butterworth High-Pass Filter", font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="white")
title_label.pack(pady=10)

# Canvas Frame
canvas_frame = tk.Frame(root, bg="#2c3e50", bd=2, relief="groove")
canvas_frame.pack(pady=10)
canvas = tk.Canvas(canvas_frame, width=300, height=300, bg="black", highlightthickness=0)
canvas.pack()

# Controls Frame
controls_frame = tk.Frame(root, bg="#34495e")
controls_frame.pack(pady=15, padx=10, fill="x")

# Upload Button
upload_btn = tk.Button(controls_frame, text="Upload Image", command=upload_image, font=("Arial", 12, "bold"), bg="#1abc9c", fg="white", padx=10, pady=5, relief="flat")
upload_btn.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Cutoff Frequency Slider
cutoff_slider = tk.Scale(controls_frame, from_=5, to=100, label="Cutoff Frequency", orient="horizontal", command=apply_filter,
                         font=("Arial", 10), bg="#34495e", fg="white", troughcolor="#1abc9c", highlightthickness=0)
cutoff_slider.set(30)
cutoff_slider.grid(row=1, column=0, padx=10, pady=5)

# Order Slider
order_slider = tk.Scale(controls_frame, from_=1, to=10, label="Filter Order", orient="horizontal", command=apply_filter,
                        font=("Arial", 10), bg="#34495e", fg="white", troughcolor="#1abc9c", highlightthickness=0)
order_slider.set(2)
order_slider.grid(row=1, column=1, padx=10, pady=5)

# Run GUI
root.mainloop()
