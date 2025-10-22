<h1 align="center">✨ Transcend ✨</h1>
<h3 align="center">🧠 AI-Powered Handwriting Recognition Chat Assistant</h3>
<p align="center">
  <em>Smart Assistant: Handwritten Digit & Text Recognition Powered by AI</em>
</p>

---

## 🚀 Overview

**Transcend** is an AI-driven web application that bridges the gap between handwritten input and intelligent conversational AI.  
It allows users to **upload handwritten text or notes**, automatically extract the text using **deep learning-based OCR (TrOCR)**, and get meaningful, conversational responses via an **AI chatbot** powered by OpenAI GPT models.

### 🎯 Problem Solved
Traditional OCR tools like Tesseract struggle to read cursive or inconsistent handwriting.  
**Transcend** overcomes this limitation using **Microsoft’s TrOCR (Transformer-based OCR)**, enabling accurate recognition and understanding of handwritten text.

---

## 🧩 Tech Stack

| **Layer** | **Technologies Used** |
|------------|------------------------|
| 🖥️ **Frontend** | HTML • CSS • JavaScript |
| ⚙️ **Backend** | Python • Flask |
| 🧠 **AI / ML Models** | Microsoft TrOCR (Hugging Face Transformers) • OpenAI GPT |
| 💾 **Database** | SQLite (for user authentication) |
| 🧰 **Libraries** | Flask-SQLAlchemy • Torch • Transformers • Pillow • Werkzeug |
| 🧑‍💻 **Environment** | Local Flask Development Server |

---

## 🌟 Features

### 🏠 Homepage
- A clean and welcoming interface introducing the app’s purpose.
- Navigation to login, signup, or chat interface.

### 🔐 Authentication
- Secure **Signup/Login** using Flask sessions.
- Passwords safely hashed using **Werkzeug**.

### 💬 Chat Interface
- Interactive chat UI (ChatGPT-style).
- Supports:
  - ✍️ **Handwritten image upload**
  - 📷 **Live camera capture**
  - 💬 **Text input**
  - 🎤 **Voice input (speech-to-text)**
- Real-time AI responses with **text-to-speech playback**.

### ✍️ OCR (Optical Character Recognition)
- Integrated **Microsoft TrOCR** for advanced handwriting extraction.
- Displays recognized text in an editable box with:
  - 🧠 Grammar correction
  - 🪄 Summarization
  - 🔁 Resubmission to chatbot

### 🧭 Additional UI Enhancements
- Modern animated loaders.
- Image preview & lightbox .
- Responsive design for mobile and desktop.

### 📸 Image Handling
- Upload or capture handwritten text.
- Preview before processing.
- Extracted text is displayed in a separate section.

###💡 Usage Instructions
- Once the app is running:
  1. Register / Login to access the main chat interface.
  2. Use the chatbox to type queries or upload handwritten images.
  3. The system will:
     - Extract text using TrOCR.
     - Display it for your review.
     - Generate an AI-powered response.
  4. Optionally, use:
     - 🎤 Microphone input for voice commands.
     - 📷 Camera capture for handwritten notes.
     - ✍️ OCR editor for correcting extracted text before resubmission.
  5. Chat responses appear in real-time, with text-to-speech support for accessibility.

###🧩 Folder Structure
Transcend-Project/
│
├── app.py                # Main Flask application
├── static/
│   ├── style.css         # Frontend styling
│   ├── script.js         # Client-side chat and OCR logic
│   └── uploads/          # Temporary image storage
│
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── signup.html
│   └── index.html        # Chat interface
│
├── database.db           # SQLite database
├── requirements.txt      # Dependencies
└── README.md             # Project documentation

###🏁 Conclusion
- Transcend demonstrates the potential of combining OCR, AI, and Flask web development to create a truly interactive, intelligent assistant.
It represents a step forward in making AI systems more accessible and human-like through natural handwriting recognition.

###📫 Contact
- 📧 Email: [ovaiz2004@gmail.com]
- 🌐 GitHub: https://github.com/ovaizbaig7
