#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import streamlit as st
import pickle


# In[9]:


log_model=pickle.load(open('log30.pkl','rb'))


# In[10]:


st.title('Model Deployment using Logistic Regression')


# In[12]:


def user_input_parameter():
    Pregnancies=st.sidebar.number_input('Enter the pregnancies')
    Glucose=st.sidebar.number_input('Enter the Glucose Level')
    BMI=st.sidebar.number_input('Enter the BMI')
    DiabetesPedigreeFunction=st.sidebar.number_input('Enter the Diabetes Pedigree Value')
    Age=st.slider('Select Your Age',0,100)
    dict1={'Pregnancies':Pregnancies,'Glucose':Glucose,'BMI':BMI,'DiabetesPedigreeFunction':DiabetesPedigreeFunction,'Age':Age} # Converting it into a diction to convert it into a dataframe
    features=pd.DataFrame(dict1,index=[0])
    return features
df=user_input_parameter()
pred=log_model.predict(df)
pred_prob=log_model.predict_proba(df)
button=st.button('predict')
if button is True:
    st.subheader('Predicted')
    st.write('Diabetic' if pred_prob[0][1]>=0.5 else 'Not Diabetic')
    st.subheader('Pred_prob')
    st.write(pred_prob)


# In[ ]:





# In[ ]:




