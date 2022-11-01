# Importing Modules/Libraries
import tweepy
import time
from datetime import datetime
import random
from auxiliar import *

# Credentials (Insert your keys and tokens below)
api_key = " "
api_secret = " "
bearer_token = " "
access_token = " "
access_token_secret = " "

# Connecting to Twitter API
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Getting the bot's unique ID
Minovsky = client.get_me().data.id

# Hinders the bot from replying to old tweets
start_id = 1
initialisation_resp = client.get_users_tweets(Minovsky)
if initialisation_resp.data != None:
    start_id = initialisation_resp.data[0].id

# Looking for mentions tweets in an endless loop
while True:
    
    #Check if weather/song was requested
    mentions = client.get_users_mentions(Minovsky, since_id=start_id)
    
    if mentions.data != None:
        for tweet in  mentions.data:
            try:
                twt = tweet.text.lower()
                if 'music' in twt or 'musica' in twt or 'música' in twt:
                    client.create_tweet(in_reply_to_tweet_id=tweet.id, text=music())
                    start_id = tweet.id
                elif 'tempo' in twt:
                    city = tweet.text.split()[-1]
                    client.create_tweet(in_reply_to_tweet_id=tweet.id, text=weather(city))
                    start_id = tweet.id
            except Exception as error:
                print(error)
  
    #Searches for my friends new tweets
    for i in range(len(friends)):
        
        response = client.get_users_tweets(amgs[i], exclude=['replies', 'retweets'], since_id=start_id)

        if response.data != None:
            for tweet in response.data:
                try:
                    if random.random() <= .70:
                        answer = bruh[random.randint(0, len(msg)-1)]
                        print('Tweet: ', tweet.text, '\nResp: ', answer, '\n')
                        client.create_tweet(in_reply_to_tweet_id=tweet.id, text=answer)
                        start_id = tweet.id
                except Exception as error:
                    print(error)
       
    # Delay (so the bot doesn't search for new tweets a bucn of time each second)
    time.sleep(30)
