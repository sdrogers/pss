import json

from flask import Flask
from flask import render_template, make_response
from flask import request

from pss_code.pss_utils import VALID_MOVES
from pss_code.pss_utils import pick_move, check_winner

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

@app.route('/play')
def play():
    name = json.loads(request.cookies.get('name'))
    return render_template('play.html', name=name, vm = VALID_MOVES)

@app.route('/submit_move', methods=['POST', 'GET'])
def submit_move():
    user_total = request.cookies.get('user')
    if user_total is None:
        user_total = 0
    else:
        user_total = json.loads(user_total)
    
    ai_total = request.cookies.get('AI')
    if ai_total is None:
        ai_total = 0
    else:
        ai_total = json.loads(ai_total)
    if request.method == 'POST':
        move = request.form['move']
        move = int(move)
        ai_move = pick_move()
        ww = check_winner(ai_move, move)
        ai_total += ww
        if ww == 1:
            result = 'AI won!'
        elif ww == -1:
            result = 'You won!'
        else:
            result = 'Draw'
        user_total += -ww
        response = make_response(render_template('result.html', result=result, user=user_total, ai=ai_total))
        response.set_cookie('user', json.dumps(user_total))
        response.set_cookie('AI', json.dumps(ai_total))
    else:
        response = render_template('play.html')
    return response
