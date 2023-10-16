--  SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student.
DELIMITER //

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    -- Declare variables to hold the computed values
    DECLARE total_weighted_score DECIMAL(10, 2);
    DECLARE total_weight DECIMAL(10, 2);
    DECLARE average_weighted_score DECIMAL(10, 2);

    -- Calculate the total weighted score and total weight for the user
    SELECT
        SUM(c.score * p.weight) INTO total_weighted_score,
        SUM(p.weight) INTO total_weight
    FROM
        corrections c
    JOIN
        projects p ON c.project_id = p.id
    WHERE
        c.user_id = user_id;

    -- Check if there are scores for the user
    IF total_weight IS NOT NULL THEN
        -- Calculate the average weighted score
        SET average_weighted_score = total_weighted_score / total_weight;

        -- Update the user's average_score in the users table
        UPDATE users
        SET average_score = average_weighted_score
        WHERE id = user_id;
    END IF;
END //

DELIMITER ;
