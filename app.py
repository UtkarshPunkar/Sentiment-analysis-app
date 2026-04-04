from flask import Flask, render_template, request
from model import predict_sentiment

app = Flask(__name__)

posts = [
    "I love this phone!",
    "Worst service ever",
    "This app is amazing",
    "Not worth the money",
    "Great experience overall"
]

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    user_input = ""

    if request.method == "POST":
        user_input = request.form["text"]
        result = predict_sentiment(user_input)

    # ONLY 2 VALUES → NO ERROR
    analyzed_posts = [(p, predict_sentiment(p)) for p in posts]

    return render_template(
        "index.html",
        result=result,
        posts=analyzed_posts,
        user_input=user_input
    )

if __name__ == "__main__":
    app.run(debug=True)
    #app.py file
