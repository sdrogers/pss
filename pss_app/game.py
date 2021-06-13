import json

from flask import Blueprint
from flask import render_template, make_response
from flask import request

from pss_app.pss_utils import check_winner, MOVE_DICT
from pss_app.pss_players import pick_move_random as pick_move


bp = Blueprint("game", __name__)

PLAY_TEMPLATE = 'play.html'

# Main landing page - asks for name of user
@bp.route('/')
def index():
    return render_template('index.html')


# Useful method to just reset all the stuff in the cookie
def reset_cookie(response):
    response.set_cookie('ai_total', '0', httponly=True, secure=True)
    response.set_cookie('user_total', '0', httponly=True, secure=True)
    response.set_cookie('history', json.dumps([]), httponly=True, secure=True)
    return response


# turn a history of ints into strings to make it nicer
# for visualisation
def make_pretty_history(history):
    pretty_history = []
    for h in history:
        pretty_history.append([MOVE_DICT[h[0]], MOVE_DICT[h[1]]])
    return pretty_history


# Called from index with players name
# adds name to cookie
# returns main.html, passing name
@bp.route('/addname', methods=['POST'])
def addname():
    name = request.form['name']
    response = make_response(render_template('main.html', name=name))
    response = reset_cookie(response)
    response.set_cookie('name', name, httponly=True, secure=True)
    return response


@bp.route('/play')
def play():
    name = request.cookies.get('name')
    user_total = int(json.loads(request.cookies.get('user_total')))
    ai_total = int(json.loads(request.cookies.get('ai_total')))
    return render_template(PLAY_TEMPLATE, name=name,
                           user_total=user_total,
                           ai_total=ai_total)


# Main logic, called when a user makes their move and a POST request
# is sent from play.
@bp.route('/submit_move', methods=['POST'])
def submit_move():

    # Get the current totals and history
    user_total = int(request.cookies.get('user_total', '0'))
    ai_total = int(request.cookies.get('ai_total', '0'))

    history = json.loads(request.cookies.get('history', '[]'))

    # Get the user's move
    user_move = int(request.form['move'])

    # Get the AI move
    ai_move = pick_move(history=history)

    # Check the winner
    ww = check_winner(ai_move, user_move)
    if ww == 1:
        result = 'AI won!'
        ai_total += 1
    elif ww == -1:
        result = 'You won!'
        user_total += 1
    else:
        result = 'Draw'

    # Add the round to the history
    history.append([ai_move, user_move])

    # Make the history nice for displaying
    # (replaces the numbers with strings)
    pretty_history = make_pretty_history(history)

    # Make the response
    response = make_response(render_template('result.html',
                                                result=result,
                                                user=user_total,
                                                ai=ai_total,
                                                history=pretty_history))

    # Update the cookies
    response.set_cookie('user_total', str(user_total), httponly=True, secure=True)
    response.set_cookie('ai_total', str(ai_total), httponly=True, secure=True)
    response.set_cookie('history', json.dumps(history), httponly=True, secure=True)
    return response


@bp.route('/reset_scores')
def reset_scores():
    name = request.cookies.get('name')
    response = make_response(render_template(PLAY_TEMPLATE, name=name))
    response = reset_cookie(response)
    return response
