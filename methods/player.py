import os
import requests

from dotenv import load_dotenv

load_dotenv()

class Proxy:
  def __init__(self):
    self.endpoint = None
    self.player_id = None
    self.region = None
    self.bracket = None
    self.page = None

  def __setitem__(self, key, value):
    setattr(self, key, value)
  
  def __getitem__(self, key):
    return getattr(self, key)

  def unpack(self, data):
    for point in data.keys():
      self[point] = data.get(point)

  def __get_legends(self):
    response = requests.get(f'https://api.brawlhalla.com/legend/all?api_key={os.getenv("API_KEY")}').json()
    return response

  def __get_player_ranked(self):
    response = requests.get(f'https://api.brawlhalla.com/player/{self.player_id}/ranked?api_key={os.getenv("API_KEY")}').json()
    return response

  def __get_player_stats(self):
    response = requests.get(f'https://api.brawlhalla.com/player/{self.player_id}/stats?api_key={os.getenv("API_KEY")}').json()
    return response
  
  def __get_leaderboard(self):
    response = requests.get(f'https://api.brawlhalla.com/rankings/{self.bracket}/{self.region}/{self.page}?api_key={os.getenv("API_KEY")}').json()
    return response

  def direct_call(self):
    match self.endpoint:
      case 'legend':
        return self.__get_legends()
      case 'stats':
        stats = self.__get_player_stats()
        ranked = self.__get_player_ranked()
        player = {
          'name': stats['name'] or ranked['name'],
          'brawlhalla_id': self.player_id,
        }
        return {'player': player, 'stats': stats, 'ranked': ranked}
      case 'rankings':
        return self.__get_leaderboard()