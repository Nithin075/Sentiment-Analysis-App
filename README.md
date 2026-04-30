# 🤖 AI Sentiment Analysis Web App

A clean, responsive web application built with **Python (Flask)** that performs real-time sentiment analysis on user-entered text. The app uses the **TextBlob** library to determine the emotional tone, polarity, and subjectivity of the input.

## 🚀 Features
- **Real-time Analysis:** Get instant feedback on the sentiment of your text.
- **Visual Indicators:** Results are color-coded (Green for Positive, Red for Negative, Gray for Neutral).
- **Sentiment Metrics:** 
  - **Polarity:** Measures how positive or negative the text is (Range: -1.0 to 1.0).
  - **Subjectivity:** Measures how factual or opinionated the text is (Range: 0.0 to 1.0).
- **Emoji Support:** Displays emojis based on the detected mood (😊, 😐, 😠).

## 🛠️ Tech Stack
- **Backend:** Python, Flask
- **AI/NLP:** TextBlob (NLTK-based)
- **Frontend:** HTML5, CSS3 (Responsive Design)

## 📥 Local Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Nithin075/Sentiment-Analysis-App.git](https://github.com/Nithin075/Sentiment-Analysis-App.git)
   cd Sentiment-Analysis-App
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download NLTK Corpora:**
   ```bash
   python -m textblob.download_corpora
   ```

5. **Run the application:**
   
```bash
   python app.py
   ```
   Open `http://127.0.0.1:5000` in your browser.

## ☁️ Deployment
This app is ready for deployment on **Render** or **Heroku**. 
- Ensure `requirements.txt` and `Procfile` are present in the root directory.
- Use the following start command: `gunicorn app:app`

---
Built with ❤️ by [Your Name/Nithin]


Now, when you visit your GitHub link, you'll see a beautifully formatted description instead of just a list of files!

**Are we ready to flip the switch on Render and go live?**
