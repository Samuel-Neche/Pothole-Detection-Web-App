# 🛣️ Pothole Detection Web App

This project uses a fine-tuned **ResNet50 deep learning model** to detect potholes in road images. It is built with **TensorFlow** and deployed using **Streamlit**.

---

## 📌 Features

- Upload a road image (JPG, PNG)
- Predict if the road is **Normal** or contains a **Pothole**
- See model confidence
- Visual feedback with uploaded image
- Lightweight and deployable

---

## 🧠 Model Summary

- Base Model: `ResNet50` (pre-trained on ImageNet)
- Custom Layers: `GlobalAveragePooling2D`, `Dense`, `Dropout`
- Fine-tuned last 20 layers
- Optimizer: Adam with learning rate `1e-4`
- Loss Function: Binary Crossentropy
- Data Augmentation: Rotation, Zoom, Flip, etc.

---

## 🚀 How to Run

### 1. Clone this repo
```bash
git clone https://github.com/Samuel-Neche/Pothole-Detection-Web-App
cd pothole-detection-app
