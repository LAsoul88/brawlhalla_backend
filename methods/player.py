import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_player_stats():
  response = requests.get(f'https://api.brawlhalla.com/player/3/stats?api_key={os.getenv("API_KEY")}')
  return response.text