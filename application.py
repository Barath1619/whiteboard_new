import os

from flask import Flask, request, jsonify, render_template
from faker import Faker
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import SyncGrant

application = Flask(__name__)
fake = Faker()


@application.route('/')
def hellow_world():
    return render_template('index.html')


@application.route('/token')
def generate_token():
    # get credentials from environment variables
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    api_key = os.getenv('TWILIO_API_KEY')
    api_secret = os.getenv('TWILIO_API_SECRET')
    sync_service_sid = os.getenv('TWILIO_SYNC_SERVICE_SID')
    username = request.args.get('username', fake.user_name())
    # create access token with credentials
    token = AccessToken(account_sid, api_key, api_secret, identity=username)
    # create a Sync grant and add to token
    sync_grant = SyncGrant(sync_service_sid)
    token.add_grant(sync_grant)
    return jsonify(identity=username, token=token.to_jwt())


if __name__ == '__main__':
    application.run(host='0.0.0.0')
