# Music Database - Quick Reference

## Database Overview
This relational database contains information about artists and their studio albums

### Files
- **music_database.db** - SQLite database file (the actual database)
- **setup_database.py** - Python script to create and populate the database
- **schema.sql** - SQL schema and sample queries


## Database Structure

### Artists Table
| Column                  | Type    | Description                   |
|-------------------------|---------|-------------------------------|
| artist_id               | INTEGER | Primary key, auto-increment   |
| artist_name             | TEXT    | Artist name (unique)          |
| label                   | TEXT    | Record label                  |

### Albums Table
| Column        | Type    | Description                          |
|---------------|---------|--------------------------------------|
| album_id      | INTEGER | Primary key, auto-increment          | 
| album_name    | TEXT    | Album name                           |
| artist_id     | INTEGER | Foreign key to artists table         |
| year_released | INTEGER | Release year                         |
| genre         | TEXT    | Music genre                          |
| label         | TEXT    | Music label album was released under |


## Useful SQL Queries

### View all alcums with artist information
```sql
SELECT a.artist_name, c.album_name, c.year_released, c.genre
FROM albums c
JOIN artists a ON c.artist_id = a.artist_id
ORDER BY c.year_released;
```

### Find alcums by a specific artist
```sql
SELECT c.album_name, c.year_released, c.genre
FROM albums c
WHERE c.artist_id = (SELECT artist_id FROM artists WHERE artist_name = 'Biffy Clyro')
ORDER BY c.year_released;
```

### Count albums by genre
```sql
SELECT c.genre, COUNT(*) as count
FROM albums c
GROUP BY c.genre
ORDER BY count DESC;
```

### View artist details
```sql
SELECT a.artist_name, a.number_of_studio_albums, a.label, COUNT(c.album_id) as albums_in_db
FROM artists a
LEFT JOIN albums c ON a.artist_id = c.artist_id
GROUP BY a.artist_id
ORDER BY a.artist_name;
```


## How to Use

### Python
```python
import sqlite3

conn = sqlite3.connect('music_database.db')
cursor = conn.cursor()

# Example: Get all albums
cursor.execute('SELECT * FROM albums LIMIT 10')
for row in cursor.fetchall():
    print(row)

conn.close()
```

### Command Line (sqlite3)
```bash
sqlite3 music_database.db
sqlite> SELECT * FROM artists;
sqlite> SELECT * FROM albums;
```
