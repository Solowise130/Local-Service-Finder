-- create new database
CREATE DATABASE IF NOT EXISTS service_finder_db;

-- create new user
CREATE USER IF NOT EXISTS user@localhost IDENTIFIED BY 'password';

-- grant all priviledges to user
GRANT ALL ON service_finder_db.* TO user@localhost;