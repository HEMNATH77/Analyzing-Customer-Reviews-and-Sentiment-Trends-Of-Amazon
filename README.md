
## 📊 **Amazon E-Commerce Product Review Sentiment Analysis**

This section gives a **brief overview of the project**, stating what the project is about. It introduces the reader to the **core objective** — using sentiment analysis on product reviews from Amazon to classify them into **positive, negative, or neutral** using Python and storing the results in MySQL. Visualizations are used to make the insights more comprehensible.

---

## 📁 **Dataset**

This section outlines the **data source and the relevant features** extracted from it. It specifies that the dataset is a CSV file containing Amazon product reviews and lists the most significant columns:

* **name** – the product's name
* **brand** – the product’s brand
* **primaryCategories** – the category the product belongs to
* **reviews.date** – the date when the review was posted
* **reviews.text** – the textual content of the customer review

---

## 🎯 **Project Objectives**

Here, the **goals** of the project are broken down:

* Clean and prepare the raw review data.
* Use **TextBlob** to analyze the sentiment in the review text.
* Store the resulting data (including sentiment labels) in a **MySQL database**.
* Visualize the distribution of sentiments (positive/neutral/negative) using **Seaborn and Matplotlib**.

---

## 🛠 **Tech Stack**

This part lists the **technologies and libraries** used:

* **Python** – Programming language.
* **pandas** – To handle data cleaning and manipulation.
* **TextBlob** – For natural language processing and sentiment analysis.
* **Seaborn & Matplotlib** – For data visualization.
* **SQLAlchemy & PyMySQL** – For connecting and inserting data into the MySQL database.
* **MySQL** – Database to store the cleaned and processed review data.

---

## 🔍 **Step-by-Step Breakdown**

Each of these steps walks through the **actual implementation**:

### 1. **Import Libraries**

Essential libraries are imported for data handling, sentiment analysis, and database connection.

### 2. **Load and Filter Dataset**

* The CSV file is read.
* Only the relevant columns are retained.
* Duplicate rows are dropped.
* Null review texts are removed to avoid analysis errors.

### 3. **Text Cleaning and Date Formatting**

* **Non-alphanumeric characters** are removed from the reviews.
* Dates are parsed into a proper datetime format for consistency and future analysis.

### 4. **Define Sentiment Function**

* A custom function uses **TextBlob's polarity score**:

  * > 0: Positive sentiment
  * < 0: Negative sentiment
  * \== 0: Neutral sentiment
* This function is applied to the review texts to assign sentiment labels.

### 5. **Drop Unused Columns**

After extracting the useful data and generating the sentiment, the original columns (`reviews.text` and `reviews.date`) are removed for clarity and to reduce redundancy.

### 6. **MySQL Integration**

* A SQLAlchemy engine is created to connect to a local MySQL database.
* The `to_sql()` function (commented out for now) can be used to **upload the cleaned DataFrame** into the database table named `reviews`.

### 7. **Visualization**

* A **count plot** is created using Seaborn to show the distribution of sentiment labels.
* Labels are added on top of each bar.
* A plot title is given for clarity.

### 8. **Output Visualization**

* A final plot appears showing the count of positive, negative, and neutral reviews.
* This helps quickly understand **customer sentiment trends**.
<img width="640" height="480" alt="fig" src="https://github.com/user-attachments/assets/0d8ed4a9-8f31-4acd-8cad-06f7424d9c86" />
---

## 🚀 **How to Run**

Instructions on **setting up and running** the project locally:

1. Install required Python libraries using pip.
2. Place the dataset (`Amazon.csv`) in the working directory.
3. Ensure that a local MySQL instance is running and a database named `Amazon_reviews` exists.

---

## ✅ **Prerequisites**

Specifies what is **required before running** the project:

* Python version 3.7 or above.
* MySQL installed and running.
* Dataset file available in the same directory as the script.

---

## ✅ **Conclusion**

Summarizes what was accomplished in the project:

* Raw reviews were cleaned and transformed.
* Sentiment analysis was performed using TextBlob.
* The results were stored in a structured format in MySQL.
* Sentiment distribution was visualized.
* Notes how this workflow can be **scaled** or integrated into **dashboards** to extract business insights from customer feedback.
