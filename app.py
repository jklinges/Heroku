from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from os import environ

app = Flask(__name__)

app.config['MONGO_URI'] = environ.get(
    'MONGODB_URI', 'mongodb://localhost:27017/heroku')   
    # this may need to be '/notepad'

mongo = PyMongo(app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get(
    'DATABASE_URL','sqlite:///heroku.sqlite')

db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/tasks-postgres')
def tasksPostGres():
    tasks = db.session.query(Task)
    data = []

    for task in tasks:
        item = {
            'id': task.id,
            'description': task.description
        }
        data.append(item)
    
    return jsonify(data)


@app.route('/api/tasks-mongo')
def tasksMongo():
    tasks = mongo.db.tasks.find({})
    data = []

    for task in tasks:
        item = {
            '_id': str(task['_id']),
            'description': task['description']
        }
        data.append(item)

    return jsonify(data)


if __name__ == '__main__':
     app.run(debug=True) 
© 2021 GitHub, Inc.