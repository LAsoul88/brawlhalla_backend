from flask import Flask, request
from methods.player import get_player_stats

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def player_stats():
  if request.method == 'POST':
    return get_player_stats()
