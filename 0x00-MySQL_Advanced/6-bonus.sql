-- SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
  DECLARE project_id INT;

  /* Check if the project_name already exists */
  SELECT id INTO project_id FROM projects WHERE name = project_name LIMIT 1;

  /* If project_name does not exist create a new project */
  IF project_id IS NULL THEN
    INSERT INTO projects(name) values(project_name);
    SET project_id = LAST_INSERT_ID();
  END IF;

  /* Insert the correction */
  INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);

END;
$$
DELIMITER ;
