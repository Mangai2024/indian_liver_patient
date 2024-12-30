import streamlit as st
import numpy as np
import pickle
import xgboost as xgb
import pandas as pd

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

    
# Input fields for Parkinson's disease prediction
    MDVP_Fo_Hz = st.number_input("Fundamental Frequency (MDVP:Fo(Hz))", min_value=0.0, value=0.0)
    MDVP_Fhi_Hz = st.number_input("Maximum Frequency (MDVP:Fhi(Hz))", min_value=0.0, value=0.0)
    MDVP_Flo_Hz = st.number_input("Minimum Frequency (MDVP:Flo(Hz))", min_value=0.0, value=0.0)
    MDVP_Jitter_percent = st.number_input("Jitter (MDVP:Jitter(%))", min_value=0.0, value=0.0)
    MDVP_Jitter_Abs = st.number_input("Absolute Jitter (MDVP:Jitter(Abs))", min_value=0.0, value=0.0)
    MDVP_RAP = st.number_input("Relative Average Perturbation (MDVP:RAP)", min_value=0.0, value=0.0)
    MDVP_PPQ = st.number_input("Pitch Period Perturbation Quotient (MDVP:PPQ)", min_value=0.0, value=0.0)
    Jitter_DDP = st.number_input("Degree of Derivative Perturbation (Jitter:DDP)", min_value=0.0, value=0.0)
    MDVP_Shimmer = st.number_input("Shimmer (MDVP:Shimmer)", min_value=0.0, value=0.0)
    MDVP_Shimmer_dB = st.number_input("Shimmer in dB (MDVP:Shimmer(dB))", min_value=0.0, value=0.0)
    Shimmer_APQ3 = st.number_input("Amplitude Perturbation Quotient (Shimmer:APQ3)", min_value=0.0, value=0.0)
    Shimmer_APQ5 = st.number_input("Amplitude Perturbation Quotient (Shimmer:APQ5)", min_value=0.0, value=0.0)
    MDVP_APQ = st.number_input("Amplitude Perturbation Quotient (MDVP:APQ)", min_value=0.0, value=0.0)
    Shimmer_DDA = st.number_input("Difference of Average Amplitude (Shimmer:DDA)", min_value=0.0, value=0.0)
    NHR = st.number_input("Noise-to-Harmonics Ratio (NHR)", min_value=0.0, value=0.0)
    HNR = st.number_input("Harmonics-to-Noise Ratio (HNR)", min_value=0.0, value=0.0)
    RPDE = st.number_input("Recurrence Period Density Entropy (RPDE)", min_value=0.0, value=0.0)
    DFA = st.number_input("Detrended Fluctuation Analysis (DFA)", min_value=0.0, value=0.0)
    spread1 = st.number_input("Signal Spread 1 (spread1)", value=0.0)
    spread2 = st.number_input("Signal Spread 2 (spread2)", value=0.0)
    D2 = st.number_input("Correlation Dimension (D2)", min_value=0.0, value=0.0)
    PPE = st.number_input("Pitch Period Entropy (PPE)", min_value=0.0, value=0.0)















