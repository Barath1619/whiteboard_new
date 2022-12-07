from flask import Flask
application = Flask(__name__)


@application.route('/')
def hellow_world():
    return 'Hi Dhanush, priya'


if __name__ == '__main__':
    app.run('0.0.0.0')
