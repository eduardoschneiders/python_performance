from server import Server

class TestSuit():
  def __init__(self, ROOT_PATH, *methods):
    self.server = Server(ROOT_PATH)
    self.methods = methods

  def __enter__(self):
    self.server.start()

  def __exit__(self, type, value, traceback):
    self.server.stop()
    for method in self.methods:
      method()