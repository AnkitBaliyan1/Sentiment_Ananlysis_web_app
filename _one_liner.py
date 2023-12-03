import streamlit as st
from openai._client import OpenAI

API_KEY = st.secrets['OPENAI_API']
client = OpenAI(api_key=API_KEY)

st.write("Analyse sentiment below: ")

def generate_message(user_input):

    system_input = "Mood Gauge is a specialized sentiment analysis tool designed to \
        present its findings in a distinct, structured format. Each analysis begins with \
            the heading 'Sentiment:', under which it categorizes the text as positive, neutral, \
                or negative. Following this, Mood Gauge provides a 'Score:' ranging from -1 to 1, \
                    where -1 indicates extreme negative sentiment, 0 is neutral, and 1 is extreme \
                        positive. This format ensures that the results are clear and easy to understand, \
                            making Mood Gauge ideal for a wide array of text analyses, from brief social media \
                                snippets to comprehensive reviews. The tool's adaptability in tone, varying from formal \
                                    to conversational based on the text's nature, further enhances its user-friendly appeal and \
                                        analytical precision."
    
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

    user_input = st.text_input("Enter your question..")


    if st.button("Translate"):
        final_answer = generate_response(user_input=user_input)

        st.write(final_answer)



