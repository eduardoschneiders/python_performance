import time
import requests
import os
from server import Server
from calculate_time import CalculateTime

HOST = 'http://localhost:3000'
ROOT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

class RunningServer():
  def __init__(self):
    self.server = Server(ROOT_PATH)

  def __enter__(self):
    self.server.start()

  def __exit__(self, type, value, traceback):
    self.server.stop()

with RunningServer():
  ct = CalculateTime()

  @ct.register_time
  def request(method, url):
    eval('requests.' + method)(url)

  request('get', HOST + '/')
  request('get', HOST + '/test')

  ct.print_results()

