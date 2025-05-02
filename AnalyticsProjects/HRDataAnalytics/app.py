# HR Analytics Dashboard with Predictive Insights (Streamlit Version)

import pandas as pd
import numpy as np  # imported for future numeric operations
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

st.set_page_config(page_title="HR Analytics Dashboard", layout="wide")
st.title("HR Analytics Dashboard with Predictive Insights")

# Upload dataset
uploaded_file = st.file_uploader("Upload your HR CSV data", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.dataframe(df.head())

    # Data cleaning
    df.dropna(inplace=True)
    df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})
    df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

    # Sidebar filters
    with st.sidebar:
        st.header("Filters")
        selected_dept = st.selectbox(
            "Select Department", options=df['Department'].unique())
        filtered_df = df[df['Department'] == selected_dept]

    # Exploratory Data Analysis
    st.subheader("Attrition by Department")
    fig, ax = plt.subplots()
    sns.countplot(data=filtered_df, x='JobRole', hue='Attrition', ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Feature engineering
    features = ['Age', 'Gender', 'MonthlyIncome', 'YearsAtCompany']
    X = df[features]
    y = df['Attrition']

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42)

    # Model training
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predictions and evaluation
    y_pred = model.predict(X_test)
    st.subheader("Model Performance")
    st.text("Confusion Matrix")
    st.write(confusion_matrix(y_test, y_pred))
    st.text("Classification Report")
    st.text(classification_report(y_test, y_pred))

    # Feature importances
    importances = model.feature_importances_
    feat_importances = pd.Series(importances, index=features)
    st.subheader("Feature Importances")
    fig2, ax2 = plt.subplots()
    feat_importances.sort_values().plot(kind='barh', ax=ax2)
    st.pyplot(fig2)

    # Export results
    df['Attrition_Predicted'] = model.predict(X)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Predictions", data=csv,
                       file_name='employee_predictions.csv', mime='text/csv')
else:
    st.info("Awaiting CSV upload.")
