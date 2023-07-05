# -*- coding: utf-8 -*-

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

print(heart_disease_model)

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Disease Prediction System',
                          [
                           'Heart Disease Prediction', ],
                          icons=['activity','heart','person'],
                          default_index=0)
    
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Tuổi')
        
    with col2:
        sex = st.number_input('Giới tính')
        
    with col3:
        cp = st.number_input('Chest pain type - tức ngực')
        
    with col1:
        trestbps = st.number_input('trestbps - Huyết áp')
        
    with col2:
        chol = st.number_input('Lượng cholestoral trong máu (mg/dl)')
        
    with col3:
        fbs = st.number_input('Lượng đường trong máu > 120 mg/dl')

    with col1:
        restecg = st.number_input('Kết quả điện tâm đồ')
        
    with col2:
        thalach = st.number_input('Nhịp tim(thalach)')
        
    with col3:
        exang = st.number_input('Đau thắt ngực khi tập thể dục')
        
    with col1:
        oldpeak = st.number_input('Tình trạng stress')
        
    with col2:
        slope = st.number_input('Độ dốc đoạn ST trong điện tâm đồ')
        
    with col3:
        ca = st.number_input('Số lượng các mạch chính')
        
    with col1:
        thal = st.number_input('thal - thalium stress result - stress thalium')
        
        
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1 ):
          heart_diagnosis = 'Bị bệnh tim mạch'
        else:
          heart_diagnosis = 'Không bị bệnh tim mạch'
        
    st.success(heart_diagnosis)
        
    


