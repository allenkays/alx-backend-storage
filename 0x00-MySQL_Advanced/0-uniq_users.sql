-- SQL script that creates a table users following these requirements:
-- With these attributes:
-- id, integer, never null, auto increment and primary key email, string (255 characters), never null and unique name, string (255 characters)

-- Creates a table users only if it does not exist
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT NOT NULL,
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255)
  PRIMARY KEY (id),
  UNIQUE (email)
  );
