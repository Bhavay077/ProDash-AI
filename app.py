import streamlit as st
import google.generativeai as genai

# 1. BRAIN SETUP (Update with your key)
API_KEY = "AQ.Ab8RN6LEo-qIfyXNpzj5_lR4tT2PR4OsdoccD4dto0tRdo5UsA"
genai.configure(api_key=API_KEY)
genai.configure(api_key=API_KEY, transport='rest')

model = genai.GenerativeModel('gemini-1.5-flash')

# 2. THE "GEMINI" UI/UX DESIGN
st.set_page_config(page_title="ProDash.AI", page_icon="✦", layout="wide")

st.markdown("""
    <style>
    /* Main Background and Text */
    .stApp {
        background-color: #131314; 
        color: #E3E3E3;
        font-family: 'Inter', sans-serif;
    }
    
    /* Hiding the default Streamlit header */
    header {visibility: hidden;}
    
    /* Gemini-style Glowing Title */
    .gemini-title {
        font-size: 42px;
        font-weight: 600;
        letter-spacing: -1px;
        background: linear-gradient(90deg, #4285F4, #9B72CB, #D96570);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
    }

    /* Professional Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #1e1e1f !important;
        border-right: 1px solid #333;
    }

    /* Chat Input Styling */
    .stChatInputContainer {
        padding-bottom: 20px;
        background-color: transparent !important;
    }
    
    /* Message Bubbles */
    div[data-testid="stChatMessage"] {
        background-color: transparent !important;
        border-radius: 15px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. INTERFACE LAYOUT
st.markdown('<p class="gemini-title">✦ ProDash.AI</p>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🛠️ Inscription Studio")
    product_mode = st.radio("Focus Area", ["3D Product Design", "UI/UX Layout", "Business Logic", "Data Model"])
    st.info(f"Mode: {product_mode} Active")
    if st.button("Clear Workspace"):
        st.session_state.messages = []
        st.rerun()

# 4. CHAT SYSTEM
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How can I help you build today?"}]

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Ask anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # We add the "Inscription" context to the prompt behind the scenes
        full_context = f"Context: The user is in {product_mode} mode. Requirement: {prompt}"
        response = model.generate_content(full_context)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
import time # Add this at the very top of your file

# ... (Keep your UI and Setup code the same) ...

if prompt := st.chat_input("Inscribe your requirements..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            full_context = f"Context: {product_mode}. Requirement: {prompt}"
            response = model.generate_content(full_context)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            if "429" in str(e):
                st.error("🚦 Traffic Jam! Google's free tier is busy. Please wait 30 seconds and try again.")
            else:
                st.error(f"An unexpected error occurred: {e}")
                import streamlit as st
