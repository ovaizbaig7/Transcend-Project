#🚀 Transcend – AI-Powered Handwriting Recognition Chat Assistant
Smart Assistant: Handwritten Digit Recognition Powered by AI
🧠 Project Overview

Transcend is an intelligent web-based assistant capable of understanding handwritten text from images and responding intelligently using AI-powered conversational models.

It bridges the gap between visual handwritten input and natural language understanding, allowing users to interact with AI by simply uploading handwritten notes or typing directly in a chat interface.

Core Problem Solved:
Traditional OCR systems struggle to accurately read handwritten content. Transcend leverages deep learning-based OCR (TrOCR) to extract handwriting with improved accuracy and then uses an AI chatbot (powered by OpenAI GPT models) to interpret and respond contextually.

🛠️ Tech Stack
Layer	Technologies Used
Frontend	HTML, CSS, JavaScript
Backend	Python, Flask
AI / ML Models	Microsoft TrOCR (via Hugging Face Transformers), OpenAI GPT
Database	SQLite (for authentication and user data)
Libraries & Tools	Flask-SQLAlchemy, Transformers, Torch, PIL, Werkzeug
Environment	Local Flask Server
🌟 Features
🏠 Homepage

Introductory page explaining the purpose of Transcend.

Navigation options for Login, Signup, and Chat Interface.

🔐 Authentication

Secure signup and login system using password hashing.

Session-based authentication for user management.

💬 Chat Interface

Real-time AI-powered chat resembling ChatGPT.

Users can:

Type questions directly.

Upload handwritten images.

Use their camera for live capture.

View OCR results and edit before sending to the chatbot.

✍️ OCR (Optical Character Recognition)

Integrated Microsoft TrOCR model for handwriting extraction.

Handles both printed and cursive handwriting.

Editable OCR result panel with:

Grammar correction

Summarization

Re-send to chatbot options

📸 Image Upload & Preview

Upload or capture handwritten text via webcam.

Automatic image processing and text extraction.

🧩 User Dashboard

Displays chat history and extracted text summaries (optional future scope).
