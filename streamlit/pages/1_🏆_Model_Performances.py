import streamlit as st

st.set_page_config(
    page_title="Model Performances",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.title("Average & High Period Model Performances")

st.markdown('## Average Model ')
st.text('The winning model for the average training data was XGBoost. Neural Net came close but XGBoost, FTW.')

st.subheader('GridSearch Parameters') 
st.text('learning_rate: 0.8 | max_depth: 4 | n_estimators: 150')

st.subheader('Scores & Error Metrics')
st.markdown('- Train R2 Score: 0.988')
st.markdown('- Test R2 Score: 0.971')
st.markdown('- Mean Absolute Error: 2.761')
st.markdown('- Mean Squared Error: 14.165')

st.markdown('![image](https://robfordsfjord.files.wordpress.com/2022/08/a_model.jpeg)')

st.markdown('## High Model ')
st.text('The winning model for the high training data was also XGBoost with added PolynomialFeatures.')

st.subheader('GridSearch Parameters') 
st.text('learning_rate: 0.8 | max_depth: 5 | n_estimators: 150 | reg_lambda: 1')

st.subheader('Scores & Error Metrics')
st.markdown('- Train R2 Score: 0.972')
st.markdown('- Test R2 Score: 0.922')
st.markdown('- Mean Absolute Error: 3.272')
st.markdown('- Mean Squared Error: 20.242')

st.markdown('![image](https://robfordsfjord.files.wordpress.com/2022/08/h_model.jpeg)')