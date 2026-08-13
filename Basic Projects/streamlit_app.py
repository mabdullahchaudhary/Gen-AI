import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_groq import ChatGroq

load_dotenv()

st.set_page_config(page_title="GenAI Assistant", page_icon="🤖")
st.title("My Full Stack Gen AI")

with st.sidebar:
    st.header("Bot Settings")
    selection_persona = st.selectbox(
        "Choose bot persona: ",
        ["Friendly Assistant", "Sarcastic Senior Dev", "Kindergarten Teacher"],
    )

persona_prompts = {
    "Friendly Assistant": "You are a helpful and polite AI assistant. Keep answers concise.",
    "Sarcastic Senior Dev": "You are a highly experienced but sarcastic senior developer. Roast the user lightly for asking questions, then give a perfect short answer.",
    "Kindergarten Teacher": "You are a sweet kindergarten teacher. Explain concepts using simple words, emojis, and examples of toys or candies.",
}

@st.cache_resource
def get_llm():
    return ChatGroq(model="llama-3.3-70b-versatile", temperature=0.4)

llm = get_llm()

# CORRECTION 1: Changed "message" to "messages" to match your list variable
if "messages" not in st.session_state or st.session_state.get("current_persona") != selection_persona:
    st.session_state.messages = [
        SystemMessage(content=persona_prompts[selection_persona])
    ]
st.session_state.current_persona = selection_persona

for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# CORRECTION 2: Changed st.chat_message to st.chat_input
if user_input := st.chat_input("Type your message here"):
    with st.chat_message("user"):
        st.write(user_input)
    
    st.session_state.messages.append(HumanMessage(content=user_input))

    with st.spinner("Thinking....."):
        response = llm.invoke(st.session_state.messages)

    with st.chat_message("assistant"):
        st.write(response.content)

    st.session_state.messages.append(AIMessage(content=response.content))