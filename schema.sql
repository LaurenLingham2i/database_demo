-- Music Database Schema
-- This schema defines a relational database for managing artists and their albums

-- Create artists table
CREATE TABLE artists (
    artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    artist_name TEXT NOT NULL UNIQUE
);

-- Create albums table
CREATE TABLE albums (
    album_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    artist_id INTEGER NOT NULL,
    year_released INTEGER NOT NULL,
    genre TEXT NOT NULL,
    label TEXT NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
);

-- Index for faster lookups
CREATE INDEX idx_albums_artist_id ON albums(artist_id);
CREATE INDEX idx_artists_name ON artists(artist_name);

-- Sample queries:

-- Get all albums by an artist
-- SELECT c.name, c.year_released, c.genre 
-- FROM albums c
-- WHERE c.artist_id = (SELECT artist_id FROM artists WHERE artist_name = 'Biffy Clyro')
-- ORDER BY c.year_released;

-- Get artist information with album count
-- SELECT a.artist_name, COUNT(c.album_id) as albums_in_db
-- FROM artists a
-- LEFT JOIN albums c ON a.artist_id = c.artist_id
-- GROUP BY a.artist_id
-- ORDER BY a.artist_name;

-- Get all albums ordered by year
-- SELECT a.artist_name, c.name, c.year_released, c.genre
-- FROM albums c
-- JOIN artists a ON c.artist_id = a.artist_id
-- ORDER BY c.year_released;

-- Get albums by genre
-- SELECT c.genre, COUNT(*) as count
-- FROM albums c
-- GROUP BY c.genre
-- ORDER BY count DESC;
