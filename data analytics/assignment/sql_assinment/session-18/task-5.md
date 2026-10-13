## Tasks 5:List two optimizations you would apply to speed up a query that filters Flipkart products by category and price, and briefly explain how each helps.<br><br><em><strong>Hint:</strong> Think about indexes and query structure.</em>



1. Create a composite index on category and price: An index such as (category, price) helps the database quickly locate products in a specific category within a given price range, reducing the number of rows scanned.
example:
```sql
CREATE INDEX idx_category_price
ON products (category, price);
```


2. Optimize the WHERE clause: Use direct, selective conditions, such as WHERE category = 'Mobiles' AND price BETWEEN 10000 AND 20000, and avoid unnecessary functions or conversions on indexed columns. This allows the database to use indexes efficiently and filter products faster.

example:
```sql
SELECT product_name, price
FROM products
WHERE category = 'Mobiles'
  AND price BETWEEN 10000 AND 20000;
```