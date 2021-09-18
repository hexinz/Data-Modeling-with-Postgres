# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS SONGPLAYS"
user_table_drop = "DROP TABLE IF EXISTS USERS"
song_table_drop = "DROP TABLE IF EXISTS SONGS"
artist_table_drop = "DROP TABLE IF EXISTS ARTISTS"
time_table_drop = "DROP TABLE IF EXISTS TIME"
# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE SONGPLAYS (
    songplays SERIAL PRIMARY KEY,
    start_time TIMESTAMP NOT NULL, 
    user_id INTEGER NOT NULL, 
    level  VARCHAR(30), 
    song_id VARCHAR(60), 
    artist_id VARCHAR(60), 
    session_id INTEGER, 
    location VARCHAR(200),
    user_agent TEXT
)
""")

user_table_create = ("""
CREATE TABLE USERS (
    user_id INTEGER PRIMARY KEY,
    first_name VARCHAR(60) NOT NULL,
    last_name VARCHAR(60) NOT NULL,
    gender VARCHAR(30),
    level VARCHAR(30) UNIQUE
)
""")

song_table_create = ("""
CREATE TABLE SONGS (
    song_id VARCHAR(60) PRIMARY KEY,
    title VARCHAR(200) NOT NULL UNIQUE,
    artist_id VARCHAR(60) NOT NULL,
    year INTEGER,
    duration NUMERIC NOT NULL
)
""")

artist_table_create = ("""
CREATE TABLE ARTISTS (
    artist_id VARCHAR(60) PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    location VARCHAR(200),
    latitude NUMERIC,
    longitude NUMERIC
)
""")

time_table_create = ("""
CREATE TABLE TIME (
    start_time TIMESTAMP PRIMARY KEY, 
    hour INTEGER NOT NULL, 
    day INTEGER NOT NULL, 
    week INTEGER NOT NULL, 
    month INTEGER NOT NULL, 
    year INTEGER NOT NULL, 
    weekday INTEGER NOT NULL
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO SONGPLAYS (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES 
(%s, %s, %s, %s, %s, %s, %s, %s) 
ON CONFLICT DO NOTHING
""")

user_table_insert = ("""
INSERT INTO USERS (user_id, first_name, last_name, gender, level) VALUES 
(%s, %s, %s, %s, %s) 
ON CONFLICT (level) DO UPDATE SET level = EXCLUDED.level
""")

song_table_insert = ("""
INSERT INTO SONGS (song_id, title, artist_id, year, duration) VALUES 
(%s, %s, %s, %s, %s)
ON CONFLICT (title) DO UPDATE SET title = EXCLUDED.title
""")

artist_table_insert = ("""
INSERT INTO ARTISTS (artist_id, name, location, latitude, longitude) VALUES 
(%s, %s, %s, %s, %s) 
ON CONFLICT DO NOTHING
""")


time_table_insert = ("""
INSERT INTO TIME (start_time, hour, day, week, month, year, weekday) VALUES 
(%s, %s, %s, %s, %s, %s, %s) 
ON CONFLICT DO NOTHING
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, s.artist_id FROM songs s 
join artists a on s.artist_id = a.artist_id 
WHERE s.title = %s and a.name = %s and s.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]