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
# After running the above code you will get tokenized tweets
