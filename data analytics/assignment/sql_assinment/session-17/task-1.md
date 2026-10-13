## Tasks 1:Create a SQL table called Restaurant with columns: id, name, cuisine, location, and average_rating. Insert at least 5 sample rows representing popular restaurants from Zomato.

```sql
create table restaurant(
  id int primary key auto_increment ,
  name varchar(255) ,
  cuisine varchar(255),
  location varchar(255),
  average_rating decimal(2,1)

)

INSERT INTO Restaurant (id, name, cuisine, location, average_rating) VALUES
(1, 'Toit', 'Microbrewery, Italian', 'Indiranagar, Bangalore', 4.7),
(2, 'Peter Cat', 'North Indian, Mughlai', 'Park Street, Kolkata', 4.5),
(3, 'Leopold Cafe', 'Cafe, Chinese, Continental', 'Colaba, Mumbai', 4.2),
(4, 'Indian Accent', 'Modern Indian', 'Lodhi Road, New Delhi', 4.9),
(5, 'Truffles', 'Burgers, American, Desserts', 'Koramangala, Bangalore', 4.6);

```