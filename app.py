from flask import Flask, request
from flask_cors import CORS
from methods.player import get_legends, get_player_ranked

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

@app.route('/api', methods=['GET', 'POST'])
def brawlhalla_api():
  if request.method == 'GET':
    return get_legends()

  if request.method == 'POST':
    player_id = request.get_json()
    return get_player_ranked(player_id)
