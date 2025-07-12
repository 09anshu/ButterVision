# 🧠 ButterVision: Real-Time Butterworth High-Pass Filter in Digital Image Processing

**ButterVision** is a **Digital Image Processing (DIP)** project that demonstrates the application of the **Butterworth High-Pass Filter** to grayscale images using the frequency domain. It offers a user-friendly graphical interface built with Python and Tkinter, where users can experiment with real-time parameter tuning and observe the effects of frequency filtering.

---

## 🎯 Project Domain

> **Digital Image Processing (DIP)**  
This project focuses on frequency domain filtering techniques, specifically using the Butterworth High-Pass filter to enhance image details and suppress low-frequency components such as background and illumination.

---

## 🚀 Features

- 📤 Upload and preview any grayscale image.
- 🔧 Interactive sliders to adjust:
  - **Cutoff Frequency**: Controls the radius of the high-pass filtering effect.
  - **Filter Order**: Controls the sharpness or steepness of the filter's transition.
- ⚡ Real-time preview of filtered image as you adjust parameters.
- 🎨 Clean and modern GUI using Tkinter.

---

## 🧰 Tools & Libraries Used

| Tool | Purpose |
|------|---------|
| `Python` | Core programming language |
| `Tkinter` | GUI development |
| `OpenCV` | Image reading and preprocessing |
| `NumPy` | FFT-based frequency domain filtering |
| `Pillow (PIL)` | Image format conversion and GUI rendering |

---

## 📸 GUI Screenshot

Here’s a glimpse of the user interface:

![ButterVision GUI](./1486a746-8568-4c85-bb96-befcafd1259c.png)

---

## 📂 How to Run

### 🛠️ Prerequisites

Install required libraries:

```bash
pip install opencv-python pillow numpy
