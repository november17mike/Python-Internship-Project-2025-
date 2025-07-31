from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("Route / accessed")
    sentiment = None
    polarity = None
    subjectivity = None

    if request.method == 'POST':
        print("POST method detected")
        user_text = request.form['text']
        print(f"Received text: {user_text}")
        blob = TextBlob(user_text)
        polarity = round(blob.sentiment.polarity, 3)
        subjectivity = round(blob.sentiment.subjectivity, 3)

        if polarity > 0:
            sentiment = 'Positive'
        elif polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        print(f"Sentiment: {sentiment}, Polarity: {polarity}, Subjectivity: {subjectivity}")

    return render_template('home.html', sentiment=sentiment,
                           polarity=polarity,
                           subjectivity=subjectivity)

if __name__ == '__main__':
    app.run(debug=True, port=5050)
