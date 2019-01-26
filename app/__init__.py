from flask import Flask, render_template
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(db, app)


@app.route('/')
@app.route('/index')
def hello_world():
    return render_template("index.html", title="Home")


if __name__ == '__main__':
    app.run()
