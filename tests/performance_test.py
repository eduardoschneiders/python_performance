import time
import requests
import os
from server import Server

HOST = 'http://localhost:3000'
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


class CalculateTime():
  def __init__(self):
    self.results = []

  def register_time(self, function):
    def wrapper(*args):
      t = time.time()
      result = function(*args)
      total_time = round(time.time() - t, 3)
      self.results.append(total_time)
      return result

    return wrapper

  def get_results(self):
    return self.results

class RunningServer():
  def __init__(self):
    self.server = Server(ROOT_PATH)

  def __enter__(self):
    self.server.start()

  def __exit__(self, type, value, traceback):
    self.server.stop()

with RunningServer() as status:
  ct = CalculateTime()

  @ct.register_time
  def request(method, url):
    eval('requests.' + method)(url)

  request('get', HOST + '/')
  request('get', HOST + '/test')

  print(ct.get_results())

