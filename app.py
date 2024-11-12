
import streamlit as st
import pickle


def load_model():
    
    with open('model.pkl', 'rb') as file:
        return pickle.load(file)

model = load_model()

st.set_page_config(page_title="Customer Offer Prediction", page_icon="🔮", layout="centered", initial_sidebar_state="collapsed")
st.header("Customer Offer Prediction")
def get_user_input():
    
    time_on_website = st.slider("Time on Website", 0.0, 40.0, 10.0)  # Website par time
    yearly_amount = st.slider("Yearly Amount Spent", 0.0, 800.0, 400.0)  # Saalana kharch
    time_on_app = st.slider("Time on App", 0.0, 20.0, 8.0)  # App par time
    length_of_membership = st.slider("Length of Membership", 0.0, 8.0, 3.0)  # Member hone ka time
   
    return [time_on_website, yearly_amount, time_on_app, length_of_membership]


user_input = get_user_input()


def make_prediction(input_data):
  
    prediction = model.predict([input_data])
    return prediction


if st.button("Predict"):

    prediction = make_prediction(user_input)
    
    
    if prediction == 1:
        st.subheader("Offer")  
        
        st.markdown('<div style="background-color: green; color: white; padding: 10px;">Yes  the customer will get Offer</div>', unsafe_allow_html=True)
    else:
        st.subheader("No Offer")
       
        st.markdown('<div style="background-color: red; color: white; padding: 10px;">No the customer wont get Offer</div>', unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: black;
        color: white;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        Made with ❤️ by <a href='https://github.com/sanskaryo' target='_blank'>Sanskar</a><br>
        So you can get Great Offers
    </div>
    """,
    unsafe_allow_html=True
)