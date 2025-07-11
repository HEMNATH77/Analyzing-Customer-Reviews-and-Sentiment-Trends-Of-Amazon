create database Amazon_reviews;


use Amazon_reviews;

create table amazon(name varchar(75),brand char(75),primaryCategories char(50),reviews_text text,review_date date,sentiment char(10))

SELECT * FROM reviews;

select sentiment ,count(*)as count 
 from reviews 
 group by sentiment;

select reviews_text,count(*)as count  
from reviews 
group by reviews_text;

select  count(*) as total_reviews 
from reviews ;


select name,count(*) as total_reviews
 from reviews
 group by name order by total_reviews desc limit 10;
