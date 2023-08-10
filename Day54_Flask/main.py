from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        new = function()
        new = f"<b>{new}</b>"
        return new
    return wrapper


@app.route('/')
@make_bold
def hello_world():
    return 'Hello, World!'


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f'''<h1 style="text-align: center">Hello {name}</h1> 
    <p>you are {number} years old</p>
    <img src="https://media.giphy.com/media/kiJEGxbplHfT5zkCDJ/giphy.gif">'''


if __name__ == "__main__":
    app.run(debug=True)
