from flask import render_template
from app import app

from build_graph import create_edgelist


@app.route('/')
@app.route('/index')
def hello_world():
    return render_template("index.html", title="Home")


@app.route('/api/test', methods=['GET'])
def return_edgelist():
    return create_edgelist()

