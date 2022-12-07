import os

from flask import Flask, request, jsonify, render_template


application = Flask(__name__)


@application.route('/')
def hellow_world():
    return render_template('index.html')


if __name__ == '__main__':
    application.run('0.0.0.0')
