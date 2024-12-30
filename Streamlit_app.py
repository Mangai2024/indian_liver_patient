import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Streamlit UI
st.title("Mulitiple Disease Prediction")

# Sidebar for disease selection
nav = st.sidebar.radio("Select Multiple Disease Prediction", ["Parkinson's Disease", "Kidney Disease", "Liver Disease"])

if nav == "Parkinson's Disease":
    st.header("Parkinson's Multiple Disease Prediction")
    
    # Load the Parkinson's model
    try:
        parkinson_model = pickle.load(open(r'XGBparkinsons.pkl', 'wb'))
    except FileNotFoundError:
        st.error("Model file not found. Please check the file path.")
        st.stop()
