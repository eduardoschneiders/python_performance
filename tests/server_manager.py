from server import Server

class RunningServer():
  def __init__(self, ROOT_PATH):
    self.server = Server(ROOT_PATH)

  def __enter__(self):
    self.server.start()

  def __exit__(self, type, value, traceback):
    self.server.stop()