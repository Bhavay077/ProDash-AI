import streamlit as st
import google.generativeai as genai

# 1. SETUP
API_KEY = "PASTE_YOUR_GEMINI_KEY_HERE" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro') # Using 'Pro' for better 3D/logic

# 2. PRO-LEVEL UI/UX
st.set_page_config(page_title="ProDash.AI | Studio", page_icon="💎", layout="wide")

st.markdown("""
    <style>
    .stApp {background-color: #050505; color: #E0E0E0;}
    .sidebar .sidebar-content {background-image: linear-gradient(#111, #050505);}
    .main-header {
        font-size: 50px; font-weight: 900;
        background: linear-gradient(45deg, #00FFA3, #03A9F4, #AF40FF);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .stButton>button {background-color: #1A1C24; border: 1px solid #00FFA3; color: white; border-radius: 20px;}
    </style>
    """, unsafe_allow_html=True)

# 3. THE "INSCRIPTION" SIDEBAR
with st.sidebar:
    st.markdown("<h1 style='color: #00FFA3;'>INSCRIPTION</h1>", unsafe_allow_html=True)
    product_type = st.selectbox("Product Category", ["3D Model (STL/OBJ)", "UI/UX Mockup", "Business Intelligence Dash", "Physical Prototype"])
    complexity = st.select_slider("System Complexity", options=["Draft", "Standard", "Pro", "Enterprise"])
    st.divider()
    st.info(f"Mode: Generating {product_type}")

# 4. MAIN WORKSPACE
st.markdown('<p class="main-header">✦ ProDash.AI Studio</p>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Ready to materialize your concept. Describe the product in detail."}]

for m in st.session_state.messages:
    with st.chat_message(m["role"]): st.markdown(m["content"])

# 5. PRODUCT GENERATION LOGIC
if prompt := st.chat_input("Inscribe your product requirements..."):
    # We add the "Context" from the sidebar automatically
    full_prompt = f"Act as a professional product engineer. Category: {product_type}. Complexity: {complexity}. Task: {prompt}. If 3D, provide specific dimensions and structure."
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Materializing..."):
            response = model.generate_content(full_prompt)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
