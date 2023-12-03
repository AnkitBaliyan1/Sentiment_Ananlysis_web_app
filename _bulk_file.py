import streamlit as st
import pandas as pd
import base64
from _translate_liner import generate_message, generate_response
from openai._client import OpenAI

# Function to download data
def get_table_download_link(df, filename, text):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}">{text}</a>'
    return href


def main():
    st.title("Bulk file translation")

    # Display a sample dataframe
    st.write("Sample input file format:")
    sample_df = pd.DataFrame({
            'input': [
                "यहां नमूना पाठ दर्ज करें",    # Hindi
                "এখানে নমুনা পাঠ্য লিখুন",    # Bengali
                "हांव नमुना पाठ दाखल करा",     # Konkani
                "ਇੱਥੇ ਨਮੂਨਾ ਪਾਠ ਦਰਜ ਕਰੋ"     # Punjabi
            ],
            'output': [""] * 4  
        })
    st.write(sample_df)
    st.write("Note: Enter your data in Input column. \n Column name should be \"input\" and \"output\" ")

    # File uploader
    uploaded_file = st.file_uploader("Upload a file (CSV or Excel)", type=["csv", "xlsx"])

    if uploaded_file is not None:
        # Read the file
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            run=True
        elif uploaded_file.name.endwith('xlsx'):
            df = pd.read_excel(uploaded_file)
            run=True
        else:
            st.error("Incorrect file format")
            run=False

        if run:
            with st.spinner():
                # Perform operation on 'input' column
                df['output'] = df['input'].apply(lambda x: generate_response(user_input=x))  # Replace with your operation

                # Show processed DataFrame
                st.write("Processed DataFrame:")
                st.write(df)

            # Download link
            st.markdown(get_table_download_link(df, 'processed_data.csv', 'Download Processed Data as CSV'), unsafe_allow_html=True)

    