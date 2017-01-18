import urllib.request
def parseData(fname):
  for l in urllib.request.urlopen(fname):
    yield eval(l)

data = list(parseData("http://jmcauley.ucsd.edu/cse190/data/beer/beer_50000.json"))

# remove review text
def delete_review_text(dict):
	dict.pop("review/text",None)
	dict.pop("review/timeStruct",None)
	return dict

data2=[delete_review_text(d) for d in data]

import pandas as pd
df=pd.DataFrame(data2)

df.to_csv('beer_review.csv', header=True)

