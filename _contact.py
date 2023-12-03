import streamlit as st


def main():
    st.title('Contact Us')
    st.subheader('Ping me at: +91-9958631596')
    footer_style = """
            <style>
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #f1f1f1;
                color: black;
                text-align: center;
                padding: 10px;
                font-size: 16px;
            }
            </style>
        """

    # Add custom CSS for the footer
    st.markdown(footer_style, unsafe_allow_html=True)

    # Adding the footer
    footer = """
        <div class="footer">
        <p><strong>Note:</strong> We don't have timings decided yet.!</p>
        </div>
    """
    st.markdown(footer, unsafe_allow_html=True)
