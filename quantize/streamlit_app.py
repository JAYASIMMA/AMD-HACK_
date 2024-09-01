import streamlit as st
import tensorflow as tf
from tensorflow import keras
import tensorflow_model_optimization as tfmot
import tempfile
import os
import shutil

# Function to load a pre-trained model
def load_model(model_path):
    try:
        model = keras.models.load_model(model_path)
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None
    return model

# Function to quantize the model
def quantize_model(model):
    quantize_model = tfmot.quantization.keras.quantize_model
    q_aware_model = quantize_model(model)
    
    q_aware_model.compile(optimizer='adam',
                          loss='sparse_categorical_crossentropy',
                          metrics=['accuracy'])
    return q_aware_model

# Function to save the quantized model to a temporary file and return its path
def save_model(model):
    temp_dir = tempfile.mkdtemp()
    save_path = os.path.join(temp_dir, 'quantized_model')
    model.save(save_path)
    zip_path = shutil.make_archive(save_path, 'zip', save_path)
    return zip_path

# Streamlit UI
st.title("Model Quantization with Ryzen AI")
uploaded_file = st.file_uploader("Upload your Keras model (.h5)", type="h5")

if uploaded_file is not None:
    model_path = os.path.join(tempfile.gettempdir(), uploaded_file.name)
    with open(model_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    model = load_model(model_path)
    if model:
        st.write("Model loaded successfully!")
        
        if st.button("Quantize Model"):
            quantized_model = quantize_model(model)
            st.write("Model quantized successfully!")
            
            zip_path = save_model(quantized_model)
            
            with open(zip_path, "rb") as f:
                st.download_button("Download Quantized Model", f, file_name="quantized_model.zip")
