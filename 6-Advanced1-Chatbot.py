
import numpy as np
import pandas as pd

# import streamlit package
import streamlit as st

# Insert a streamlit title 'My Greeting Streamlit App'
st.title('My Greeting Streamlit App')

# Insert streamlit button 'Say Hello' and assign it to a variable 'btn'
btn = st.button('Say Hello')

# If btn is clicked
if btn:
    # Display 'Hello' on the app using st.text
    st.text('Hello')
# Else
else:
    # Display 'Goodbye' on the app using st.text
    st.text('Goodbye')

# Run the app:
# py -m streamlit run 3-Question2.py
