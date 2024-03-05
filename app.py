from flask import Flask, request
from flask_cors import CORS
from methods.player import get_player_stats

app = Flask(__name__)
CORS(app)

@app.route('/api', methods=['POST'])
def player_stats():
  if request.method == 'POST':
    player_id = request.get_json()
    return get_player_stats(player_id)
