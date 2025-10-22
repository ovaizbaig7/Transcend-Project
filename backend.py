from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from openai import OpenAI
from dotenv import load_dotenv
import os
from PIL import Image
import pytesseract
import cv2

# ------------------------
# 🔐 CONFIG
# ------------------------

# Load environment variables (optional)
load_dotenv()

# Set custom OpenAI base and key
API_KEY = "ddc-beta-yjd9ndlf3v-5MTMG8CgcpxlHfaqI65yY1osk2OY4hTH0l0"
BASE_URL = "https://api.sree.shop/v1"

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

# ------------------------
# ✅ FLASK SETUP
# ------------------------

app = Flask(__name__)
app.secret_key = "your_sec7efd8ff6047863c2b8d7e08ce618d32b8a180c7bd01f84de8e4675064e65beffret_key"

# SQLite DB
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# File Upload
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ------------------------
# ✅ DATABASE MODELS
# ------------------------

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

with app.app_context():
    db.create_all()

# ------------------------
# ✅ ROUTES
# ------------------------

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/index")
def index():
    if "user_id" in session:
        return render_template("index.html")
    return redirect(url_for("login"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["user_name"] = user.name
            return redirect(url_for("index"))

        flash("❌ Invalid credentials", "error")
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            flash("❌ Passwords do not match", "error")
            return redirect(url_for("signup"))

        if User.query.filter_by(email=email).first():
            flash("⚠️ Email already registered", "error")
            return redirect(url_for("signup"))

        hashed_pw = generate_password_hash(password)
        new_user = User(name=name, email=email, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        flash("✅ Signup successful! Please log in.", "success")
        return redirect(url_for("login"))

    return render_template("signup.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# ------------------------
# ✅ OCR UTILITY
# ------------------------

def process_ocr(image_path):
    try:
        image = Image.open(image_path)
        return pytesseract.image_to_string(image).strip()
    except Exception as e:
        return f"⚠️ OCR Error: {str(e)}"

# ------------------------
# ✅ CHATBOT LOGIC
# ------------------------

chat_history = []

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # --- Handle plain text messages ---
        if request.is_json:
            data = request.get_json()
            msg = data.get("msg")
            if msg:
                chat_history.append({"role": "user", "content": msg})

                response = client.chat.completions.create(
                    model="Provider-9/gpt-4.1",
                    messages=[
                        {"role": "system", "content": "You are Transcend, a helpful and friendly assistant."}
                    ] + chat_history
                )

                reply = response.choices[0].message.content.strip()
                chat_history.append({"role": "assistant", "content": reply})

                return jsonify({"response": reply})

        # --- Handle image upload ---
        if "image" in request.files:
            file = request.files["image"]
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], secure_filename(file.filename))
            file.save(filepath)

            extracted_text = process_ocr(filepath)

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are Transcend, a chatbot who understands OCR text from images."},
                    {"role": "user", "content": f"Read this image text and respond:\n{extracted_text}"}
                ]
            )

            reply = response.choices[0].message.content.strip()
            return jsonify({"response": reply, "extracted_text": extracted_text})

        return jsonify({"response": "⚠️ Invalid input. Send text or image."})

    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"response": f"⚠️ Internal Server Error: {str(e)}"}), 500

# ------------------------
# ✅ RUN
# ------------------------

if __name__ == "__main__":
    app.run(debug=False)
