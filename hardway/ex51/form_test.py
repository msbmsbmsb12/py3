from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello")
def index():
    # http://127.0.0.1:5000/hello?name=M
    name = request.args.get('name', 'Nobody')
    greet = request.args.get('great', 'Hello')
    if name:
        greeting = f"{greet}, {name}"
    else:
        greeting = "Hello World"

    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run()