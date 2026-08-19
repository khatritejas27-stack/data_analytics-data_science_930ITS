## task 5:Open ChatGPT or Copilot and ask it to explain the difference between a table, a row, and a column in SQL using an example from a food delivery app like Zomato. Paste the explanation you receive into your assignment.

# Difference Between a Table, Row, and Column in SQL

Imagine you're building the database for a food delivery app like **Zomato**. SQL stores data in **tables**, which are made up of **rows** and **columns**.

## Example: `Restaurants` Table

| restaurant_id | restaurant_name | city      | cuisine | rating |
|----------------|-----------------|-----------|----------|--------|
| 101            | Pizza Palace    | Mumbai    | Italian  | 4.5    |
| 102            | Spice Hub       | Delhi     | Indian   | 4.3    |
| 103            | Sushi World     | Bengaluru | Japanese | 4.8    |

## 1. Table

A **table** is a collection of related data organized into rows and columns.

**Example:**
- The entire `Restaurants` table stores information about restaurants available on the food delivery app.

## 2. Row

A **row** represents one complete record in a table.

For example, this row:

| restaurant_id | restaurant_name | city | cuisine | rating |
|----------------|-----------------|------|----------|--------|
| 102            | Spice Hub       | Delhi | Indian | 4.3 |

This row contains all the information about the restaurant **Spice Hub**.

## 3. Column

A **column** represents one specific attribute (or field) for every record in the table.

Examples:
- `restaurant_id` → Unique identifier for each restaurant
- `restaurant_name` → Name of the restaurant
- `city` → City where the restaurant is located
- `cuisine` → Type of food served
- `rating` → Customer rating

Each row has one value for every column.

## Real-World Analogy

Think of the table like an Excel spreadsheet:

- **Table** → The entire spreadsheet of restaurants
- **Row** → One restaurant's information
- **Column** → One category of information (Name, City, Rating, etc.)

## Summary

| SQL Term | Meaning | Zomato Example |
|----------|---------|----------------|
| **Table** | A collection of related records | `Restaurants` table |
| **Row** | One complete record | Details of **Spice Hub** |
| **Column** | One attribute of every record | `restaurant_name`, `city`, `rating` |

## Key Takeaway

- **Table** = All restaurant data
- **Row** = One restaurant's record
- **Column** = One attribute of each restaurant

