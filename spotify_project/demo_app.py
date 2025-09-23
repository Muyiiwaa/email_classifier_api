import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from utils import make_prediction



st.title("COLLEGE PLACEMENT PREDICTION APPLICATION")
st.divider()

col1, col2 = st.columns(2)
with col1:
    iq = st.number_input(label='iq', min_value=0)
    prev_sem_result = st.number_input(label='previous result', min_value=0)
    cgpa = st.number_input(label='CGPA', min_value=0)
    academic_performance = st.number_input(label='academic_performance', min_value=0)
with col2:
    internship_experience = st.selectbox(label='internship_experience',options=["Yes","No"])
    extra_curricular_score = st.number_input(label='extra_curricular_score', min_value=0)
    communication_skills = st.number_input(label='communication_skills', min_value=0)
    Projects_Completed = st.number_input(label='Projects_Completed', min_value=0)

if st.button(label="Predict College Placement", type="primary"):
    column_names = ['IQ', 'Prev_Sem_Result', 'CGPA',
        'Academic_Performance', 'Internship_Experience',
        'Extra_Curricular_Score', 'Communication_Skills', 'Projects_Completed']
    data_list = [[iq,prev_sem_result,cgpa,academic_performance,internship_experience,
                extra_curricular_score,communication_skills,Projects_Completed]]
    data = pd.DataFrame(data=data_list, columns= column_names)
    prediction = make_prediction(data=data)
    placements = ["No","Yes"]
    st.success(f"The placement decision is {placements[prediction]}")

