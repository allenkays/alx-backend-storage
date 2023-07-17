-- SQL script that creates a table users following these requirements:
-- attributes:id, email, name
-- Creates a table users only if it does not exist

CREATE TABLE IF NOT EXISTS `users`(
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255),
  PRIMARY KEY (id),
  UNIQUE (email)
);
