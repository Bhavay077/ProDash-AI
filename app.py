import streamlit as st
import ollama

# 1. Page Config
st.set_page_config(page_title="ProDash.AI", page_icon="🚀", layout="wide")

# 2. Professional Styling (CSS)
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    /* Header Styling */
    .main-header {
        font-size: 45px;
        font-weight: 800;
        background: -webkit-linear-gradient(#00FFA3, #03A9F4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px;
    }
    /* Chat Bubbles */
    .stChatMessage {
        background-color: #1A1C24;
        border-radius: 15px;
        border: 1px solid #30363D;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.markdown("<h1 style='color: #00FFA3;'>ProDash.AI</h1>", unsafe_allow_html=True)
    st.caption("Advanced Analytics Workspace")
    st.divider()
    if st.button("Clear Workspace"):
        st.session_state.messages = []
        st.rerun()

# 4. Main Interface
st.markdown('<p class="main-header">✦ ProDash.AI</p>', unsafe_allow_html=True)
st.markdown("---")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. Interactive Chat
if prompt := st.chat_input("Ask ProDash anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Processing..."):
            try:
                response = ollama.chat(model='llama3', messages=[{'role': 'user', 'content': prompt}])
                full_response = response['message']['content']
                st.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"System Error: {e}")
