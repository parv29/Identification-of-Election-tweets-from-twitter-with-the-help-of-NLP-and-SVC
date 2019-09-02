
import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = "               "
consumer_secret = "                    "
access_token = "        "
access_token_secret = "                      "

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('fif.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["date", "twee"])
# Wrtie the topic you want to search in q and the set the count 
for tweet in tweepy.Cursor(api.search,q="#élection",count=1000,
                           lang="en",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])

    
election=pd.DataFrame(pd.DataFrame({"Tweets":p}))
election.to_csv("election.csv",index=False)
data=pd.read_csv("fif.csv")
