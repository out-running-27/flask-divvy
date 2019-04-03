from flask import render_template, jsonify
from app import app

from build_graph import create_edgelist, compute_pagerank, join_station_data


@app.route('/')
@app.route('/index')
def hello_world():
    return render_template("index.html", title="Home")


@app.route('/api/test', methods=['GET'])
def return_edgelist():
    edges = create_edgelist()
    graph = compute_pagerank(edges, damping_factor=0.85)
    df = join_station_data(graph)
    return jsonify(df.to_dict('records'))
