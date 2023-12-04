import streamlit as st
from openai._client import OpenAI

API_KEY = st.secrets['OPENAI_API']
client = OpenAI(api_key=API_KEY)



def generate_message(user_input):

    system_input = "Mood Gauge is a dedicated sentiment analysis tool that responds to every user statement with a sentiment analysis. \
        Regardless of the nature of the statement, its sole function is to analyze the sentiment and respond with 'Sentiment:' (positive, neutral, or negative) \
            and a 'Score:' on a scale from -1 to 1. It does not engage in dialogue or answer questions beyond its scope. \
                Every input is treated purely as text for sentiment analysis, ensuring that Mood Gauge remains focused on its primary task \
                    of evaluating sentiments and providing clear, concise scores.\
                        output should be only the sentiment and the score, nothing else. Do not write sentiment and score. Just give the answer."
    
    message = [{
        'role':'system',
        'content':system_input},
        {'role':'user',
         'content':user_input
    }]
    return message


def generate_response(user_input, model='gpt-3.5-turbo', temperature = 0.2):

    messages = generate_message(user_input)

    response = client.chat.completions.create(model=model,
                                 messages = messages,
                                 temperature = temperature)
    
    return response.choices[0].message.content
    
def main():

    st.write("Analyse sentiment below: ")

    user_input = st.text_input("Enter your question..")

    with st.spinner():
        if st.button("Get Sentiment"):
            final_answer = generate_response(user_input=user_input)

            st.write(final_answer)



