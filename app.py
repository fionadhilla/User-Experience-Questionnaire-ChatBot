import streamlit as st
from chat import init_cs_bot_session

st.title('AI Chatbot CS Bot')

# Instalasi bot
if 'chat_bot' not in st.session_state:
    st.session_state['chat_bot'] = init_cs_bot_session()

if 'Messages' not in st.session_state:
    st.session_state.Messages = []

# Kolom inputan
user_input = st.chat_input("Say something")

if user_input:
    # Mengirim pesan ke chatbot dan mendapatkan balasan
    try:
        response = st.session_state['chat_bot'].send_message(user_input)
        if response and response.candidates:
            model_answer = response.candidates[0].content.parts[0].text.strip()
        else:
            model_answer = "No response from the model."
    except Exception as e:
        model_answer = f"Error occurred: {e}"

    # Menyimpan pesan pengguna dan balasan model
    st.session_state.Messages.append({"role": "user", "content": user_input})
    st.session_state.Messages.append({"role": "assistant", "content": model_answer})

# Menampilkan pesan di antarmuka
for message in st.session_state.Messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
