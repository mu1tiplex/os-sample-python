from flask import Flask
import time
from random import randint

application = Flask(__name__)

@application.route("/")
def hello():
# sleep for a few seconds, to allow livelyness probe to fail sometimes 
	sometime=randint(0,4) 
	time.sleep(sometime)
    return "Hello NIS (with sleep)!" 

if __name__ == "__main__":
    application.run()
