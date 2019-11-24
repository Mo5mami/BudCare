import csv
import tweepy
import sys
#Twitter API credentials
consumer_key = 'TMuoiU12dsowYSWfm0zF248at'
consumer_secret = 'T30pj99njZ9tTEIRPrscvuS2HfSqyLGFwdeABhrCrx6GFmOtmt'
access_key = '1147519079764451334-QUk66hNc5LMbMjbshXmyDrRUWqu3uf'
access_secret = 'TaIj4nHRdjG5x2dFkjKmDyCisLMc4049zbCXIgq7QklGM'


def get_all_tweets(screen_name):
	
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200,tweet_mode='extended')
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.full_text] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass

def to_ahmed_csv():
	import pandas as pd
	import string 
	ahmed = pd.read_csv('AhmedAt17151873_tweets.csv',encoding = "cp1252")
	h = ahmed['text']     
	translation = str.maketrans("","", string.punctuation)
	#text is array of sentences 
	for i,s in enumerate(h):
    		h[i]=h[i].translate(translation);
    		h[i]=h[i].lower()
	ahmed['text']=h
	ahmed.drop('id',axis=1, inplace=True)
	ahmed.to_csv('tweets.csv',index=False)
if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets(sys.argv[1])
	to_ahmed_csv()
	