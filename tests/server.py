import subprocess
import signal
import time
import os

class Server():
  def __init__(self, root_path):
    os.environ['FLASK_APP'] = root_path + '/app.py'
    os.environ['FLASK_ENV'] = 'test'

  def start(self):
    proc = subprocess.Popen(['flask', 'run', '-p', '3000'],
      stdout=subprocess.DEVNULL)

    response = 1
    while int(response) != 0:
      response = subprocess.call(['kill', '-0', str(proc.pid)],
        stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
      time.sleep(1)

    self.proc = proc

  def stop(self):
    os.kill(self.proc.pid, signal.SIGTERM)