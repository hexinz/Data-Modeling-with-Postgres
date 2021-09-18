# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS SONGPLAY"
user_table_drop = "DROP TABLE IF EXISTS USER_TABLE"
song_table_drop = "DROP TABLE IF EXISTS SONG"
artist_table_drop = "DROP TABLE IF EXISTS ARTIST"
time_table_drop = "DROP TABLE IF EXISTS TIME"
# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE SONGPLAY (
    start_time BIGINT, 
    userId INTEGER, 
    level  VARCHAR(30), 
    songId VARCHAR(60), 
    artistId VARCHAR(60), 
    sessionId INTEGER, 
    location VARCHAR(200),
    userAgent TEXT,
    PRIMARY KEY (start_time, userId)
)
""")

user_table_create = ("""
CREATE TABLE USER_TABLE (
    userId INTEGER PRIMARY KEY,
    firstName VARCHAR(60) NOT NULL,
    lastName VARCHAR(60) NOT NULL,
    gender VARCHAR(30),
    level VARCHAR(30)
)
""")

song_table_create = ("""
CREATE TABLE SONG (
    song_id VARCHAR(60) PRIMARY KEY,
    title VARCHAR(200) NOT NULL UNIQUE,
    artist_id VARCHAR(60) NOT NULL,
    year INTEGER,
    duration NUMERIC NOT NULL
)
""")

artist_table_create = ("""
CREATE TABLE ARTIST (
    artist_id VARCHAR(60) PRIMARY KEY,
    artist_name VARCHAR(200) NOT NULL,
    artist_location VARCHAR(200),
    artist_latitude NUMERIC,
    artist_longitude NUMERIC
)
""")

time_table_create = ("""
CREATE TABLE TIME (
    start_time BIGINT PRIMARY KEY, 
    hour INTEGER NOT NULL, 
    day INTEGER NOT NULL, 
    week_of_year INTEGER NOT NULL, 
    month INTEGER NOT NULL, 
    year INTEGER NOT NULL, 
    weekday INTEGER NOT NULL
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO SONGPLAY (start_time, userId, level, songId, artistId, sessionId, location, userAgent) VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s) 
ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
INSERT INTO USER_TABLE (userId, firstName, lastName, gender, level) VALUES 
(%s, %s, %s, %s, %s) 
ON CONFLICT DO NOTHING
""")

song_table_insert = ("""
INSERT INTO SONG (song_id, title, artist_id, year, duration) VALUES 
(%s, %s, %s, %s, %s)
ON CONFLICT (title) DO UPDATE SET title = EXCLUDED.title
""")

artist_table_insert = ("""
INSERT INTO ARTIST (artist_id, artist_name, artist_location, artist_latitude, artist_longitude) VALUES 
(%s, %s, %s, %s, %s) 
ON CONFLICT DO NOTHING
""")


time_table_insert = ("""
INSERT INTO TIME (start_time, hour, day, week_of_year, month, year, weekday) VALUES 
(%s, %s, %s, %s, %s, %s, %s) 
ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT songid, artistid FROM songplay sp
join song s on sp.songId = s.song_id
join artist a on sp.artistId = a.artist_id 
WHERE s.title = %s and a.artist_name = %s and s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]