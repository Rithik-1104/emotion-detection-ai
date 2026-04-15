import streamlit as st
import google.generativeai as genai
import time
from datetime import datetime
import os

# ============================
# Configure Gemini API (FIXED)
# ============================
api_key = os.getenv("GEMINI_API_KEY")

# Page configuration
st.set_page_config(
    page_title="Emotion Detection AI",
    page_icon="🎭",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for chat-like interface
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
    }
    .stTextInput > div > div > input {
        background-color: #262730;
        color: white;
        border-radius: 10px;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .user-message {
        background-color: #2b313e;
        border-left: 4px solid #4CAF50;
    }
    .assistant-message {
        background-color: #1e2128;
        border-left: 4px solid #2196F3;
    }
    .emotion-badge {
        display: inline-block;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-weight: bold;
        margin: 0.5rem 0;
        font-size: 1.1rem;
    }
    .emotion-joy { background-color: #4CAF50; color: white; }
    .emotion-sadness { background-color: #2196F3; color: white; }
    .emotion-anger { background-color: #f44336; color: white; }
    .emotion-fear { background-color: #9C27B0; color: white; }
    .emotion-love { background-color: #E91E63; color: white; }
    .emotion-surprise { background-color: #FF9800; color: white; }
    .emotion-neutral { background-color: #607D8B; color: white; }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "api_key" not in st.session_state:
    st.session_state.api_key = api_key
if "example_text" not in st.session_state:
    st.session_state.example_text = None

# Emotion mapping with emojis
EMOTION_MAP = {
    "joy": ("😊", "emotion-joy"),
    "happiness": ("😊", "emotion-joy"),
    "sadness": ("😢", "emotion-sadness"),
    "sad": ("😢", "emotion-sadness"),
    "anger": ("😡", "emotion-anger"),
    "angry": ("😡", "emotion-anger"),
    "fear": ("😱", "emotion-fear"),
    "scared": ("😱", "emotion-fear"),
    "love": ("😍", "emotion-love"),
    "surprise": ("😲", "emotion-surprise"),
    "surprised": ("😲", "emotion-surprise"),
    "neutral": ("😐", "emotion-neutral"),
    "disgust": ("🤢", "emotion-anger"),
    "excitement": ("🤩", "emotion-joy"),
}

def get_emotion_emoji(emotion_text):
    """Extract emotion and return emoji with CSS class"""
    emotion_lower = emotion_text.lower()
    for key, (emoji, css_class) in EMOTION_MAP.items():
        if key in emotion_lower:
            return emoji, css_class, key.capitalize()
    return "🎭", "emotion-neutral", "Mixed"

def analyze_emotion(text, api_key):
    """Analyze emotion using Gemini API"""
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"""You are an expert emotion detection AI. Analyze the following text and:
1. Identify the PRIMARY emotion from: Joy, Sadness, Anger, Fear, Love, Surprise, Neutral
2. Provide a confidence score (0-100%)
3. Give a brief 2-3 sentence explanation of why you detected this emotion
4. Highlight key emotional words/phrases

Text: "{text}"

Format your response EXACTLY like this:
**Primary Emotion:** [Emotion Name]
**Confidence:** [XX]%
**Key Indicators:** [list emotional words/phrases]
**Analysis:** [Your 2-3 sentence explanation]
"""
        
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Sidebar
with st.sidebar:
    st.title("🎭 Emotion AI Settings")
    
    if st.session_state.api_key:
        st.success("✅ API Key configured!")
    else:
        st.error("❌ API key missing! Add it in environment variables.")
    
    st.divider()
    
    st.markdown("### 📊 Emotion Categories")
    st.markdown("""
    - 😊 **Joy**
    - 😢 **Sadness**
    - 😡 **Anger**
    - 😱 **Fear**
    - 😍 **Love**
    - 😲 **Surprise**
    - 😐 **Neutral**
    """)
    
    st.divider()
    
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("### 💡 Try These Examples:")
    examples = [
        "I just got promoted at work! This is amazing!",
        "I lost my pet yesterday. I miss them so much.",
        "This traffic is driving me crazy!",
        "I'm worried about my exam tomorrow.",
        "I love spending time with my family."
    ]
    
    for example in examples:
        if st.button(f"📝 {example[:30]}...", use_container_width=True, key=example):
            st.session_state.example_text = example

# Main chat interface
st.title("🎭 Emotion Detection AI")
st.markdown("*An LLM-powered system for fine-grained emotion analysis*")

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"""
        <div class="chat-message user-message">
            <b>👤 You:</b><br>
            {message["content"]}
        </div>
        """, unsafe_allow_html=True)
    else:
        emoji, css_class, emotion_name = get_emotion_emoji(message["content"])
        
        st.markdown(f"""
        <div class="chat-message assistant-message">
            <b>🤖 Emotion AI:</b><br>
            <span class="emotion-badge {css_class}">{emoji} {emotion_name}</span><br>
            {message["content"].replace('**', '<b>').replace('**', '</b>')}
        </div>
        """, unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Type your text here to analyze emotions...")

if st.session_state.example_text:
    user_input = st.session_state.example_text
    st.session_state.example_text = None

# Process input
if user_input:
    if not st.session_state.api_key:
        st.error("⚠️ API key missing!")
    else:
        st.session_state.messages.append({"role": "user", "content": user_input})
        
        with st.spinner("🔍 Analyzing emotions..."):
            time.sleep(0.5)
            response = analyze_emotion(user_input, st.session_state.api_key)
            
            st.session_state.messages.append({"role": "assistant", "content": response})
        
        st.rerun()

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem;'>
    <p>🎓 <b>NLP Project:</b> Text Emotion Detection using LLM | Built with Gemini API & Streamlit</p>
    <p style='font-size: 0.9rem;'>Detects 7 emotion categories</p>
</div>
""", unsafe_allow_html=True)
