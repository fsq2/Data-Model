# DROP TABLES

songplay_table_drop = "DROP table IF EXISTS songplays"
user_table_drop = "Drop table IF EXISTS users"
song_table_drop = "Drop table IF EXISTS songs"
artist_table_drop ="Drop table IF EXISTS artists"
time_table_drop = "Drop table  IF EXISTS time"

# CREATE TABLES

# creating songplay table SERIAL incrment the songplay_id
songplay_table_create = (""" 
CREATE TABLE IF NOT EXISTS
songplays(
songplay_id SERIAL PRIMARY KEY not null,
start_time timestamp not null , 
user_id varchar not null, level varchar, 
song_id varchar, artist_id varchar,
session_id  varchar not null , 
location varchar, user_agent varchar)""")
     
user_table_create = ("""
CREATE TABLE IF NOT EXISTS users(
user_id varchar not null primary key,
first_name varchar not null,
last_name varchar not null,
gender char,
level varchar
)
""")
# craete songs table 
song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs(
song_id varchar not null primary key, title varchar, 
artist_id varchar not null, year int ,duration float)""")
# artist table 
artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists(
artist_id varchar not null primary key ,
 name varchar not null, 
location varchar, latitude text, longitude text)""")
# time table 
time_table_create = ("""
CREATE TABLE IF NOT EXISTS time(
start_time timestamp primary key not null, hour int not null, day int not null, 
week int not null, month int not null,
 year int not null, weekday int not null)""")

# INSERT RECORDS
# insert in songplay add conflict l  
songplay_table_insert = ("""
INSERT INTO songplays(
songplay_id, 
start_time,
user_id,
level,
song_id, 
artist_id,
session_id,
location, 
user_agent
)
VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT(songplay_id) DO NOTHING 

""")
#INSERT IN USER TABLE AND ADD CONFLICT when the user change thier leve

user_table_insert = ("""
INSERT INTO users(
user_id,
first_name, 
last_name, 
gender,
level) 
VALUES (%s,%s,%s,%s,%s)
ON CONFLICT(user_id) DO UPDATE SET level = excluded.level
""")
#INSERT IN SONGS TABLE AND ADD CONFLICT 

song_table_insert = ("""
INSERT INTO songs(
song_id,
title, 
 artist_id, 
 year, 
 duration) 
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT(song_id) DO NOTHING 
     """)
#INSERT IN artist TABLE AND ADD CONFLICT 

artist_table_insert = ("""
INSERT INTO artists(
artist_id, name, 
location, latitude,
longitude) 
VALUES(%s,%s,%s,%s,%s)
ON CONFLICT(artist_id) DO NOTHING 
     """)

#INSERT IN TIME TABLE AND ADD CONFLICT 
time_table_insert = ("""
INSERT INTO time(
start_time, 
hour, 
day,
week,
month,
year,
weekday) 
VALUES(%s,%s,%s,%s,%s,%s,%s)
ON CONFLICT(start_time) DO NOTHING 
""")

# FIND SONGS

song_select = ("""
SELECT songs.song_id,
artists.artist_id 
FROM songs JOIN artists
ON songs.artist_id = artists.artist_id
WHERE songs.title = %s AND artists.name=%s 
AND 
songs.duration=%s
   """) 

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]