## task 5:Explain the difference between WHERE and HAVING by giving one example query for each, using the Orders table. Your examples should show a scenario where WHERE and HAVING filter different things.



## 1.where : filter indivsual order
```sql
SELECT * FROM Orders WHERE OrderAmount > 1000;
```
**This returns only orders where the OrderAmount is greater than 1000.**


## 2.having: filter group of row after group by aggregation
```sql
SELECT CustomerID, SUM(OrderAmount) AS TotalAmount FROM Orders GROUP BY CustomerID HAVING SUM(OrderAmount) > 5000;
```
**This returns only customers whose total order amount is greater than 5000.**

## Key Difference:
**WHERE** filters rows before grouping , while **HAVING** filters groups after grouping.



