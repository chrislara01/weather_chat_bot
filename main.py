import streamlit as st
from streamlit_chat import message
from utils.api_utils import api_calling

def main():  
    st.title("Flowise ChatBot")

    if 'messages' not in st.session_state:
        greeting = "Hello! I am a helpful assitant. How may I help you today?"
        
        st.session_state.messages = [{
            'is_user': False,
            'content': greeting
        }]

        message(greeting, avatar_style="miniavs", is_user=False)

    def get_text():
        input_text = st.chat_input("Type your question...", key="input")
        return input_text

    user_input = get_text()

    if user_input:
        output = api_calling(user_input)
        output = output.lstrip("\n")

        # Store the output
        st.session_state['messages'].append({
                'is_user': True,
                'content': user_input
            })
        st.session_state['messages'].append({
            'is_user': False,
            'content': output
        })

        # Display the chat messages
        for message_obj in st.session_state['messages']:
            role = message_obj['is_user']
            content = message_obj['content']
            message(content, avatar_style="icons" if role else "miniavs", is_user=role)

if __name__ == "__main__":
    main()