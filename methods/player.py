import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_player_stats(player_id):
  response = requests.get(f'https://api.brawlhalla.com/player/{player_id}/stats?api_key={os.getenv("API_KEY")}')
  return response.text