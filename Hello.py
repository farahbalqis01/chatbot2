chatbot.py
# Import necessary libraries
from chatbot import load_model, bot_respond
import streamlit as st
from transformers import pipeline
import requests

# Set the background color using HTML and CSS
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0;  /* Change this to the desired color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Insert title 'My Chatbot App'
st.title('My Chatbot App')

# Sidebar
# Insert a sidebar title 'Sidebar'
st.sidebar.title('Sidebar')
# Insert a sidebar subheader 'Pages'
st.sidebar.subheader('Pages')
# Insert a sidebar selectbox 'Select a page' with options 'Home' and 'Chatbot' and assign it to variable 'app_mode'
app_mode = st.sidebar.selectbox('Select a page', ['Home', 'Chatbot'])

# If app_mode is 'Home'
if app_mode == 'Home':
    # Display 'Chat with me if you feel bored' using st.markdown
    st.markdown('Chat with me if you feel bored')
    # Display any video from youtube using st.video
    st.video('https://youtu.be/Kn1HF3oD19c')
# Else if app_mode is 'Chatbot'
elif app_mode == 'Chatbot':
    # Display 'Please talk to me' using st.text
    st.text('Please talk to me')
    # Call load_model
    load_model()
    # Insert a text input 'You:' and assign it to variable 'text'
    text = st.text_input('You:')
    # If text is not empty
    if text:
        # Display 'Chatbot:' using st.write
        st.write('Chatbot:')
        # While the response is loading, display 'Loading...' using st.spinner
        with st.spinner('Loading...'):
            # Try to get the response from bot_respond(text)
            try:
                response = bot_respond(text)
                # Display the response from bot_respond(text) using st.write
                st.write(response)

                # Add a button to fetch a random joke
                if st.button("Tell me a joke"):
                    joke_generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")
                    joke = joke_generator("Tell me a joke")[0]["generated_text"]
                    st.write("Bot: " + joke)

                # Add sentiment analysis
                sentiment_analyzer = pipeline("sentiment-analysis")
                sentiment_result = sentiment_analyzer(text)
                st.write(f"Sentiment Analysis: {sentiment_result[0]['label']}")

                # Add translation feature
                translation_languages = ["en", "es", "fr", "de", "ms"]  # You can add more languages
                selected_language = st.selectbox("Select a language for translation:", translation_languages)
                if st.button("Translate"):
                    translation_generator = pipeline("translation", model="facebook/mbart-large-50-many-to-many-mmt")
                    translated_text = translation_generator(text, target_language=selected_language)[0]['translation_text']
                    st.write(f"Translated ({selected_language}): {translated_text}")

                # Add a button to display a quote of the day
                if st.button("Quote of the Day"):
                    quote_response = requests.get("https://api.quotable.io/random")
                    quote_data = quote_response.json()
                    quote_text = quote_data["content"]
                    quote_author = quote_data["author"]
                    st.write(f"Quote of the Day: '{quote_text}' - {quote_author}")

            # Handle exceptions
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Run the app:
# py -m streamlit run 6-Advanced1-Chatbot.py

