--SQL Script that creates the table unique_id on MYSQL server.
CREATE TABLE IF NOT EXISTS `unique_id` (`id` INT DEFAULT 1 UNIQUE, `name` VARCHAR(256));
