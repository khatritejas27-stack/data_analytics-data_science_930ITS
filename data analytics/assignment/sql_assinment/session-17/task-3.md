## Tasks 3:Add a new table called Review with columns: id, restaurant_id, user_name, rating, and review_date. Insert at least 10 sample reviews, linking them to restaurants using restaurant_id.


```sql
create table review(
id int primary key AUTO_INCREMENT,
restaurant_id int,
user_name varchar(255), 
rating decimal(2,1), 
review_date DATE,
FOREIGN key(restaurant_id) REFERENCES restaurant(id)
);
INSERT INTO Review  VALUES
(1, 1, 'Rahul Sharma', 5.0, '2026-09-15'),
(2, 1, 'Ananya Iyer', 4.5, '2026-10-01'),
(3, 4, 'David Miller', 5.0, '2026-08-20'),
(4, 5, 'Priya Nair', 4.0, '2026-09-28'),
(5, 6, 'Vikram Malhotra', 4.5, '2026-10-05'),
(6, 6, 'Sneha Patel', 5.0, '2026-07-12'),
(7, 7, 'Rohan Das', 4.0, '2026-09-10'),
(8, 9, 'Meera Krishnan', 5.0, '2026-10-09'),
(9, 13, 'John Doe', 4.5, '2026-08-14'),
(10, 14, 'Karthik Rao', 4.5, '2026-09-30');
```