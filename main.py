
import pandas as pd
import seaborn as sns
from textblob import TextBlob
from textblob.en import polarity
from  sqlalchemy import create_engine

import matplotlib.pyplot as plt

df = pd.read_csv("./Amazon.csv")
#print(df.head(5))

df1 = df[['name','brand','primaryCategories','reviews.date','reviews.text']]
#print(df1)

df1 = df1.drop_duplicates()
df1 = df1.dropna(subset=["reviews.text"])

df1.loc[:,'reviews_text'] = df1["reviews.text"].str.replace(r'[^A-Za-z0-9]','',regex = True)
df1.loc[:,"review_date"] = pd.to_datetime(df1['reviews.date'],format = 'mixed',errors = 'coerce').dt.date

#print(df1)

def sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'Neutral'
df1['sentiment'] = df1['reviews_text'].apply(sentiment)

#print(df1[['name',"reviews_text","sentiment"]].head(40))

df1.drop(['reviews.text','reviews.date'],axis = 1,inplace = True)

#df1.to_csv("Sentiment_analysis.csv",index=False)




engine = create_engine('mysql+pymysql://root:root@localhost/Amazon_reviews')

#df1.to_sql('reviews',con = engine,if_exists = 'replace',index=False)


a = sns.countplot(data = df1,x = "sentiment")
for i in a.containers:
    a.bar_label(i)
plt.title("Sentiment Distribution")
plt.show()
