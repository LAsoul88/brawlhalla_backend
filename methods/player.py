import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_legends():
  response = requests.get(f'https://api.brawlhalla.com/legend/all?api_key={os.getenv("API_KEY")}')
  return response.text

def get_player_ranked(player_id):
  response = requests.get(f'https://api.brawlhalla.com/player/{player_id}/ranked?api_key={os.getenv("API_KEY")}')
  return response.text