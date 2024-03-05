from flask import Flask, request

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def player_stats():
  if request.method == 'POST':
    return
