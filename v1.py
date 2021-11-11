import os
from os.path import join,dirname
from dotenv import load_dotenv
from pushbullet import Pushbullet

dotenv_path = join(dirname(__file__),'.env')
load_dotenv(dotenv_path)

api_key = os.environ.get('API_KEY','default')

#Authentication
pb = Pushbullet(api_key)

#get all devices the current user has access to
print(pb.devices)
