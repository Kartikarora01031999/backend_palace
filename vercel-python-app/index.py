from flask import Flask, jsonify, request
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv
from flask_cors import CORS
load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["POST","GET"])
def home():
    data=request.form
    message = Mail(
    from_email='ka340689@gmail.com',
    to_emails='acsgitikaarora@gmail.com',
    subject='Booking Enquiry by '+data["password"] +" Email: "+data["email"],
    html_content='<strong>'+data["startTime"]+"<br>"+data["endTime"]+"<br>"+data["date"]+"<br>"+data["message"]+"<strong>")

    sg = SendGridAPIClient("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")
    response = sg.send(message)
    return jsonify("Mail Sent Successfully")


@app.route('/about')
def about():
    return 'About Page Route'


@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'


@app.route('/contact')
def contact():
    return 'Contact Page Route'


@app.route('/api')
def api():
    with open('data.json', mode='r') as my_file:
        text = my_file.read()
        return text

if __name__ == "__main__":
        app.run(debug=True)