-- Creates a table unique_id with UNIQUE constraint
CREATE table IF NOT EXISTS unique_id
  (id INT DEFAULT 1 UNIQUE,
   name VARCHAR(256)
  );
