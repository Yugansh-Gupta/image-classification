import streamlit as st
import numpy as np
from skimage.io import imread
from skimage.transform import resize
from PIL import Image
st.title('Image Classifier Using SVM')

import pickle
model = pickle.load(open('img_model.p','rb'))

uploaded_file = st.file_uploader("Choose an image",type="jpg")
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img,caption='Uploaded Image')
