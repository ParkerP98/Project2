from flask import Flask, render_template, jsonify, redirect, request
from flask_pymongo import PyMongo

app = Flask(__name__)

# Establish mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/NBAStats")


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/playerPage')
def playerPage():
    args = request.args
    if "name" in args:
        name=args["name"]
    data = mongo.db.Individuals.find_one({'Name':name})
    print(data)
    return render_template('playa.html', d = data)


if __name__ == "__main__":
    app.run(debug=True)