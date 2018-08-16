from flask import Flask, jsonify
import logging
import os

app = Flask(__name__)

try:
  environment = os.environ['FLASK_ENV']
except KeyError:
  environment = 'development'

if environment == 'test':
  logging.getLogger('werkzeug').disabled = True

@app.route('/')
def root():
  return jsonify({'message': 'root'})

@app.route('/test')
def test():
  return jsonify({'message': 'testing'})