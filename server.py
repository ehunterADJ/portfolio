from flask import Flask, render_template, request, redirect
from datetime import datetime
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_file(data):
    with open("data.txt", "a+") as file:
        now = (datetime.now()).strftime("%d/%m/%Y %H:%M:%S")
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file.write(f"{now}, {email}, {subject}, {message}\n")

def write_csv(data):
    with open("data.csv", "a", newline="") as database:
        now = (datetime.now()).strftime("%d/%m/%Y %H:%M:%S")
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([now, email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_csv(data)
        return redirect("thankyou.html")
    else:
        return "Something went wrong..."
