from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

from game import Game

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

game = Game()

@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'test route'}), 200)

@app.route('/setup', methods=['GET'])
def get_board():
    return jsonify(game.show_board())

@app.route('/restart', methods=['GET'])
def restart_game():
    game.restart_game()
    return jsonify(success=True)

@app.route('/possible_moves', methods=['GET'])
def show_possible_moves():
  return game.possible_moves

@app.route('/make_move', methods=['POST'])
def make_move():
  field = request.json.get('field')
  is_ok = game.player_move(field)
  return jsonify(success=is_ok)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')