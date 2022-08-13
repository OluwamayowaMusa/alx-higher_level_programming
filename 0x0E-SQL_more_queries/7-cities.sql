-- Create a database and a table wih constraint
CREATE database IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE table IF NOT EXISTS cities
  (id INT NOT NULL PRIMARY KEY UNIQUE AUTO_INCREMENT,
   state_id INT NOT NULL, FOREIGN KEY(id) REFERENCES states(id),
   name VARCHAR(256) NOT NULL
  );
