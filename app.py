import streamlit as st
import pickle
import numpy as np


# import the model
pipe = pickle.load(open('pipe.pkl','rb'))
df = pickle.load(open('df_final.pkl','rb'))

st.title("Mobile Price Predictor")

# brand
company = st.selectbox('Brand',df['brand'].unique())

# model
model = st.selectbox('Model',df['model'].unique())

#processor
processor = st.selectbox('Processor',df['processor'].unique())

# rom
rom = st.selectbox('ROM (in GB)',df['ROM'].unique())

# ram
ram = st.selectbox('RAM (in GB)',df['RAM'].unique())

# display
display = st.number_input('Screen display in inch')

# battery
battery = st.number_input('Battery capacity in MAH')

# camera
camera = st.selectbox('Camera',df['camera'].unique())

# 5G
fiveG = st.selectbox('5G',['No','Yes'])


if st.button('Predict Price'):
    # query
    if fiveG == 'Yes':
        fiveG = 1
    else:
        fiveG = 0

    query = np.array([company,model,processor,rom,ram,display,battery,camera,fiveG])

    query = query.reshape(1,9)
    res = int(np.exp(pipe.predict(query)[0]))
    res_plus = res + (res * 0.05)
    res_min = res - (res * 0.05)
    st.title("The predicted price of this configuration is between " + str(res_min) + " to " + str(res_plus))