import streamlit as st
import aawaz.core.assistant as assistant
from aawaz.audio.stt import listen
import os
import time

STOPWATCH_FILE = ".stopwatch_state"

# 1. Page Configuration
st.set_page_config(
    page_title="Aawaz AI Assistant",
    page_icon="🎙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for Premium Look
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stChatFloatingInputContainer {
        padding-bottom: 20px;
    }
    .ai-card {
        background-color: #1e2227;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #30363d;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    .big-title {
        font-size: 100px !important;
        font-weight: 950 !important;
        background: linear-gradient(90deg, #ffffff 0%, #777777 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0px !important;
        letter-spacing: -3px !important;
        line-height: 1 !important;
    }
    .subtitle {
        color: #8892b0;
        font-size: 24px;
        margin-top: -10px;
        margin-bottom: 50px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="big-title">🎙️ Aawaz AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">The Next-Gen Agentic Virtual Assistant</div>', unsafe_allow_html=True)

# 3. Session State Initialization
if "history" not in st.session_state:
    st.session_state.history = []
if "last_decision" not in st.session_state:
    st.session_state.last_decision = {}

# 4. Sidebar for Voice (Optional) or just keep it in main
with st.sidebar:
    st.header("Voice Controls")
    speak_btn = st.button("🎤 Start Listening", use_container_width=True)
    
    st.write("---")
    st.header("⚡ Quick Actions")
    if st.button("🌤 Weather", use_container_width=True):
        st.session_state.quick_query = "What is the weather?"
    if st.button("🎵 Play Music", use_container_width=True):
        st.session_state.quick_query = "Play some relaxing music"
    if st.button("📰 News", use_container_width=True):
        st.session_state.quick_query = "Tell me the latest news"
    if st.button("🏏 IPL Score", use_container_width=True):
        st.session_state.quick_query = "What is the live IPL score?"

    st.write("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.history = []
        st.session_state.last_decision = {}
        st.session_state.quick_query = None
        st.rerun()

# 5. Main Layout
chat_col, ai_col = st.columns([2, 1], gap="large")

with chat_col:
    st.subheader("💬 Conversation")
    
    # Container for scrollable chat
    chat_container = st.container()
    
    with chat_container:
        for speaker, text in st.session_state.history:
            role = "user" if speaker == "You" else "assistant"
            with st.chat_message(role):
                st.write(text)

    # Chat Input
    user_input = st.chat_input("How can I help you today?")

with ai_col:
    st.subheader("📊 System Status")
    if os.path.exists(STOPWATCH_FILE):
        with open(STOPWATCH_FILE, "r") as f:
            start_time = float(f.read())
        elapsed = time.time() - start_time
        mins, secs = divmod(elapsed, 60)
        st.success(f"⏱️ **Stopwatch:** {int(mins)}m {int(secs)}s running")
    else:
        st.info("No active background tasks.")

    st.subheader("🧠 AI Transparency Panel")
    with st.container():
        if st.session_state.last_decision:
            d = st.session_state.last_decision
            st.markdown(f"""
            <div class="ai-card">
                <p><b>Selected Tool:</b> <code>{d.get('tool', 'N/A')}</code></p>
                <p><b>Confidence:</b> <code>{d.get('confidence', 'N/A')}</code></p>
                <hr style="border: 0.5px solid #30363d;">
                <p><b>Intent Reasoning:</b><br>{d.get('intent', 'N/A')}</p>
                <p><b>Extracted Parameters:</b><br><code>{d.get('parameter', '{}')}</code></p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Ask Aawaz something to see the agent's decision-making process.")
            
    # Expandable Debug Log for internal JSON
    st.write("---")
    with st.expander("🔍 System Debug Log"):
        if st.session_state.last_decision:
            st.json(st.session_state.last_decision)
        else:
            st.write("No active session data.")

# 6. Logic Execution
query_to_run = None

# Priority: Chat Input > Quick Actions > Voice
if user_input:
    query_to_run = user_input
elif "quick_query" in st.session_state and st.session_state.quick_query:
    query_to_run = st.session_state.quick_query
    st.session_state.quick_query = None # Clear it after use

if speak_btn:
    with st.spinner("Listening..."):
        query_to_run = listen()
        if not query_to_run or query_to_run == "None":
            st.warning("Could not hear anything clearly. Please try again.")
            query_to_run = None
        else:
            st.success(f"You said: {query_to_run}")

if query_to_run:
    with st.spinner("Thinking..."):
        result = assistant.handle_query(query_to_run)
    
    st.session_state.last_decision = result
    display_text = result.get("response", "Command executed successfully.")
    
    st.session_state.history.append(("You", query_to_run))
    st.session_state.history.append(("Aawaz", display_text))
    st.rerun()
