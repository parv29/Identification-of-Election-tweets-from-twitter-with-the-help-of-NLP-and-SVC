import pandas as pd
import numpy as np

election=pd.read_csv("yes.csv")
rando=pd.read_csv("no.csv")


k=election.append(rando)
k.to_csv("final.csv",index=False)



import random
fid = open("fully.csv", "r")
li = fid.readlines()
fid.close()
print(li)

random.shuffle(li)
print(li)

fid = open("shuffled.csv", "w")
fid.writelines(li)
fid.close()

data=pd.read_csv("shuffled.csv")