from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_data = Post().getPosts(blog_url=blog_url)


@app.route('/')
def home():
    return render_template("index.html",
                           blogs=blog_data)


@app.route("/post/<id>")
def post(id):
    id = int(id) - 1
    return render_template("post.html",
                           id=id,
                           posts=blog_data)


if __name__ == "__main__":
    app.run(debug=True)
