from flask import Flask, redirect, url_for, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/feedback-form")
db = mongodb_client.db


@app.route('/feedback-form', methods=['POST', 'GET'])
def send_feedback():
    if request.method == 'POST':
        title = request.form["title"]
        summary = request.form["summary"]
        if title and summary:
            db.feedbacks.insert_one({'title': title, 'summary': summary})
            return redirect(url_for("thank_you"))
        else:
            return redirect(url_for("send_feedback"))
    else:
        return render_template('feedback.html')


@app.route('/thank-you')
def thank_you():
    return 'Thank You!'


if __name__ == '__main__':
    app.run()
