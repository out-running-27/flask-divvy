from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def hello_world():
    return render_template("index.html", title="Home")


if __name__ == '__main__':
    app.run()
