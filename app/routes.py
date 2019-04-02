from flask import render_template
from app import app

from build_graph import create_edgelist, compute_pagerank


@app.route('/')
@app.route('/index')
def hello_world():
    return render_template("index.html", title="Home")


@app.route('/api/test', methods=['GET'])
def return_edgelist():
    data = create_edgelist()
    pr = compute_pagerank(data, damping_factor=0.85)

    return

