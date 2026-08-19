## Tasks 4:Write an SQL query to display the first 10 restaurants from a 'restaurants' table, sorted alphabetically by name, just like Zomato's A-Z listing.<br><br><em><strong>Hint:</strong> Use ORDER BY with LIMIT.</em>
``` sql
select *from restaurants order by restaurant_name asc limit 0,10 ;
```