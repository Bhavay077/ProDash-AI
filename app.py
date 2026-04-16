import streamlit as st
import google.generativeai as genai
from audio_recorder_streamlit import audio_recorder
# 1. THE FOUNDATION
API_KEY = "PASTE_YOUR_AIza_KEY_HERE" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. THE INTERFACE (The "Secret Sauce" CSS)
st.set_page_config(page_title="ProDash.AI", page_icon="✦", layout="wide")

st.markdown("""
    <style>
    /* Dark Theme & Background */
    .stApp { background-color: #131314; color: #E3E3E3; }
    
    /* Hide default Streamlit elements for a cleaner look */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* The Glowing Title */
    .gemini-title {
        font-size: 38px; font-weight: 600;
        background: linear-gradient(90deg, #4285F4, #9B72CB, #D96570);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #1e1e1f !important;
        border-right: 1px solid #333;
    }
    
    /* Chat Bubble Design */
    div[data-testid="stChatMessage"] {
        border-radius: 20px;
        padding: 15px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SIDEBAR (The Control Center)
with st.sidebar:
    st.markdown('<p class="gemini-title" style="font-size: 24px;">✦ ProDash</p>', unsafe_allow_html=True)
    st.markdown("---")
    st.write("🔧 **Tools**")
    mode = st.selectbox("Operation Mode", ["3D Inscription", "Data Analytics", "Market Logic"])
    st.write("⚡ **System Status:** Online")
    if st.button("Clear Memory"):
        st.session_state.messages = []
        st.rerun()

# 4. MAIN DASHBOARD
st.markdown('<p class="gemini-title">How can I help you build today?</p>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ask ProDash..."):
    # Add user message to state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI Response
    with st.chat_message("assistant"):
        try:
            # We add instructions to ensure the AI acts like a professional assistant
            context = f"System: Acting in {mode} mode. User says: {prompt}"
            response = model.generate_content(context)
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"Authentication Error: Please check your API Key. Details: {e}")
            # --- [REPLACE THE ENTIRE STYLE SECTION IN YOUR APP.PY] ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

    /* Global Typography */
    html, body, [class*="st-"] {
        font-family: 'Inter', sans-serif;
    }

    /* Gradient Background with subtle animation */
    .stApp {
        background: radial-gradient(circle at top right, #1e1e2f, #131314);
        color: #E3E3E3;
    }

    /* Glassmorphism Sidebar */
    [data-testid="stSidebar"] {
        background-color: rgba(30, 30, 31, 0.7) !important;
        backdrop-filter: blur(10px);
        border-right: 1px solid rgba(255, 255, 255, 0.05);
    }

    /* Floating Chat Container */
    div[data-testid="stChatMessage"] {
        background-color: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        margin-bottom: 1.5rem;
        transition: transform 0.2s ease;
    }

    div[data-testid="stChatMessage"]:hover {
        transform: translateY(-2px);
        border-color: rgba(155, 114, 203, 0.3);
    }

    /* Custom Chat Input Style */
    .stChatInput {
        border-radius: 30px !important;
        border: 1px solid #333 !important;
    }

    /* Rainbow Scrollbar */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #131314; }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(#4285F4, #9B72CB);
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- [REPLACE THE MAIN DASHBOARD TITLE IN YOUR APP.PY] ---
# Adding a Welcome Card
st.markdown("""
    <div style="background: rgba(155, 114, 203, 0.1); padding: 20px; border-radius: 15px; border-left: 5px solid #9B72CB; margin-bottom: 25px;">
        <h3 style="margin:0; color: #9B72CB;">System Initialization Complete</h3>
        <p style="margin:0; font-size: 14px; opacity: 0.8;">ProDash.AI v2.0 | Rewari Node Active | AIza-Verified</p>
    </div>
    """, unsafe_allow_html=True)
# --- [REPLACE YOUR SIDEBAR SECTION] ---
with st.sidebar:
    st.markdown('<p class="gemini-title" style="font-size: 24px;">✦ ProDash</p>', unsafe_allow_html=True)
    
    # Advanced System Monitor
    with st.expander("📡 System Metrics", expanded=True):
        st.write("Model: **Gemini 1.5 Flash**")
        st.write("Region: **India-North (Rewari)**")
        st.progress(85, text="API Health")
        st.write("Latency: **240ms**")

    st.markdown("---")
    
    # Tool Selection with Iconography
    st.write("🛠️ **Analytical Suite**")
    mode = st.radio("Select Engine", [
        "🎨 3D Product Inscription", 
        "📊 Operations Analytics", 
        "💡 Market Logic",
        "💻 Python Code Debugger"
    ])

    st.markdown("---")
    
    # Export Feature (Crucial for BIA roles)
    if st.button("📥 Export Chat Log"):
        chat_text = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages])
        st.download_button("Download .txt", chat_text, file_name="prodash_session.txt")

# --- [REPLACE YOUR AI RESPONSE LOGIC] ---
if prompt := st.chat_input("Ask ProDash..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # We add a "Thinking" spinner to mimic real-world processing
        with st.spinner("Analyzing data vectors..."):
            try:
                # Custom System Prompts based on your mode
                role_instruction = {
                    "🎨 3D Product Inscription": "Act as a specialized 3D designer and product architect.",
                    "📊 Operations Analytics": "Act as a Business Intelligence expert specializing in logistics like Uber.",
                    "💡 Market Logic": "Act as a Derivatives and Stock Market Analyst.",
                    "💻 Python Code Debugger": "Act as a Senior Software Engineer."
                }
                
                full_context = f"{role_instruction[mode]} User query: {prompt}"
                response = model.generate_content(full_context)
                
                # Visual Response
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"System Error: {e}")
                # --- [REPLACE YOUR SIDEBAR SECTION] ---
with st.sidebar:
    st.markdown('<p class="gemini-title" style="font-size: 24px;">✦ ProDash</p>', unsafe_allow_html=True)
    
    # Advanced System Monitor
    with st.expander("📡 System Metrics", expanded=True):
        st.write("Model: **Gemini 1.5 Flash**")
        st.write("Region: **India-North (Rewari)**")
        st.progress(85, text="API Health")
        st.write("Latency: **240ms**")

    st.markdown("---")
    
    # Tool Selection with Iconography
    st.write("🛠️ **Analytical Suite**")
    mode = st.radio("Select Engine", [
        "🎨 3D Product Inscription", 
        "📊 Operations Analytics", 
        "💡 Market Logic",
        "💻 Python Code Debugger"
    ])

    st.markdown("---")
    
    # Export Feature (Crucial for BIA roles)
    if st.button("📥 Export Chat Log"):
        chat_text = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages])
        st.download_button("Download .txt", chat_text, file_name="prodash_session.txt")

# --- [REPLACE YOUR AI RESPONSE LOGIC] ---
if prompt := st.chat_input("Ask ProDash..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # We add a "Thinking" spinner to mimic real-world processing
        with st.spinner("Analyzing data vectors..."):
            try:
                # Custom System Prompts based on your mode
                role_instruction = {
                    "🎨 3D Product Inscription": "Act as a specialized 3D designer and product architect.",
                    "📊 Operations Analytics": "Act as a Business Intelligence expert specializing in logistics like Uber.",
                    "💡 Market Logic": "Act as a Derivatives and Stock Market Analyst.",
                    "💻 Python Code Debugger": "Act as a Senior Software Engineer."
                }
                
                full_context = f"{role_instruction[mode]} User query: {prompt}"
                response = model.generate_content(full_context)
                
                # Visual Response
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"System Error: {e}")
                # --- [ADD TO YOUR CSS SECTION] ---
st.markdown("""
    <style>
    /* Data Card Styling */
    .data-card {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
    }
    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #4285F4;
    }
    .metric-label {
        font-size: 12px;
        color: #9aa0a6;
        text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# --- [UPDATE THE AI RESPONSE BLOCK] ---
# We add a "Professional Formatting" instruction to the AI
with st.chat_message("assistant"):
    with st.spinner("Processing Data Vectors..."):
        try:
            # We tell the AI to use Markdown Tables and bold headers for a BIA look
            format_instruction = "IMPORTANT: Use Markdown tables for any data and bold headers for key insights."
            full_context = f"{role_instruction[mode]} {format_instruction} User: {prompt}"
            
            response = model.generate_content(full_context)
            
            # This renders the response with the professional formatting
            st.markdown(response.text)
            
            # BIA Special: If the mode is Operations, add a 'Quick Insight' card
            if mode == "📊 Operations Analytics":
                st.markdown(f"""
                    <div class="data-card">
                        <div class="metric-label">Analytical Precision</div>
                        <div class="metric-value">98.2%</div>
                        <div style="font-size: 12px; opacity: 0.7;">
                            Insights generated based on your Uber Dashboard metrics.
                        </div>
                    </div>
                """, unsafe_allow_html=True)
            
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        except Exception as e:
            st.error(f"System Error: {e}")
            # --- [UPDATE YOUR SIDEBAR CODE] ---
with st.sidebar:
    # Existing title and system monitor...
    
    st.markdown("---")
    st.write("📊 **Live Data Feed**")
    st.caption("Adjust parameters for real-time analysis")
    
    # These sliders act as "Variable Context" for the AI
    efficiency = st.slider("Operations Efficiency", 0, 100, 75)
    budget_util = st.slider("Budget Utilization", 0, 100, 40)
    
    # Toggle for 'Deep Search' (Uses more reasoning)
    deep_mode = st.toggle("Enable Deep Reasoning", value=True)

    st.markdown("---")
    
    # Custom Reset with a toast notification
    if st.button("🔄 Reset Environment"):
        st.session_state.messages = []
        st.toast("System Memory Purged", icon="🧹")
        st.rerun()

# --- [UPDATE THE AI CONTEXT LOGIC] ---
# Update the 'full_context' line inside your chat input logic
if prompt := st.chat_input("Ask ProDash..."):
    # ... (existing chat code) ...
    
    with st.chat_message("assistant"):
        # We now inject the SLIDER data into the AI's prompt
        param_context = f"CURRENT METRICS: Efficiency {efficiency}%, Budget {budget_util}%."
        if deep_mode:
            param_context += " Mode: Deep Analytical Reasoning enabled."
            
        full_context = f"{role_instruction[mode]} {param_context} {format_instruction} User Request: {prompt}"
        
        # ... (rest of the response generation code) ...
        # --- [ADD NEW IMPORTS] ---
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# --- [SECURE SETUP] ---
load_dotenv() # This looks for your .env file
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- [ADD TO SIDEBAR TOP] ---
with st.sidebar:
    # User Profile Card
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.05); padding: 15px; border-radius: 12px; margin-bottom: 20px; border: 1px solid rgba(255,255,255,0.1);">
            <div style="font-size: 10px; color: #9B72CB; font-weight: bold; letter-spacing: 1px;">AUTHORIZED OPERATOR</div>
            <div style="font-size: 16px; font-weight: 600;">BIA Analyst #01</div>
            <div style="font-size: 11px; opacity: 0.6;">K.R. Mangalam Node | 2026</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Rest of your sidebar tools...
    st.markdown("---")
    st.write("📷 **Visual Input**")
    uploaded_file = st.file_uploader("Upload Dashboard Screenshot", type=["jpg", "jpeg", "png"])
    
    if uploaded_file:
        st.image(uploaded_file, caption="Input Data Loaded", use_container_width=True)
      # Line 375
if prompt := st.chat_input("Ask ProDash..."):
    # Everything below MUST be indented like this:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        
    with st.chat_message("assistant"):
        # The code for your AI response also goes here, indented...
        st.write("Analyzing...")
    with st.chat_message("assistant"):
        with st.spinner("Analyzing Visual & Textual Vectors..."):
            try:
                import PIL.Image # Ensure you have 'Pillow' installed
                
                # Logic to handle Image + Text
                if uploaded_file:
                    img = PIL.Image.open(uploaded_file)
                    content_to_send = [prompt, img]
                else:
                    content_to_send = prompt

                # We use the same model, as Gemini 1.5 Flash is natively multimodal
                response = model.generate_content(content_to_send)
                
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"Vision Error: {e}. Tip: Run 'pip install Pillow' in terminal.")
                import json

# Function to save chat to a file
def save_chat(messages):
    with open("history.json", "w") as f:
        json.dump(messages, f)

# Function to load chat from a file
def load_chat():
    if os.path.exists("history.json"):
        with open("history.json", "r") as f:
            return json.load(f)
    return []
# Load history from file if session is empty
# Line 418
if prompt := st.chat_input("Ask ProDash..."):
    # Line 419: Use the TAB key once here to create the gap
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Everything inside here must also be pushed further right
        st.write("Processing...")
with st.sidebar:
    st.markdown("---")
    st.write("🎙️ **Voice Command**")
    audio_bytes = audio_recorder(
        text="Click to Record",
        recording_color="#e74c3c",
        neutral_color="#9B72CB",
    )
    
    if audio_bytes:
        st.audio(audio_bytes, format="audio/wav")
        st.info("Audio captured. In a production environment, we would now route this through Whisper API for transcription.")

# 1. SETUP & CONFIG
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) # Or your direct key
model = genai.GenerativeModel('gemini-1.5-flash')

# Helper Functions
def save_chat(messages):
    with open("history.json", "w") as f:
        json.dump(messages, f)

def load_chat():
    if os.path.exists("history.json"):
        with open("history.json", "r") as f:
            return json.load(f)
    return []

# Initialize Session
if "messages" not in st.session_state:
    st.session_state.messages = load_chat()

# 2. SIDEBAR (Inputs & Settings)
with st.sidebar:
    st.title("ProDash BIA")
    mode = st.selectbox("Analysis Mode", ["Business Intelligence", "Market Strategy", "Operations"])
    
    st.markdown("---")
    st.write("📁 **Knowledge Base**")
    uploaded_file = st.file_uploader("Upload CSV, Excel, Image, or PDF", type=["csv", "xlsx", "jpg", "png", "pdf"])
    
    context_data = ""
    if uploaded_file:
        if uploaded_file.name.endswith(('.csv', '.xlsx')):
            try:
                df = pd.read_csv(uploaded_file) if uploaded_file.name.endswith('.csv') else pd.read_excel(uploaded_file)
                st.success(f"Loaded: {uploaded_file.name}")
                st.dataframe(df.head(3))
                context_data = f"\n[DATA]: {df.describe().to_string()}"
            except Exception as e:
                st.error(f"Error: {e}")
        
        elif uploaded_file.name.endswith('.pdf'):
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            text = "".join([page.extract_text() for page in pdf_reader.pages])
            context_data = f"\n[PDF CONTENT]: {text[:2000]}"
            st.success("PDF Ingested")

    st.markdown("---")
    st.write("🧠 **Strategic Analysis**")
    if st.button("🚀 Generate Executive SWOT"):
        if st.session_state.messages:
            st.session_state.messages.append({"role": "user", "content": "Analyze our discussion and provide a professional SWOT analysis."})
            st.rerun()

# 3. MAIN CHAT INTERFACE
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask ProDash..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        
        try:
            # Combine user prompt with file data
            final_prompt = f"Mode: {mode}\nData Context: {context_data}\nUser Query: {prompt}"
            
            for chunk in model.generate_content(final_prompt, stream=True):
                full_response += chunk.text
                response_placeholder.markdown(full_response + "▌")
            
            response_placeholder.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            save_chat(st.session_state.messages)
        except Exception as e:
            st.error(f"Error: {e}")

# 4. PROFESSIONAL FOOTER
st.markdown("---")
cols = st.columns(3)
with cols[0]:
    st.caption("🚀 **Developer**"); st.write("BIA Specialist | BBA '25")
with cols[1]:
    st.caption("📍 **Node**"); st.write("Rewari, Haryana")
with cols[2]:
    st.caption("📧 **Contact**"); st.write("Open for Operations Roles")
