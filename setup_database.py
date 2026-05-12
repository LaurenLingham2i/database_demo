#!/usr/bin/env python3
"""
Create and populate a relational database with artists and albums
"""
import sqlite3
from datetime import datetime

# Database connection
conn = sqlite3.connect('music_database.db')
cursor = conn.cursor()

# Drop existing tables if they exist
cursor.execute('DROP TABLE IF EXISTS albums')
cursor.execute('DROP TABLE IF EXISTS artists')

# Create artists table
cursor.execute('''
    CREATE TABLE artists (
        artist_id INTEGER PRIMARY KEY AUTOINCREMENT,
        artist_name TEXT NOT NULL UNIQUE
    )
''')

# Create albums table
cursor.execute('''
    CREATE TABLE albums (
        album_id INTEGER PRIMARY KEY AUTOINCREMENT,
        album_name TEXT NOT NULL,
        artist_id INTEGER NOT NULL,
        year_released INTEGER NOT NULL,
        genre TEXT NOT NULL,
        FOREIGN KEY (artist_id) REFERENCES artists(artist_id)
    )
''')

# Sample data for artists 
artists_data = [
    ('Biffy Clyro'),
    ('blink-182'),
    ('City and Colour'),
    ('Eminem'),
    ('Explosions in the Sky'),
    ('Fightstar'),
    ('Hell Is For Heroes'),
    ('Hundred Reasons'),
    ('Idlewild'),
    ('Linkin Park'),
    ('Manic Street Preachers'),
    ('Mogwai'),
    ('Mono'),
    ('Paramore'),
    ('Placebo'),
    ('Rise Against'),
    ('Starsailor')
]

# Sample Albums data - structured as (album_name, artist_name, year_released, genre, label)
albums_data = [
    # Biffy Clyro
    ('Blackened Sky', 'Biffy Clyro', 2002, 'Alternative Rock', 'Beggars Banquet'),
    ('The Vertigo of Bliss', 'Biffy Clyro', 2003, 'Post-Grunge', 'Beggars Banquet'),
    ('Infinity Land', 'Biffy Clyro', 2004, 'Alternative Rock', 'Beggars Banquet'),
    ('Puzzle', 'Biffy Clyro', 2007, 'Alternative Rock', '14th Floor'),
    ('Opposites', 'Biffy Clyro', 2013, 'Alternative Rock', '14th Floor'),
    ('Ellipsis', 'Biffy Clyro', 2016, 'Alternative Rock', '14th Floor'),
    ('Balance, Not Symmetry', 'Biffy Clyro', 2019, 'Alternative Rock', '14th Floor'),
    ('A Celebration of Endings', 'Biffy Clyro', 2020, 'Alternative Rock', '14th Floor'),
    ('The Myth of the Happily Ever After', 'Biffy Clyro', 2021, 'Alternative Rock', '14th Floor'),
    ('Futique', 'Biffy Clyro', 2025, 'Alternative Rock', '14th Floor'),
    
    # blink-182
    ('Cheshire Cat', 'blink-182', 1994, 'Pop Punk', 'Cargo'),
    ('Dude Ranch', 'blink-182', 1997, 'Pop Punk', 'Cargo'),
    ('Enema of the State', 'blink-182', 1999, 'Pop Punk', 'MCA'),
    ('Take Off Your Pants and Jacket', 'blink-182', 2001, 'Pop Punk', 'MCA'),
    ('Blink-182', 'blink-182', 2003, 'Pop Punk', 'Geffen'),
    ('Neighborhoods', 'blink-182', 2011, 'Pop Punk', 'DGC'),
    ('California', 'blink-182', 2016, 'Pop Punk', 'BMG'),
    ('Nine', 'blink-182', 2019, 'Pop Punk', 'Columbia'),
    ('One More Time...', 'blink-182', 2023, 'Pop Punk', 'Columbia'),
    
    # City and Colour
    ('Sometimes', 'City and Colour', 2005, 'Folk Rock', 'Dine Alone'),
    ('Bring Me Your Love', 'City and Colour', 2008, 'Folk Rock', 'Dine Alone'),
    ('Little Hell', 'City and Colour', 2011, 'Folk Rock', 'Dine Alone'),
    ('The Hurry and the Harm', 'City and Colour', 2013, 'Folk Rock', 'Dine Alone'),
    ('If I Should Go Before You', 'City and Colour', 2015, 'Folk Rock', 'Dine Alone'),
    ('A Pill for Loneliness', 'City and Colour', 2019, 'Folk Rock', 'Still'),
    ('The Love Still Held Me Near', 'City and Colour', 2023, 'Folk Rock', 'Still'),
    
    # Eminem
    ('Infinite', 'Eminem', 1996, 'Hip Hop', 'Web'),
    ('The Slim Shady LP', 'Eminem', 1999, 'Hip Hop', 'Aftermath'),
    ('The Marshall Mathers LP', 'Eminem', 2000, 'Hip Hop', 'Aftermath'),
    ('The Eminem Show', 'Eminem', 2002, 'Hip Hop', 'Shady'),
    ('Encore', 'Eminem', 2004, 'Hip Hop', 'Shady'),
    ('Relapse', 'Eminem', 2009, 'Hip Hop', 'Shady'),
    ('Recovery', 'Eminem', 2010, 'Hip Hop', 'Shady'),
    ('The Marshall Mathers LP 2', 'Eminem', 2013, 'Hip Hop', 'Shady'),
    ('Revival', 'Eminem', 2017, 'Hip Hop', 'Shady'),
    ('Kamikaze', 'Eminem', 2018, 'Hip Hop', 'Shady'),
    ('Music to Be Murdered By', 'Eminem', 2020, 'Hip Hop', 'Shady'),
    ('The Death of Slim Shady', 'Eminem', 2024, 'Hip Hop', 'Shady'),

    # Explosions in the Sky
    ('How Strange, Innocence', 'Explosions in the Sky', 2000, 'Post-Rock', 'Ultimate Dilemma'),
    ('Earth Is Not a Cold Dead Place', 'Explosions in the Sky', 2001, 'Post-Rock', 'Temporary Residence'),
    ('The Earth Is Not a Cold Dead Place', 'Explosions in the Sky', 2003, 'Post-Rock', 'Temporary Residence'),
    ('We Look Like Clouds', 'Explosions in the Sky', 2006, 'Post-Rock', 'Temporary Residence'),

    # Fightstar
    ('Grand Unification', 'Fightstar', 2006, 'Alternative Rock', 'Island'),
    ('One Day Son, This Will All Be Yours', 'Fightstar', 2006, 'Alternative Rock', 'Gut'),
    ('Be Human', 'Fightstar', 2009, 'Alternative Rock', 'Search and Destroy'),
    ('Behind the Devil\'s Back', 'Fightstar', 2015, 'Alternative Rock', 'Warner'),

    # Hell Is For Heroes
    ('The Neon Handshake', 'Hell Is For Heroes', 2003, 'Alternative Rock', 'EMI'),
    ('Transmit Disrupt', 'Hell Is For Heroes', 2005, 'Alternative Rock', 'Captains of Industry'),
    ('Hell Is For Heroes', 'Hell Is For Heroes', 2007, 'Alternative Rock', 'Golf'),
        
    # Hundred Reasons
    ('Ideas Above Our Station', 'Hundred Reasons', 2002, 'Post-Grunge', 'Columbia'),
    ('Shatterproof Is Not a Challenge', 'Hundred Reasons', 2004, 'Post-Grunge', 'Columbia'),
    ('Kill Your Own', 'Hundred Reasons', 2006, 'Post-Grunge', 'V2'),
    ('Quick the Word, Sharp the Action', 'Hundred Reasons', 2007, 'Post-Grunge', 'V2'),
    ('Glorious Sunset', 'Hundred Reasons', 2023, 'Post-Grunge', 'SO Recordings'),

    # Idlewild
    ('Captain', 'Idlewild', 1998, 'Indie Rock', 'Deceptive Records'),
    ('Hope is Important', 'Idlewild', 1998, 'Indie Rock', 'Food Records'),
    ('100 Broken Windows', 'Idlewild', 2000, 'Indie Rock', 'Food Records'),
    ('The Remote Part', 'Idlewild', 2002, 'Indie Rock', 'Parlophone'),
    ('Warnings/Promises', 'Idlewild', 2005, 'Indie Rock', 'Parlophone'),
    ('Make Another World', 'Idlewild', 2007, 'Indie Rock', 'Sequel Records'),
    ('Post Electric Blues', 'Idlewild', 2009, 'Indie Rock', 'Cooking Vinyl'),
    ('Everything Ever Written', 'Idlewild', 2015, 'Indie Rock', 'Empty Words'),
    ('Interview Music', 'Idlewild', 2019, 'Indie Rock', 'Empty Words'),
    ('Idlewild', 'Idlewild', 2025, 'Indie Rock', 'V2'),

    # Linkin Park
    ('Hybrid Theory', 'Linkin Park', 2000, 'Nu Metal', 'Warner Bros.'),
    ('Meteora', 'Linkin Park', 2003, 'Nu Metal', 'Warner Bros.'),
    ('Minutes to Midnight', 'Linkin Park', 2007, 'Nu Metal', 'Warner Bros.'),
    ('A Thousand Suns', 'Linkin Park', 2010, 'Nu Metal', 'Warner Bros.'),
    ('Living Things', 'Linkin Park', 2012, 'Nu Metal', 'Warner Bros.'),
    ('The Hunting Party', 'Linkin Park', 2014, 'Nu Metal', 'Warner Bros.'),
    ('One More Light', 'Linkin Park', 2017, 'Nu Metal', 'Warner Bros.'),
    ('From Zero', 'Linkin Park', 2024, 'Nu Metal', 'Warner Bros.'),

    # Manic Street Preachers
    ('Generation Terrorists', 'Manic Street Preachers', 1992, 'Alternative Rock', 'Columbia'),
    ('Gold Against the Soul', 'Manic Street Preachers', 1993, 'Alternative Rock', 'Columbia'),
    ('The Holy Bible', 'Manic Street Preachers', 1994, 'Alternative Rock', 'Epic'),
    ('Everything Must Go', 'Manic Street Preachers', 1996, 'Alternative Rock', 'Epic'),
    ('This Is My Truth Tell Me Yours', 'Manic Street Preachers', 1998, 'Alternative Rock', 'Epic'),
    ('Know Your Enemy', 'Manic Street Preachers', 2001, 'Alternative Rock', 'Epic'),
    ('Lifeblood', 'Manic Street Preachers', 2004, 'Alternative Rock', 'Epic'),
    ('Send Away the Tigers', 'Manic Street Preachers', 2007, 'Alternative Rock', 'Columbia'),
    ('Journal for Plague Lovers', 'Manic Street Preachers', 2009, 'Alternative Rock', 'Columbia'),
    ('Postcards from a Young Man', 'Manic Street Preachers', 2010, 'Alternative Rock', 'Columbia'),
    ('Rewind the Film', 'Manic Street Preachers', 2013, 'Alternative Rock', 'Columbia'),
    ('Futurology', 'Manic Street Preachers', 2014, 'Alternative Rock', 'Columbia'),
    ('Resistance Is Futile', 'Manic Street Preachers', 2018, 'Alternative Rock', 'Columbia'),
    ('Critical Thinking', 'Manic Street Preachers', 2025, 'Alternative Rock', 'Columbia'),

    # Mono
    ('Under the Pipal Tree', 'Mono', 2001, 'Post-Rock', 'Tzadik'),
    ('One Step More and You Die', 'Mono', 2002, 'Post-Rock', 'Arena Rock'),
    ('Walking Cloud and Deep Red Sky, Flag Fluttered and the Sun Shined', 'Mono', 2004, 'Post-Rock', 'Temporary Residence'),
    ('You Are There', 'Mono', 2006, 'Post-Rock', 'Temporary Residence'),
    ('Hymn to the Immortal Wind', 'Mono', 2009, 'Post-Rock', 'Temporary Residence'),
    ('For My Parents', 'Mono', 2012, 'Post-Rock', 'Temporary Residence'),
    ('Rays of Darkness', 'Mono', 2014, 'Post-Rock', 'Temporary Residence'),
    ('The Last Dawn', 'Mono', 2014, 'Post-Rock', 'Temporary Residence'),
    ('Requiem for Hell', 'Mono', 2016, 'Post-Rock', 'Temporary Residence'),
    ('Nowhere Now Here', 'Mono', 2019, 'Post-Rock', 'Temporary Residence'),
    ('Pilgrimage of the Soul', 'Mono', 2021, 'Post-Rock', 'Temporary Residence'),
    ('OATH', 'Mono', 2024, 'Post-Rock', 'Temporary Residence'),

    # Mogwai
    ('Mogwai Young Team', 'Mogwai', 1997, 'Post-Rock', 'Chemikal Underground'),
    ('Come On Die Young', 'Mogwai', 1999, 'Post-Rock', 'Chemikal Underground'),
    ('Rock Action', 'Mogwai', 2001, 'Post-Rock', 'Play It Again Sam'),
    ('Happy Songs for Happy People', 'Mogwai', 2003, 'Post-Rock', 'Play It Again Sam'),
    ('The Hawk Is Howling', 'Mogwai', 2008, 'Post-Rock', 'Wall of Sound'),
    ('Hardcore Will Never Die, But You Will', 'Mogwai', 2011, 'Post-Rock', 'Rock Action'),
    ('Les Revenants', 'Mogwai', 2013, 'Post-Rock', 'Rock Action'),
    ('Rave Tapes', 'Mogwai', 2014, 'Post-Rock', 'Rock Action'),
    ('Atomic', 'Mogwai', 2016, 'Post-Rock', 'Rock Action'),
    ('Every Country\'s Sun', 'Mogwai', 2017, 'Post-Rock', 'Rock Action'),
    ('Kin', 'Mogwai', 2018, 'Post-Rock', 'Rock Action'),
    ('ZeroZeroZero', 'Mogwai', 2020, 'Post-Rock', 'Rock Action'),
    ('As the Love Continues', 'Mogwai', 2021, 'Post-Rock', 'Rock Action'),
    ('Black Bird', 'Mogwai', 2022, 'Post-Rock', 'Rock Action'),
    ('The Bad Fire', 'Mogwai', 2025, 'Post-Rock', 'Rock Action'),

    # Paramore
    ('All We Know Is Falling', 'Paramore', 2005, 'Pop Rock', 'Fueled by Ramen'),
    ('Riot!', 'Paramore', 2007, 'Pop Rock', 'Fueled by Ramen'),
    ('Brand New Eyes', 'Paramore', 2009, 'Pop Rock', 'Fueled by Ramen'),
    ('Paramore', 'Paramore', 2013, 'Pop Rock', 'Fueled by Ramen'),
    ('After Laughter', 'Paramore', 2017, 'Pop Rock', 'Fueled by Ramen'),
    ('This Is Why', 'Paramore', 2023, 'Pop Rock', 'Atlantic'),

    # Placebo
    ('Placebo', 'Placebo', 1996, 'Electronic Rock', 'Virgin'),
    ('Without You I\'m Nothing', 'Placebo', 1998, 'Alternative Rock', 'Virgin'),
    ('Black Market Music', 'Placebo', 2000, 'Electronic Rock', 'Virgin'),
    ('Sleeping with Ghosts', 'Placebo', 2003, 'Electronic Rock', 'Virgin'),
    ('Meds', 'Placebo', 2006, 'Electronic Rock', 'Virgin'),
    ('Battle for the Sun', 'Placebo', 2009, 'Electronic Rock', 'PIAS'),
    ('Loud Like Love', 'Placebo', 2013, 'Electronic Rock', 'Vertigo'),
    ('Never Let Me Go', 'Placebo', 2022, 'Electronic Rock', 'SO Recordings'),

    # Rise Against
    ('The Unraveling', 'Rise Against', 2001, 'Punk Rock', 'Fat Wreck Chords'),
    ('Revolutions per Minute', 'Rise Against', 2003, 'Punk Rock', 'Fat Wreck Chords'),
    ('Siren Song of the Counter Culture', 'Rise Against', 2004, 'Punk Rock', 'Geffen'),
    ('The Sufferer & the Witness', 'Rise Against', 2006, 'Punk Rock', 'Geffen'),
    ('Appeal to Reason', 'Rise Against', 2008, 'Punk Rock', 'DGC'),
    ('Endgame', 'Rise Against', 2011, 'Punk Rock', 'DGC'),
    ('The Black Market', 'Rise Against', 2014, 'Punk Rock', 'Interscope'),
    ('Wolves', 'Rise Against', 2017, 'Punk Rock', 'Virgin'),
    ('Nowhere Generation', 'Rise Against', 2021, 'Punk Rock', 'Loma Vista'),
    ('Ricochet', 'Rise Against', 2025, 'Punk Rock', 'Loma Vista'),

    # Starsailor
    ('Love Is Here', 'Starsailor', 2001, 'Alternative Rock', 'EMI'),
    ('Silence Is Easy', 'Starsailor', 2003, 'Alternative Rock', 'EMI'),
    ('On the Outside', 'Starsailor', 2005, 'Alternative Rock', 'EMI'),
    ('All the Plans', 'Starsailor', 2009, 'Alternative Rock', 'EMI'),
    ('All This Life', 'Starsailor', 2017, 'Alternative Rock', 'Cooking Vinyl'),
    ('Where the Wild Things Grow', 'Starsailor', 2024, 'Alternative Rock', 'Townsend'),
]

# Insert artists
for artist_name in artists_data:
    cursor.execute(
        'INSERT INTO artists (artist_name) VALUES (?)',
        (artist_name,)
    )

# Insert Albums with proper artist_id foreign key
for album_name, artist_name, year, genre, label in albums_data:
    # Get the artist_id for this artist
    cursor.execute('SELECT artist_id FROM artists WHERE artist_name = ?', (artist_name,))
    result = cursor.fetchone()
    if result:
        artist_id = result[0]
        cursor.execute(
            'INSERT INTO albums (album_name, artist_id, year_released, genre, label) VALUES (?, ?, ?, ?, ?)',
            (album_name, artist_id, year, genre, label)
        )

# Commit the changes
conn.commit()

print("✓ Database created successfully!")
print(f"✓ Inserted {len(artists_data)} artists")
print(f"✓ Inserted {len(albums_data)} albums")

# Display summary
print("\n--- Database Summary ---")
cursor.execute('SELECT COUNT(*) FROM artists')
artist_count = cursor.fetchone()[0]
cursor.execute('SELECT COUNT(*) FROM albums')
album_count = cursor.fetchone()[0]
print(f"Total Artists: {artist_count}")
print(f"Total Albums: {album_count}")

# Display a sample query
print("\n--- Sample Data ---")
cursor.execute('''
SELECT a.artist_name, c.album_name, c.year_released, c.genre
FROM albums c
JOIN artists a ON c.artist_id = a.artist_id
LIMIT 10
''')
print("\nSample Albums:")
for row in cursor.fetchall():
    print(f"  {row[0]:30} - {row[1]:40} ({row[2]}) [{row[3]}]")

conn.close()
