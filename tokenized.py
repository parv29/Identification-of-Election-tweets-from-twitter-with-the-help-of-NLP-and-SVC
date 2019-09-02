import pandas as pd
from nltk.stem.snowball import SnowballStemmer

# The Snowball Stemmer requires that you pass a language parameter
s_stemmer = SnowballStemmer(language='english')
import spacy
nlp = spacy.load('en_core_web_sm')
len(nlp.Defaults.stop_words)
nlp.Defaults.stop_words.add('#')

nlp.vocab["#"].is_stop = True
nlp.Defaults.stop_words.add("b'RT")
          
nlp.vocab["b'RT"].is_stop = True

nlp.Defaults.stop_words.add('b"RT')
          
nlp.vocab['b"RT'].is_stop = True

nlp.Defaults.stop_words.add("*")
          
nlp.vocab["*"].is_stop = True

nlp.Defaults.stop_words.add("or")
          
nlp.vocab["or"].is_stop = True
nlp.Defaults.stop_words.add("i")
          
nlp.vocab["i"].is_stop = True          

nlp.Defaults.stop_words.add("?")
          
nlp.vocab["?"].is_stop = True          
          
k=[]

#run this code twice first with the name you want than change then name is the open and run again
for i in nlp.Defaults.stop_words:
    k.append(i)
import csv
data=pd.read_csv("runn.csv")

#HERE
csvFile = open('tkraan.csv', 'a')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["A"])

t=[]

for i in data.tweets:
    
    
    s=nlp(i)
    for j in s:
        

        if j.text  not in k:
            t.append(j)
    
    csvWriter.writerow([t])
    t=[]
# after running the upper code  write the first name u entered in the open in fi and get results
e=[]    
fi=pd.read_csv("tweetsafterrr.csv")
fi.rename(columns={"tweets after tokenization":"A"})  
for i in fi.A:
    print(i)
    for word in i:
        print(word)
        e.append(s_stemmer.stem(word))



tweet=pd.read_csv("tkelec.csv")
import re


tweet = re.sub(r':', '', tweet)
tweet = re.sub(r'‚Ä¶', '', tweet)
#replace consecutive non-ASCII characters with a space
tweet = re.sub(r'[^\x00-\x7F]+',' ', tweet)
#remove emojis from tweet
tweet = emoji_pattern.sub(r'', tweet)


