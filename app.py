import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("This is a application for my Boston housing price prediction project")

model=pickle.load(open('miit_rf_boston.pkl','rb'))

crim=st.slider('crim', min_value=0.0, max_value=89.0)
zn=st.slider('zn', min_value=0.0, max_value=100.0)
indus=st.slider('indus', min_value=0.0, max_value=100.0)
chas=st.slider('chas', min_value=0.0, max_value=1.0)
nox=st.slider('nox', min_value=0.0, max_value=1.0)
rm=st.slider('rm', min_value=0.0, max_value=10.0)
age=st.slider('age', min_value=0.0, max_value=100.0)
dis=st.slider('dis', min_value=0.0, max_value=100.0)
rad=st.slider('rad', min_value=0.0, max_value=24.0)
tax=st.slider('tax', min_value=0.0, max_value=100.0)
ptratio=st.slider('ptratio', min_value=0.0, max_value=100.0)
b=st.slider('b', min_value=0.0, max_value=100.0)
lstat=st.slider('lstat', min_value=0.0, max_value=100.0)


# creating a dict from user inputs
user_dict={'crim':crim, 
           'zn':zn, 
           'indus':indus,
           'chas':chas,
           'nox':nox,
           'rm':rm,
           'age':age,
           'dis':dis,
           'rad':rad,
           'tax':tax,
           'ptratio':ptratio,
           'b':b,
           'lstat':lstat}

# converting a dict to df
user_df=pd.DataFrame(user_dict, index=[0])



if st.button('predict'):
    prediction=model.predict(user_df)
    st.write('The predicted price is: $',np.round(prediction[0]*100000, 2))