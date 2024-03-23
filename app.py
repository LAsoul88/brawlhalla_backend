from flask import Flask, request
from flask_cors import CORS
from methods.player import Proxy

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])

@app.route('/api', methods=['POST'])
def brawlhalla_api():

  if request.method == 'POST':
    data = request.get_json()
    comms = Proxy()
    comms.unpack(data)
    print(comms.endpoint)
    return comms.direct_call()
