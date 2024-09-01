import ollama
import streamlit as st

st.title("Chat with ai")
#initialize the messages
if 'messages' not in st.session_state:
    st.session_state['messages'] = []

for message in st.session_state['messages']:
        with st.chat_message("user"):
            st.markdown(message['content'])

if prompt:= st.chat_input('what is up?'):
     st.session_state['messages'].append({'role': 'user', 'content': prompt})

     with st.chat_message('user'):
          st.markdown(prompt)

     with st.chat_message('assistant'):
          response =ollama.chat(
               model='conceptsintamil/tamil-llama-7b-instruct-v0.2',
               messages=st.session_state['messages'],
               stream=False)
     message = response['message'] ['content']
     st.markdown(message)
     st.session_state['messages'].append({'role': 'assistant', 'content': message})


