-- Script to create trigger that resets the attribute valid_email
-- only whem email has been changed.

DELIMITER //

CREATE TRIGGER reset 
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
  IF NEW.email <> OLD.email THEN
    set NEW.valid_email = 0;
  END IF;
END //
DELIMITER ;
