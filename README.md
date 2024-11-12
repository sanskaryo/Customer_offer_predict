
# Customer Offer Prediction 🎁

Welcome to the **Customer Offer Prediction** repository! This project is a machine learning-powered application built with **Streamlit** to predict whether an e-commerce customer is eligible for an offer based on their behavioral metrics. The app uses a **Random Forest classifier** to determine offer eligibility, providing valuable insights for marketing and customer engagement.

## 📌 Project Overview

In e-commerce, personalizing offers based on customer behavior can significantly increase customer retention and satisfaction. This project predicts whether a customer should receive an offer based on specific parameters, such as:

- Time spent on the website
- Time spent on the app
- Yearly amount spent
- Length of membership

By analyzing these factors, the app aims to help businesses make data-driven decisions to boost customer loyalty and engagement.

## 🎯 Key Features

- **Real-time Predictions**: Input customer metrics to get an immediate prediction of offer eligibility.
- **Streamlit Interface**: An intuitive and interactive web-based interface.
- **Customizable Parameters**: Adjust sliders to simulate different customer profiles.
- **Styled Results Display**: Visually distinct "Offer" and "No Offer" indicators for clear insights.

## 🛠️ Technology Stack

- **Python**: Core programming language.
- **Streamlit**: Frontend for building a responsive web application.
- **Scikit-Learn**: Random Forest classifier for predictive modeling.
- **Pickle**: Model serialization for easy deployment.

  ## Page View - ![image](https://github.com/user-attachments/assets/a0c6cf76-ba1f-4f00-90dc-798a193fb825)


## 🚀 Getting Started

### Prerequisites

Ensure you have **Python 3.7+** installed. Then, install the necessary packages:

```bash
pip install streamlit scikit-learn pandas
```

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/sanskaryo/Customer_offer_predict.git
    ```
   
2. **Navigate to the Project Directory**:
    ```bash
    cd Customer_offer_predict
    ```

3. **Run the App**:
    ```bash
    streamlit run app.py
    ```

4. **Access the Application**: Go to `http://localhost:8501` in your browser.

### Input Parameters

The app requires the following inputs:
- **Time on Website**: Time spent on the website (0-40 minutes).
- **Yearly Amount Spent**: Total amount spent annually by the customer (0-800 USD).
- **Time on App**: Time spent on the app (0-20 minutes).
- **Length of Membership**: Duration of membership (0-8 years).

### Example Usage

After inputting the parameters, click **"Predict Eligibility"** to see if the customer qualifies for an offer. Results are displayed with color-coded visuals:
- **Green**: Eligible for offer
- **Red**: Not eligible for offer

## 📂 Project Structure

```
.
├── app.py               # Main Streamlit application
├── model.pkl            # Serialized Random Forest model
├── README.md            # Project documentation
└── requirements.txt     # List of dependencies
```

## 📈 Model Information

The model was trained using a Random Forest classifier with historical customer data to identify patterns in spending and activity. This model can be further fine-tuned by adding more relevant features or experimenting with different algorithms for better accuracy.

## ✨ Future Enhancements

Some potential enhancements include:
- **Improving Model Accuracy**: Experiment with additional features.
- **Enhanced UI**: Add charts and interactive components.
- **Backend Integration**: Store customer data in a database for real-time analytics.

## 🤝 Contributing

Feel free to fork this repository and create a pull request if you'd like to contribute. Any ideas for improving this project are welcome!

## 📄 License

This project is licensed under the MIT License.

## 📝 Acknowledgments

Thanks to the open-source community and **Streamlit** for making this project possible.

---

Enjoy the app, and happy predicting! 🎉
