# 🚧 Pothole Detection Web App

A simple and intelligent web application that detects potholes in road images using a fine-tuned **ResNet50** deep learning model. Built with **TensorFlow** and deployed using **Streamlit**, this app is designed to help identify damaged roads — a step toward smarter infrastructure monitoring.

---

## 📌 Features

* ✅ Upload a road image (`.jpg`, `.png`, `.jpeg`)
* ✅ Predict if the road is **Normal** or has a **Pothole**
* ✅ See the model’s **confidence score**
* ✅ Visual feedback with the uploaded image
* ✅ Lightweight and deployable — model auto-downloads if not present

---

## 🧐 Model Summary

* **Base Model**: `ResNet50` (pre-trained on ImageNet)
* **Custom Layers**: `GlobalAveragePooling2D`, `Dense`, `Dropout`
* **Fine-Tuning**: Last 20 layers of ResNet50
* **Optimizer**: Adam (`learning_rate=1e-4`)
* **Loss Function**: Binary Crossentropy
* **Data Augmentation**: Random rotation, zoom, horizontal flip, etc.
* **Output**: Binary classification — `Pothole` or `Normal`

---
## Live Demo ➜ [View on Hugging Face](https://huggingface.co/spaces/nechesdc/pothole-detection-app)

---
## 🚀 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Samuel-Neche/Pothole-Detection-Web-App.git
cd Pothole-Detection-Web-App
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
# source venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

🧠 On first run, the model will automatically download from Google Drive and be cached for future use.

---

## 📂 Model Info

* **Filename**: `resnet_pothole_model.keras`
* **Downloaded Automatically** via `gdown` (no manual setup needed)
* **Google Drive Link**:
  🔗 [Click to View on Drive](https://drive.google.com/file/d/1FiaiIYT-7lbreiiEln6i_mIUN0upXxYU/view)

---

## 🧪 Example Output

After uploading a road image:

```
🧠 Prediction: Pothole detected 🚧
Confidence: 94.12%
```

---

## 📦 Dependencies

Major Python libraries used:

* `tensorflow`
* `streamlit`
* `pillow`
* `numpy`
* `gdown`

Install all with:

```bash
pip install -r requirements.txt
```

---

## 📁 Project Structure

```
Pothole-Detection-Web-App/
️️|
️️├── app.py                        # Streamlit web app
️️├── models/                       # Model directory (auto-created)
️️│   └── resnet_pothole_model.keras  # Downloaded from Google Drive
️️├── requirements.txt              # Project dependencies
️️└── README.md                     # Project documentation
```

---

## 🤝 Contributing

Got ideas to improve detection or the app itself?
Pull requests and issues are welcome — let’s make roads safer together.

---

## 👤 Author

**Samuel David Neche**
📧 [neche.sdc@gmail.com](mailto:neche.sdc@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/samuel-neche-david)
🎨 [Portfolio](https://nechesdc.my.canva.site/portfolio)

---

## 📍 License

This project is licensed under the **MIT License**.
Use it freely, modify it, and share it to build better road infrastructure tools.
