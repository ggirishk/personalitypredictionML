import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# loading the saved models
personality_model = pickle.load(open('C:/Users/91888/OneDrive/Desktop/personality/personality.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('personality prediction using ml',
                          ['Home'],
                          default_index=0)

# Define col1, col2, col3, col4, col5 outside the "Home" button block
col1, col2, col3, col4, col5 = st.columns(5)

# personality prediction Page
if selected == 'Home':
    # page title
    st.title('Personality Prediction using ML')
    st.image("download1.jpg")

    # getting the input data from the user
    with col1:
        Gender = st.text_input('Gender')
    with col2:
        Age = st.text_input('Age')
    with col3:
        experience_openness = st.number_input('Enjoy New Experience or Thing (Openness)', min_value=1, max_value=8)
    with col4:
        negativity_neuroticism = st.number_input('How Often You Feel Negativity (Neuroticism)', min_value=1, max_value=8)
    with col5:
        work_thoroughness_conscientiousness = st.number_input('Wishing to Do One\'s Work Well and Thoroughly (Conscientiousness)', min_value=1, max_value=8)

    with col1:
        work_with_peers_agreeableness = st.number_input('How Much Would You Like to Work with Your Peers (Agreeableness)', min_value=1, max_value=8)
    with col2:
        social_interaction_extraversion = st.number_input('How Outgoing and Social Interaction You Like (Extraversion)', min_value=1, max_value=8)
    with col3:
        resume_uploaded = st.file_uploader('Upload Resume', type=['pdf', 'docx'])

    # code for Prediction
    personality_pred = ''

    # creating a button for Prediction
    if st.button('Personality Result'):
        # Convert input values to numerical types
        Gender = float(Gender)
        Age = float(Age)
        experience_openness = float(experience_openness)
        negativity_neuroticism = float(negativity_neuroticism)
        work_thoroughness_conscientiousness = float(work_thoroughness_conscientiousness)
        work_with_peers_agreeableness = float(work_with_peers_agreeableness)
        social_interaction_extraversion = float(social_interaction_extraversion)

        # Use the timestamp as a numeric feature for model prediction
        personality_prediction = personality_model.predict([
            [Age, Gender, experience_openness, negativity_neuroticism, work_thoroughness_conscientiousness, work_with_peers_agreeableness, social_interaction_extraversion]
        ])
        st.success('The output is {}'.format(personality_prediction))

if selected == "About":
    st.text("Let's Learn")
    st.text("Built with Streamlit")
