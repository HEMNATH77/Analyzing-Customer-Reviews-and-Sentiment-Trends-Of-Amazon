# 📊 Amazon E-Commerce Product Review Sentiment Analysis 

This project performs **Sentiment Analysis** on Amazon product reviews using Python libraries like **TextBlob**, **Pandas**, **Seaborn**, and **SQLAlchemy**, and stores the results in a **MySQL** database. The sentiment distribution is then visualized using **Seaborn and Matplotlib**.

---

## 📁 Dataset

The dataset used is a CSV file named `Amazon.csv`, containing customer reviews of various products from Amazon. The important columns extracted are:

- `name`: Product name  
- `brand`: Product brand  
- `primaryCategories`: Category of the product  
- `reviews.date`: Review date  
- `reviews.text`: Text content of the review  

---

## 🎯 Project Objectives

- Clean and preprocess product reviews.
- Perform sentiment classification using TextBlob.
- Store cleaned and processed data in a MySQL database.
- Visualize sentiment distribution.

---

## 🛠 Tech Stack

- **Programming Language**: Python
- **Libraries**:
  - `pandas` – for data manipulation  
  - `textblob` – for sentiment analysis  
  - `seaborn`, `matplotlib` – for data visualization  
  - `sqlalchemy`, `pymysql` – for MySQL integration  
- **Database**: MySQL

---

## 🔍 Step-by-Step Breakdown

### 1. Import Libraries

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from textblob import TextBlob
from textblob.en import polarity
from sqlalchemy import create_engine
```
### 2. Load and Filter Dataset
```python
df = pd.read_csv("./Amazon.csv")
df1 = df[['name', 'brand', 'primaryCategories', 'reviews.date', 'reviews.text']]
df1 = df1.drop_duplicates()
df1 = df1.dropna(subset=["reviews.text"])
```

### 3. Text Cleaning and Date Formatting

```python
df1.loc[:,'reviews_text'] = df1["reviews.text"].str.replace(r'[^A-Za-z0-9]', '', regex=True)
df1.loc[:,"review_date"] = pd.to_datetime(df1['reviews.date'], format='mixed', errors='coerce').dt.date
```
### 4. Define Sentiment Function
```python
def sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'Neutral'

df1['sentiment'] = df1['reviews_text'].apply(sentiment)
```
### 5. Drop Unused Columns
```python
df1.drop(['reviews.text', 'reviews.date'], axis=1, inplace=True)
```
### 6. MySQL Integration
```python
engine = create_engine('mysql+pymysql://root:root@localhost/Amazon_reviews')
# df1.to_sql('reviews', con=engine, if_exists='replace', index=False)
```

### 7. Visualization
```python
a = sns.countplot(data=df1, x="sentiment")
for i in ax.containers:
     a.bar_label(i)
plt.title("Sentiment Distribution")
plt.show()
```

### 8. Output Visualization 
<img width="640" height="480" alt="fig" src="https://github.com/user-attachments/assets/0d8ed4a9-8f31-4acd-8cad-06f7424d9c86" />


## 🚀 How to Run

### 1. Install Dependencies
````python
pip install pandas seaborn matplotlib textblob sqlalchemy pymysql
````
### 2.Add Dataset
Place your Amazon.csv file inside the project directory.

### ✅ Prerequisites
Python 3.7+

MySQL running locally with a database named Amazon_reviews

Dataset named Amazon.csv in the same directory

### ✅ Conclusion
This project demonstrates how sentiment analysis can be effectively used to extract insights from e-commerce product reviews. By combining natural language processing with data visualization and SQL-based storage:

We've cleaned and transformed raw review data.

Applied TextBlob polarity scoring to classify reviews as positive, negative, or neutral.

Stored the processed data into a MySQL database for further analysis or integration.

Visualized the overall sentiment distribution to identify customer satisfaction trends.

This pipeline can be extended to larger datasets or integrated into dashboards to help businesses make data-driven decisions based on customer feedback.
