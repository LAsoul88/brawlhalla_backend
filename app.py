from flask import Flask, request, jsonify
from methods.player import get_player_stats

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def player_stats():
  if request.method == 'POST':
    data = request.get_json()
    return get_player_stats(data)
