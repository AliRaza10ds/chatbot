
import streamlit as st
from model import model, text_to_speech
from PIL import Image
import time

st.set_page_config(
    page_title="Multilingual AI Assistant",
    page_icon="🧠",
    layout="centered",
)

st.markdown(
    "<h1 style='text-align: center; color: #4B8BBE;'>🌐 Multilingual AI Assistant</h1>",
    unsafe_allow_html=True,
)
st.markdown("<h4 style='text-align: center; color: gray;'>Ask anything in any language and get spoken answers!</h4>", unsafe_allow_html=True)
st.markdown("---")

st.markdown("### ✍ Ask your question:")
user_input = st.text_input("Type your question here...")


if st.button("🚀 Get Response") and user_input.strip():
    with st.spinner("💡 Model is thinking..."):
        time.sleep(1)
        reply = model(user_input)


    st.markdown("### 🤖 AI Response:")
    st.success(reply)


    st.markdown("### 🔊 Listen to AI:")
    audio_bytes = text_to_speech(reply, lang='en')
    st.audio(audio_bytes, format='audio/mp3')

elif user_input.strip() == "":
    st.info("Please enter a question to get started.")


st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Made with ❤ using Streamlit, Gemini AI & gTTS</p>",
    unsafe_allow_html=True
)