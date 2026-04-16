import streamlit as st
import google.generativeai as genai
import os

# 1. THE "CLEAN SLATE" CONFIGURATION
# Get a fresh key from: https://aistudio.google.com/app/apikey
API_KEY = "AQ.Ab8RN6LEo-qIfyXNpzj5_lR4tT2PR4OsdoccD4dto0tRdo5UsA" 

# Force the environment to use this key and use standard web calls (REST)
# This bypasses the '401 Unauthenticated' errors we saw earlier
os.environ["GOOGLE_API_KEY"] = API_KEY
genai.configure(api_key=API_KEY, transport='rest')

# Using the stable model version
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. PREMIUM UI DESIGN (Gemini Dark Aesthetic)
st.set_page_config(page_title="ProDash.AI", page_icon="✦", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #131314; color: #E3E3E3; font-family: 'Inter', sans-serif; }
    header {visibility: hidden;}
    .gemini-title {
        font-size: 42px; font-weight: 600; letter-spacing: -1px;
        background: linear-gradient(90deg, #4285F4, #9B72CB, #D96570);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
    }
    section[data-testid="stSidebar"] { background-color: #1e1e1f !important; border-right: 1px solid #333; }
    .stChatInputContainer { padding-bottom: 20px; background-color: transparent !important; }
    div[data-testid="stChatMessage"] { background-color: transparent !important; border-radius: 15px; }
    </style>
    """, unsafe_allow_html=True)

# 3. DASHBOARD INTERFACE
st.markdown('<p class="gemini-title">✦ ProDash.AI</p>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🛠️ Inscription Studio")
    mode = st.radio("Focus Area", ["3D Product Design", "Business Intelligence", "System Logic"])
    if st.button("Reset Session"):
        st.session_state.messages = []
        st.rerun()

# 4. CHAT LOGIC
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Clean slate achieved. How can I help you build today?"}]

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Ask anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            full_context = f"Mode: {mode}. User Request: {prompt}"
            response = model.generate_content(full_context)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Error: {e}")
