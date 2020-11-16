-- This script updates the score of Bob to 10 in the second_table
UPDATE second_table
    SET score=10
    WHERE second_table.name="Bob";
