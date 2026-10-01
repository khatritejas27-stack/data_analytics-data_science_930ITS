## task 5:Given this scenario: You want to show a list of all playlists and the songs inside them, like Spotify. Explain which JOIN type (INNER, LEFT, or RIGHT) you would use to show all playlists, even if some are empty, and write the SQL query for it.

# left join use for keep evry row from left table (playlist) , even empty play list appear with null
 

```sql
SELECT
    p.name as playlist_name,
    s.title as song_title
FROM playlists p
LEFT join songs s
    on p.id = s.playlist_id
ORDER BY p.name;
```