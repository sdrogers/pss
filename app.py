import json

from flask import Flask
from flask import render_template, make_response
from flask import request

from pss_code.pss_utils import VALID_MOVES
from pss_code.pss_utils import pick_move, check_winner, MOVE_DICT

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
        resp.set_cookie('ai_total', json.dumps(0))
        resp.set_cookie('user_total', json.dumps(0))
        resp.set_cookie('history', json.dumps([]))
        
    else:
        resp = render_template('index.html')
    return resp

@app.route('/play')
def play():
    name = json.loads(request.cookies.get('name'))
    return render_template('play.html', name=name, vm = VALID_MOVES)

@app.route('/submit_move', methods=['POST', 'GET'])
def submit_move():
    user_total = request.cookies.get('user_total')
    if user_total is None:
        user_total = 0
    else:
        user_total = json.loads(user_total)
    
    ai_total = request.cookies.get('ai_total')
    if ai_total is None:
        ai_total = 0
    else:
        ai_total = json.loads(ai_total)
    
    history = json.loads(request.cookies.get('history'))

    print("USER: {}, AI: {}".format(user_total, ai_total))
    
    if request.method == 'POST':
        user_move = int(request.form['move'])
        ai_move = pick_move()
        ww = check_winner(ai_move, user_move)
        if ww == 1:
            result = 'AI won!'
            ai_total += 1
        elif ww == -1:
            result = 'You won!'
            user_total += 1
        else:
            result = 'Draw'

        print("USER: {}, AI: {}".format(user_total, ai_total))

        history.append((ai_move, user_move))

        nice_history = []
        for h in history:
            nice_history.append([MOVE_DICT[h[0]], MOVE_DICT[h[1]]])

        response = make_response(render_template('result.html', 
                                                  result=result, 
                                                  user=user_total, 
                                                  ai=ai_total,
                                                  history=nice_history))

        response.set_cookie('user_total', json.dumps(user_total))
        response.set_cookie('ai_total', json.dumps(ai_total))
        response.set_cookie('history', json.dumps(history))
    else:
        response = render_template('play.html')
    return response

@app.route('/reset_scores')
def reset_scores():
    name = request.cookies.get('name')
    response = make_response(render_template('play.html', name=name))
    response.set_cookie('ai_total', json.dumps(0))
    response.set_cookie('user_total', json.dumps(0))
    response.set_cookie('history', json.dumps([]))
    return response