import pickle
import streamlit as st

# Load models
models = {
    "Random Forest": "classifier.pkl",
    "SVM": "svm.pkl",
    "KNN": "knn.pkl"
}

def load_model(model_name):
    with open(models[model_name], 'rb') as file:
        return pickle.load(file)

@st.cache_data()
def prediction(model, Gender, Married, ApplicantIncome, LoanAmount, Credit_History):
    # Pre-processing user input    
    Gender = 0 if Gender == "Male" else 1
    Married = 0 if Married == "Unmarried" else 1
    Credit_History = 0 if Credit_History == "Unclear Debts" else 1  
    LoanAmount = LoanAmount / 1000
    
    # Making predictions 
    prediction = model.predict([[Gender, Married, ApplicantIncome, LoanAmount, Credit_History]])
    return 'Approved' if prediction == 1 else 'Rejected'

# Streamlit app
def main():
    # Header
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
    </div> 
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    # Model selection
    model_choice = st.selectbox("Choose a model", list(models.keys()))
    classifier = load_model(model_choice)
    
    # User input
    Gender = st.selectbox('Gender',("Male","Female"))
    Married = st.selectbox('Marital Status',("Unmarried","Married")) 
    ApplicantIncome = st.number_input("Applicants monthly income") 
    LoanAmount = st.number_input("Total loan amount")
    Credit_History = st.selectbox('Credit History',("Unclear Debts","No Unclear Debts"))
    result = ""
    
    # Prediction button
    if st.button("Predict"): 
        result = prediction(classifier, Gender, Married, ApplicantIncome, LoanAmount, Credit_History) 
        st.success(f'Your loan is {result}')

if __name__ == '_main_': 
    main()
