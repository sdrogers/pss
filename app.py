from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello0 world"
    
    
@app.route('/hello/<name>')
def goodbye_world(name):
    return "goodbye " + name