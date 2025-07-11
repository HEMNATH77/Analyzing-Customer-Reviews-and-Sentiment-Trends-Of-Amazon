--- 1. Create a new database for storing Amazon product reviews
create database Amazon_reviews;

--- 2. Switch to the newly created database
use Amazon_reviews;

--- 3. Create a table to store reviews and sentiment analysis results
create table amazon(name varchar(75),brand char(75),primaryCategories char(50),reviews_text text,review_date date,sentiment char(10));

---  4. View all records in the 'reviews' table
SELECT * FROM reviews;

---  5. Get the count of reviews for each sentiment category (Positive/Negative/Neutral)
select sentiment ,count(*)as count 
 from reviews 
 group by sentiment;

--- 6. Count how many times each unique review text appears (to identify duplicates or frequent feedback)

select reviews_text,count(*)as count  
from reviews 
group by reviews_text;

--- 7. Count the total number of reviews in the table
select  count(*) as total_reviews 
from reviews ;

--- 8. Show top 10 product names with the highest number of reviews

select name,count(*) as total_reviews
 from reviews
 group by name order by total_reviews desc limit 10;

