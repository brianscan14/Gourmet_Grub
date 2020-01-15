import os
import re
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env
    
app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'good_grubDB'
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_recipies')
def get_recipies():
    return render_template("recipies.html", recipies=mongo.db.recipies.find())


@app.route('/search_recipe')
def search_recipe():
    rec_search_query = request.args['query']
    query = {'$regex': re.compile('.*{}.*'.format(rec_search_query), re.IGNORECASE)}
    results = mongo.db.recipies.find({'recipe_name': query})
    return render_template('search_recipe.html', query=rec_search_query, results=results)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)