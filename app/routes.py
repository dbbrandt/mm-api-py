from app import app
from flask import request
from mlmmapi import check_answer
from flask import jsonify

@app.route('/')
@app.route('/index')
def index():
    answer = request.args.get('answer')
    correct_answer = request.args.get('correct')
    correct, prediction, score = check_answer(answer, correct_answer)
    result = jsonify( { 'correct': correct,
               'prediction': prediction,
               'score': score
    })
    return result