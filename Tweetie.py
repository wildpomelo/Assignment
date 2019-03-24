#!flask/bin/python

import tweepy, json
import sys

from flask import Flask, render_template, request, redirect, Response
import random, json

app = Flask(__name__)

@app.route('/tweet')
def output():
	# serve index template
	return render_template('page.html', 
		t1=cont[0], 
		t2=cont[1], 
		t3=cont[2], 
		t4=cont[3], 
		t5=cont[4], 
		t6=cont[5], 
		t7=cont[6], 
		t8=cont[7], 
		t9=cont[8], 
		t10=cont[9],
		t11=cont[10],
		t12=cont[11],
		t13=cont[12],
		t14=cont[13],
		t15=cont[14],
		t16=cont[15],
		t17=cont[16],
		t18=cont[17],
		t19=cont[18],
		t20=cont[19],
		t21=cont[20],
		t22=cont[21],
		t23=cont[22],
		t24=cont[23],
		t25=cont[24],
		)

# Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

cont = []

for status in tweepy.Cursor(api.user_timeline, screen_name='@realDonaldTrump', tweet_mode="extended").items(25):
#    print(status.full_text)
    cont.append(status.full_text)

if __name__ == '__main__':
	# run!
	app.run()
