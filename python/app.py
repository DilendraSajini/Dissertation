import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from image_util import ImageUtil
from Classifier import Classifier
import base64

def set_background(image_file):
    with open(image_file, "rb") as f:
        img_data = f.read()
    b64_encoded = base64.b64encode(img_data).decode()
    style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{b64_encoded});
            background-size: {2500}px {1000}px; 
            background-repeat: no-repeat;
            background-position: center center;
            background-opacity: {0.3};
        }}
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)
    
set_background('static/changed-baackground.png')

st.markdown("<h1 style='text-align: center;'>Breast Cancer Classification</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: left;'>Please upload an image of histhopathology WSI</h5>", unsafe_allow_html=True) 
file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])

# Display image
if file is not None:
    image = Image.open(file).convert('RGB')
    
    st.image(image, use_column_width=True)
    patches, preprocessed_patches = ImageUtil.get_patch_images(np.array(image))

    # Display original patches with borders
    st.markdown("<h2 style='text-align: center;'>Patches</h2>", unsafe_allow_html=True)
    num_patches = len(patches)
    num_rows = 2
    num_cols = (num_patches + 1) // num_rows  
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(num_cols * 2, num_rows * 2))

    for i, patch_img in enumerate(patches):
        row = i // num_cols
        col = i % num_cols
        axes[row, col].imshow(patch_img)
        axes[row, col].axis('off')
        axes[row, col].set_title("Patch " + str(i), fontsize=10, pad=5)
        axes[row, col].add_patch(plt.Rectangle((0, 0), patch_img.shape[1], patch_img.shape[0], fill=False, color='black', linewidth=2))

    st.pyplot(fig)

    # Display preprocessed patches with borders
    st.markdown("<h2 style='text-align: center;'>Preprocessed Patches</h2>", unsafe_allow_html=True)
    fig, axes = plt.subplots(num_rows, num_cols, figsize=(num_cols * 2, num_rows * 2))

    for i, patch_img in enumerate(preprocessed_patches):
        row = i // num_cols
        col = i % num_cols
        axes[row, col].imshow(patch_img)
        axes[row, col].axis('off')
        axes[row, col].set_title("Patch " + str(i), fontsize=10, pad=5)
        axes[row, col].add_patch(plt.Rectangle((0, 0), patch_img.shape[1], patch_img.shape[0], fill=False, color='black', linewidth=2))

    st.pyplot(fig)

    classifier_instance = Classifier()
    threshold = 0.5
    predicted_label = classifier_instance.get_predictions(preprocessed_patches, threshold)
    label = predicted_label[0][0]
    if label == 1:
       str = 'Malignant' 
    else: 
       str = 'Benign' 
    # Define a dictionary for color mapping
    color_mapping = {
    'Malignant': 'red',   # Red for malignant
    'Benign': 'green',     # Green for benign
    'unknown': 'blue'      # Blue for unknown (or any other color)
    }
    text_color = color_mapping.get(str, 'black')  # Default to black if label not in the mapping
    st.markdown(f"<h2 style='text-align: center;color: {text_color};'> {str} </h2>", unsafe_allow_html=True)

