-- Create a database and a table with constraint in the database
CREATE database IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE table IF NOT EXISTS states
  (id int UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT,
   name VARCHAR(256) NOT NULL
  );
