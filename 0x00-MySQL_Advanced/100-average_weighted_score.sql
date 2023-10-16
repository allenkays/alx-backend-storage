--  SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;

    -- Initialize variables
    SET total_score = 0;
    SET total_weight = 0;

    -- Calculate the weighted average score for the specified user
    SELECT SUM(c.score * p.weight) INTO total_score, SUM(p.weight) INTO total_weight
    FROM corrections c
    JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    -- Update the average_score for the user
    UPDATE users
    SET average_score = total_score / total_weight
    WHERE id = user_id;
END //
DELIMITER ;
