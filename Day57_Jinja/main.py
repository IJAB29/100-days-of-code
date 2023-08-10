import requests
from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    random_num = random.randint(1, 10)
    curr_year = datetime.now().strftime("%Y")
    return render_template("index.html", num=random_num, year=curr_year)


@app.route("/guess/<name>")
def guess(name):
    age_url = f"https://api.agify.io?name={name}"
    age_data = requests.get(age_url).json()
    age = age_data["age"]

    gender_url = f"https://api.genderize.io?name={name}"
    gender_data = requests.get(gender_url).json()
    gender = gender_data["gender"]

    nationality_url = f"https://api.nationalize.io?name={name}"
    nationality_data = requests.get(nationality_url).json()
    nationality = nationality_data["country"][0]["country_id"]

    return render_template("guess.html",
                           name=name,
                           age=age,
                           gender=gender,
                           nationality=nationality)


@app.route("/blog/<num>")
def blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_data = requests.get(blog_url).json()
    return render_template("blog.html",
                           posts=blog_data,
                           )


if __name__ == "__main__":
    app.run(debug=True)


