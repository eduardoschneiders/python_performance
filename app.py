from flask import Flask, jsonify
import logging

app = Flask(__name__)

logging.getLogger('werkzeug').disabled = True


@app.route('/')
def root():
  return jsonify({'message': 'root'})

@app.route('/test')
def test():
  return jsonify({'message': 'testing'})