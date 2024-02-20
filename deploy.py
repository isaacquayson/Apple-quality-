# importing the needed libraries
import numpy as np
import pickle
import pandas as np
import streamlit as st

model = pickle.load(open("C:/Users/quays/OneDrive/Desktop/model/model3.pkl", "rb"))

def main():
    st.title("Apple Quality Classification")

    # inputing the variable in the column section
    Size = st.text_input('Size of Apple: ')
    Weight = st.text_input('Weight  of Apple: ')
    Sweetness = st.text_input('Sweetness of Apple: ')
    Crunchiness = st.text_input('Crunchiness of Apple: ')
    Juiciness = st.text_input('Juiciness of Apple: ')
    Ripeness = st.text_input('Ripeness of Apple: ')
    Acidity = st.text_input('Acidity of Apple: ')

    # prediction code
    if st.button("Predict"):
        make_prediction = model.predict([['Size', 'Weight', 'Sweetness', 'Crunchiness', 'Juiciness','Ripeness', 'Acidity']])
        st.success(f"Your apple is class as {make_prediction}")

if __name__ == "__main__":
    main()
