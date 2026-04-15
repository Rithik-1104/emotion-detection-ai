# 🎭 Emotion Detection AI - LLM-Powered Text Emotion Classifier

A ChatGPT/Claude-like interface for detecting emotions in text using Google's Gemini LLM API.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🎯 Project Overview

**Course:** Natural Language Processing (NLP) Extra Experiment  
**Topic:** Text Emotion Detection using Large Language Models  

This project builds a conversational AI system that detects fine-grained emotions from text input, going beyond basic sentiment analysis (positive/negative) to identify specific emotions like Joy, Sadness, Anger, Fear, Love, Surprise, and Neutral.

### Key Features:
- 💬 **Chat-style Interface** - Looks like ChatGPT/Claude
- 🎭 **7 Emotion Categories** - Fine-grained emotion detection
- 🧠 **LLM-Powered** - Uses Google Gemini API (free)
- 📊 **Confidence Scores** - Shows prediction confidence
- 🔍 **Explanations** - AI explains its reasoning
- 🎨 **Professional UI** - Dark theme with color-coded emotions

## 🚀 Live Demo

**Deploy on Streamlit Cloud (FREE):** [Your Link Here]

## 📋 Emotion Categories

| Emotion | Emoji | Example Text |
|---------|-------|--------------|
| Joy | 😊 | "I got the job! This is amazing!" |
| Sadness | 😢 | "I lost my pet yesterday. Missing them." |
| Anger | 😡 | "This traffic is driving me crazy!" |
| Fear | 😱 | "I'm so worried about my exam tomorrow." |
| Love | 😍 | "I love spending time with my family." |
| Surprise | 😲 | "I can't believe I won the lottery!" |
| Neutral | 😐 | "The meeting is at 3 PM today." |

## 🛠️ Technology Stack

- **Frontend:** Streamlit (Python web framework)
- **LLM API:** Google Gemini 1.5 Flash (Free Tier)
- **Deployment:** Streamlit Cloud (Free hosting)
- **Version Control:** GitHub

## 📦 Installation & Local Setup

### Prerequisites
- Python 3.9 or higher
- Google Gemini API key (free)

### Step 1: Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/emotion-detection-ai.git
cd emotion-detection-ai
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Get Free Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy your API key

### Step 4: Run Locally
```bash
streamlit run emotion_detection_app.py
```

The app will open in your browser at `http://localhost:8501`

## 🌐 Deploy on Streamlit Cloud (FREE)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit: Emotion Detection AI"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/emotion-detection-ai.git
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository: `emotion-detection-ai`
5. Main file path: `emotion_detection_app.py`
6. Click "Deploy"

### Step 3: Enter API Key
Once deployed, enter your Gemini API key in the sidebar.

## 🎓 Project Explanation (For Viva)

### What is This Project?
This is a **Text Emotion Detection System** using Large Language Models (LLMs). Unlike basic sentiment analysis that only detects positive/negative, this project identifies **7 specific emotions** with explanations.

### How Does It Work?

#### 1. **Input Text**
User types a sentence in the chat interface.
```
Example: "I'm so nervous about my exam tomorrow"
```

#### 2. **LLM Processing**
The text is sent to Google's Gemini LLM with a specialized prompt that asks it to:
- Identify the primary emotion
- Calculate confidence score
- Extract emotional keywords
- Explain its reasoning

#### 3. **Emotion Classification**
The LLM analyzes context, word choice, and sentiment indicators to classify into:
- Joy 😊 | Sadness 😢 | Anger 😡 | Fear 😱 | Love 😍 | Surprise 😲 | Neutral 😐

#### 4. **Output with Explanation**
```
Primary Emotion: Fear 😱
Confidence: 85%
Key Indicators: "nervous", "worried", "exam"
Analysis: The text expresses anxiety and concern about an upcoming exam...
```

### Why LLM Instead of Traditional ML?

| Aspect | Traditional ML | LLM (This Project) |
|--------|---------------|-------------------|
| Context Understanding | Limited | Excellent |
| Setup | Needs training data | Pretrained |
| Explanations | No | Yes |
| Accuracy | Good | Better |

### Key Differences: Sentiment vs Emotion

| Analysis Type | Output | Example |
|--------------|--------|---------|
| **Sentiment Analysis** | Positive/Negative | "This movie is great!" → Positive |
| **Emotion Detection** | Specific emotions | "This movie is great!" → Joy 😊 |

**Your main project** (Twitter/Reddit) = Sentiment Analysis  
**This extra experiment** = Emotion Detection (more advanced)

### Technical Architecture

```
User Input → Streamlit UI → Gemini API → Emotion Classification → Formatted Response
```

1. **Frontend:** Streamlit handles the chat interface
2. **API Call:** Text sent to Gemini with emotion detection prompt
3. **Processing:** LLM analyzes text using its vast training
4. **Response:** Returns emotion + confidence + explanation
5. **Display:** Formatted with colors and emojis

### Free Resources Used

| Resource | Cost | Limits |
|----------|------|--------|
| Google Gemini API | FREE | 15 requests/min, 1M tokens/day |
| Streamlit Cloud | FREE | Unlimited apps, 1GB RAM |
| GitHub | FREE | Unlimited public repos |

**Total Cost: ₹0** 💰

## 🎯 Use Cases

1. **Mental Health Analysis** - Detect emotional distress in text
2. **Customer Service** - Analyze customer feedback emotions
3. **Social Media Monitoring** - Track emotional trends
4. **Chatbot Enhancement** - Make bots emotionally aware
5. **Content Moderation** - Flag angry/fearful content

## 🧪 Testing Examples

Try these in the app:

```python
# Joy
"I just got accepted to my dream university!"

# Sadness
"I miss my grandmother. She passed away last month."

# Anger
"I'm so frustrated with this terrible customer service!"

# Fear
"I'm terrified about the medical test results."

# Love
"My partner surprised me with breakfast in bed today."

# Surprise
"I won the lottery! I can't believe this is real!"

# Neutral
"The meeting has been rescheduled to next Tuesday."
```

## 📊 Expected Output Format

```
**Primary Emotion:** Sadness 😢
**Confidence:** 92%
**Key Indicators:** "miss", "passed away", "grandmother"
**Analysis:** The text expresses grief and loss related to the death 
of a loved one. The use of "miss" and past tense indicates ongoing 
sadness about this loss.
```

## 🎤 Viva Questions & Answers

### Q1: How is this different from your main project?
**A:** My main project does sentiment analysis (positive/negative) on Twitter/Reddit data. This extra experiment does emotion detection (7 specific emotions) using an LLM, which is more advanced and provides explanations.

### Q2: Did you train an LLM from scratch?
**A:** No sir/ma'am. We used a pretrained transformer model (Google Gemini) and applied prompt engineering to fine-tune it for emotion classification. Training from scratch would need massive compute resources.

### Q3: What if you don't have LLM access?
**A:** We could use traditional ML with TF-IDF vectorization + Logistic Regression or train a BERT-based classifier on emotion datasets from Kaggle/HuggingFace. But LLM gives better context understanding and explanations.

### Q4: What dataset did you use?
**A:** We used the Gemini LLM which was pretrained on massive text data. For traditional approach, we could use the "Emotion Dataset" from Kaggle with 6 emotion labels.

### Q5: How do you handle API failures?
**A:** We have error handling that catches API exceptions and prompts the user to check their API key. The free tier has 15 requests/minute which is sufficient for demo purposes.

## 📝 Project Structure

```
emotion-detection-ai/
├── emotion_detection_app.py    # Main Streamlit app
├── requirements.txt             # Python dependencies
├── .streamlit/
│   └── config.toml             # Streamlit theme config
├── README.md                    # This file
└── .gitignore                  # Git ignore file
```

## 🔧 Customization

### Change Emotion Categories
Edit the `EMOTION_MAP` dictionary in `emotion_detection_app.py`:
```python
EMOTION_MAP = {
    "joy": ("😊", "emotion-joy"),
    "your_emotion": ("🎭", "emotion-custom"),
    # Add more...
}
```

### Modify Prompt
Edit the `prompt` variable in `analyze_emotion()` function to change how the LLM analyzes text.

## 🐛 Troubleshooting

### "API Key Error"
- Get a new key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- Make sure you copied the full key
- Check if you exceeded free tier limits (15 requests/min)

### "Module Not Found"
```bash
pip install -r requirements.txt --upgrade
```

### App Not Loading on Streamlit Cloud
- Check logs in Streamlit Cloud dashboard
- Ensure all files are pushed to GitHub
- Verify `requirements.txt` is present

## 📚 References

- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Streamlit Documentation](https://docs.streamlit.io)
- [Emotion Detection Paper](https://arxiv.org/abs/2005.00547)

## 👨‍💻 Author

**Your Name**  
[Your GitHub](https://github.com/YOUR_USERNAME) | [Your Email](mailto:your.email@example.com)

## 📄 License

MIT License - Feel free to use this project for your coursework!

---

<div align="center">
    <p>Made with ❤️ for NLP Extra Experiment</p>
    <p>⭐ Star this repo if it helped you!</p>
</div>
