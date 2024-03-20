import os
import requests
from dotenv import load_dotenv

load_dotenv()

class BrawlhallaAPI:
  def __init__(self, endpoint, player_id = None):
    self.endpoint = endpoint
    self.player_id = player_id

  def direct_call(self):
    match self.endpoint:
      case 'legend':
        return self.__get_legends()
      case 'stats':
        return {'stats': self.__get_player_stats(), 'ranked': self.__get_player_ranked()}

  def __get_legends(self):
    response = requests.get(f'https://api.brawlhalla.com/legend/all?api_key={os.getenv("API_KEY")}')
    return response.text

  def __get_player_ranked(self):
    response = requests.get(f'https://api.brawlhalla.com/player/{self.player_id}/ranked?api_key={os.getenv("API_KEY")}')
    return response.text

  def __get_player_stats(self):
    response = requests.get(f'https://api.brawlhalla.com/player/{self.player_id}/stats?api_key={os.getenv("API_KEY")}')
    return response.text