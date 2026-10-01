## task 4:Write a nested SQL query to find the names of all sellers from a 'Sellers' table on a Flipkart-style platform who have sold products in every category listed in a 'Categories' table.<br><br><em><strong>Hint:</strong> Use nested subqueries to compare seller's categories with the complete list of categories.</em>

SELECT seller_name FROM sellers WHERE catg_id = (SELECT count(catg_id) from categories)

SELECT seller_name FROM sellers WHERE catg_id = (SELECT cat_id from categories)




raj
raj@gamail.com
ajay
ajay@gamail.com
vijay
vijay@gmail.com