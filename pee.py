import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np
from PIL import Image
import os
import gdown

st.set_page_config(page_title="Pothole Detector", layout="centered")
st.title("🚧 Pothole Detection App")
st.write("Upload an image of a road, and the AI will tell you if there's a pothole.")

MODEL_PATH = 'models/resnet_pothole_model.keras'
GDRIVE_FILE_ID = '1FiaiIYT-7lbreiiEln6i_mIUN0upXxYU'

# Create models folder if not exists
os.makedirs('models', exist_ok=True)

@st.cache_resource
def load_model_safely():
    if not os.path.exists(MODEL_PATH):
        with st.spinner("Downloading model..."):
            url = f'https://drive.google.com/uc?id={GDRIVE_FILE_ID}'
            gdown.download(url, MODEL_PATH, quiet=False)
    try:
        model = load_model(MODEL_PATH)
        return model
    except Exception as e:
        st.error(f"🚫 Error loading model: {e}")
        st.stop()

model = load_model_safely()

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_column_width=True)

    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    with st.spinner("Analyzing image..."):
        prediction = model.predict(img_array)[0][0]
        label = "Pothole" if prediction > 0.5 else "Normal"
        confidence = prediction if label == "Pothole" else 1 - prediction

    st.markdown(f"### 🧠 Prediction: **{'Pothole detected 🚧' if label == 'Pothole' else 'Road is normal ✅'}**")
    st.markdown(f"**Confidence:** `{confidence:.2%}`")
