import os
import streamlit as st
import anthropic


st.title('GENRATE YOUR OWN PROJECT TOPICS')

Department = st.text_input('Enter Your Department')
Educational_Level= st.selectbox('Select Your Educational Level', ('Undergraduate', 'Postgraduate', 'Masters', 'PhD'))
Subject_Interest= st.text_input('Enter Any Area or Subject you are Interested In')

button=st.button('Generate Topics')


if button:
    pass








client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.5,
    system="You are an intelligent assistant specialized in generating academic research topics for various educational levels and departments. Users will provide their department, educational level, and areas of interest. Based on these inputs, your task is to generate five well-defined and current academic research topics, thesis ideas, or dissertation themes that are relevant to their field of study. Ensure the topics are suitable for the specified educational level and reflect current trends and gaps in the literature.\nMatch the complexity and depth of the topics to the user's educational level (e.g., simpler and more focused topics for undergraduates, more complex and comprehensive topics for PhD students).\n",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Task: create 5 research tailor the topics to their specific academic [Department] and [Educational_Level].\nIncorporate the user's [Subject_Interest] to make the topics more personalized and engaging.\nEnsure that the topics are just 5, specific, researchable, and just list the 5 topics. "
                }
            ]
        }
    ]
)
print(message.content)