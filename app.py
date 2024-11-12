import streamlit as st
import pickle


def load_model():
    with open('model.pkl', 'rb') as file:
        return pickle.load(file)

model = load_model()

# Page ka text aur styling ke liye
st.set_page_config(
    page_title="🌟 Predict Your Offer Eligibility! 🌟",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get help': 'https://github.com/sanskaryo',
        'Report a bug': 'https://github.com/sanskaryo',
        'About': "# Predictive Offer Eligibility with Machine Learning"
    }
)

# The Header
st.markdown("""
    <h1 style='text-align: center; color: #4a47a3; font-weight: bold;'>Customer Offer Prediction</h1>
    <p style='text-align: center; color: #4a47a3;'>Using advanced machine learning to predict if a customer deserves a special offer!</p>
""", unsafe_allow_html=True)

# user  se input lene ke liye
def get_user_input():
    st.markdown("<h3 style='color: #4a47a3;'>Customer Metrics</h3>", unsafe_allow_html=True)
    
    time_on_website = st.slider("⏱ Time on Website (in minutes)", 0.0, 40.0, 10.0)
    yearly_amount = st.slider("💸 Yearly Amount Spent (in USD)", 0.0, 800.0, 400.0)
    time_on_app = st.slider("📱 Time on App (in minutes)", 0.0, 20.0, 8.0)
    length_of_membership = st.slider("📆 Length of Membership (in years)", 0.0, 8.0, 3.0)
   
    return [time_on_website, yearly_amount, time_on_app, length_of_membership]

user_input = get_user_input()

# Prediction ka function
def make_prediction(input_data):
    return model.predict([input_data])[0]

# Prediction button with feedback and styling
if st.button("🔍 Predict Eligibility"):

    prediction = make_prediction(user_input)
    
    # Display result with style
    if prediction == 1:
        st.markdown('<h3 style="color: #2ecc71;">🎉 Yes! The customer is eligible for an offer! 🎉</h3>', unsafe_allow_html=True)
        st.markdown('<div style="background-color: #2ecc71; color: white; padding: 15px; text-align: center;">This customer qualifies for an offer based on their engagement!</div>', unsafe_allow_html=True)
    else:
        st.markdown('<h3 style="color: #e74c3c;">🚫 No Offer</h3>', unsafe_allow_html=True)
        st.markdown('<div style="background-color: #e74c3c; color: white; padding: 15px; text-align: center;">Unfortunately, the customer doesn’t qualify for an offer at this time.</div>', unsafe_allow_html=True)

# Custom footer Bhai ka nam
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #4a47a3;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    .footer a {
        color: #ffffff;
        text-decoration: underline;
    }
    </style>
    <div class="footer">
        Made with ❤️ by <a href='https://github.com/sanskaryo' target='_blank'>Sanskar</a> | Empowering Smart Offers
    </div>
    """,
    unsafe_allow_html=True
)
