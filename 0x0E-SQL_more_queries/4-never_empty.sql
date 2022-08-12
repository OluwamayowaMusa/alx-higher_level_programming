-- Create table id_not_null with constraint PRIMARY KEY
CREATE table IF NOT EXISTS id_not_null
  (id INT PRIMARY KEY DEFAULT 1,
   name VARCHAR(256)
  );
