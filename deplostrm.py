import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

st.title('Intermediate Class Eligibility Prediction')
st.text_input('Enter your Name:', key='name')
st.file_uploader('upload a file')
#if upload is not None:
data=pd.read_csv('combine_inter1.csv')
#st.write(data)

#load model

model=joblib.load('random_reg_models.joblib')
if st.checkbox('show Training DataFrame'):
    data

# st.subheader('Variable needed')

def predict_eligibility(input_values):
    input_value_as_array=np.asarray(input_values)
    input_data_reshape=input_value_as_array.reshape(1,-1)
    predict_value=model.predict(input_data_reshape)
    print(predict_value)
    if predict_value[0]==0:
       return 'Student not eligible'
    else:
       return 'Student eligible for intermediate'
    
def main():

    #S_N=st.number_input('Student serial No')
    Lesson_Summary=st.number_input('Student lesson summary')
    Assignment_Summary=st.number_input('Student Assignment Summary')
    Grade_Point_Average=st.number_input('Student Average Grade Point')

    #predict eligibility
    eligibility=''

    # create button for prediction
    if st.button('Check Eligibility'):
        eligibility=predict_eligibility([Lesson_Summary,Assignment_Summary,Grade_Point_Average])
    
    st.success(eligibility)

 

if __name__=='__main__':
        main()

st.write(f"Nice working with you @ {st.session_state.name}")


