
import tweepy
import csv
import pandas as pd
####input your credentials here
consumer_key = "Sh4rtCV78EummAG1yWaQaXmyw"
consumer_secret = "h6BTyRKOKPol7ucXiZRNmiJuFTM4wvsu8adIU5rt5qVy6N6TfX"
access_token = "1046769984737665029-y7HJ9s9wBEyDkJKHc5ik3CCyX083Q3"
access_token_secret = "j51htadkbtPBkuiL46ZlWp1fB7tlXREia32UarRH5WKAv"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)
#####United Airlines
# Open/Create a file to append data
csvFile = open('fif.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["date", "twee"])

for tweet in tweepy.Cursor(api.search,q="#élection",count=1000,
                           lang="fr",
                           since="2017-04-03").items():
    print (tweet.created_at, tweet.text)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    
p=[]
d=pd.read_csv("fif.csv")    
for i in d.twee:
    p.append(i)

p=p[0:50]    
election=pd.DataFrame(pd.DataFrame({"Tweets":p}))
election.to_csv("election.csv",index=False)
data=pd.read_csv("fif.csv")