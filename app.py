from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form.get("user_text", "")
        
        if text.strip():
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity
            
            # Logic for Label, Color, and Emoji
            if polarity > 0:
                label, color, emoji = "Positive", "#28a745", "😊"
            elif polarity < 0:
                label, color, emoji = "Negative", "#dc3545", "😠"
            else:
                label, color, emoji = "Neutral", "#6c757d", "😐"
            
            result = {
                "score": round(polarity, 2),
                "subj": round(subjectivity, 2),
                "label": label,
                "color": color,
                "emoji": emoji,
                "original": text
            }
            
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)