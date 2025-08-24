import streamlit as st
import pandas as pd
from query_handler import QueryHandler

st.set_page_config(layout="wide", page_title="Data Explorer")

st.title("📂 Data Analysis Tool")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Load CSV or Excel
    if uploaded_file.name.endswith(".csv"):
        data = pd.read_csv(uploaded_file)
    else:
        data = pd.read_excel(uploaded_file)

    st.success("✅ Data Loaded Successfully!")
    st.dataframe(data.head(), use_container_width=True)

    # Initialize query handler
    handler = QueryHandler(data)

    # Query box fixed at the bottom
    query = st.text_input("Enter your query (press Enter to run)", key="query_box")

    # Auto submit when Enter is pressed OR button clicked
    if query or st.button("Submit Query"):
        response = handler.handle_summarize_data(query)
        st.markdown(response)
else:
    st.info("⬆️ Please upload a CSV or Excel file to get started.")