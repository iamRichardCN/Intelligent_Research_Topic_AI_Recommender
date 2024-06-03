import os
import streamlit as st
import anthropic

client = anthropic.Client(os.environ.get("ANTHROPIC_API_KEY"))

st.title('GENERATE YOUR OWN PROJECT TOPICS')
Department = st.text_input('Enter Your Department')
Educational_Level = st.selectbox('Select Your Educational Level', ('Undergraduate', 'Postgraduate', 'Masters', 'PhD'))
Subject_Interest = st.text_input('Enter Any Area or Subject you are Interested In')
button = st.button('Generate Topics')

if button:
    message = client.send_message(
        model="claude-v1",
        prompt=f"You are an intelligent assistant specialized in generating academic research topics for {Educational_Level} educational levels and {Department}. Users will provide their department, educational level, and {Subject_Interest} area of interest. Based on these inputs, your task is to generate five well-defined and current academic research topics, thesis ideas, or dissertation themes that are relevant to their field of study. Ensure the topics are suitable for the specified educational level and reflect current trends and gaps in the literature.\nMatch the complexity and depth of the topics to the user's educational level (e.g., simpler and more focused topics for undergraduates, more complex and comprehensive topics for PhD students).\n\nTask: Create 5 research topics tailored to their specific academic {Department} and {Educational_Level}. Incorporate the user's {Subject_Interest} to make the topics more personalized and engaging. Ensure that the topics are just 5, specific, researchable, and just list the 5 topics.",
        max_tokens=1000,
        temperature=0.5,
    )
    st.write(message.response)
