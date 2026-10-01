## task 1:Create two tables: Influencers (id, name) and Collaborations (id, influencer1_id, influencer2_id, collab_date). Write a SQL FULL JOIN query to list all influencers and show their collaboration partner names if any, including influencers with no collaborations.


CREATE table Influencers 
(id int primary key AUTO_INCREMENT,
 name varchar(255)
) ;
CREATE table Collaborations 
(id int primary key,
 influencer1_id int , 
 influencer2_id int , 
 collab_date date , 
 FOREIGN key (influencer1_id) REFERENCES influencers (id)
 FOREIGN key (influencer2_id) REFERENCES influencers (id)
);

SELECT 
    i.name AS influencer_name,
    p.name AS partner_name,
    c.collab_date
FROM Influencers i
LEFT JOIN Collaborations c ON i.id = c.influencer1_id
LEFT JOIN Influencers p ON c.influencer2_id = p.id