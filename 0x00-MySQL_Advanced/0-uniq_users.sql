-- SQL script that creates a table users following these requirements:
-- attributes:id, email, name
-- Creates a table users only if it does not exist

CREATE TABLE IF NOT EXISTS `users`(
  `id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `email` VARCHAR(255) NOT NULL UNIQUE,
  `name` VARCHAR(255),
);
