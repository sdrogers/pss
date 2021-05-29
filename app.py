import json

from flask import Flask
from flask import render_template, make_response
from flask import request

app = Flask(__name__)

# Main landing page - asks for name of user
@app.route('/')
def index():
    return render_template('index.html')

# Called from index with players name
# adds name to cookie
# returns main.html, passing name
@app.route('/addname', methods=['POST', 'GET'])
def addname():
    if request.method == 'POST':
        name = request.form['name']
        resp = make_response(render_template('main.html', name=name))
        resp.set_cookie('name', json.dumps(name))
    else:
        resp = render_template('index.html')
    return resp



@app.route('/hello/<name>')
def goodbye_world(name):
    return "goodbye " + name