--Junior Data Analyst Test Answers
-- Question 1
SELECT 
    start_date, 
    COUNT(*) AS enrollment_count
FROM mock_enrollments
GROUP BY start_date
ORDER BY start_date
LIMIT 5;

-- Question 2
SELECT COUNT(*) as enrollment_count
FROM mock_enrollments
WHERE 
    grade = 8 
    AND start_date <= '2019-02-01' 
    AND (end_date >= '2019-02-01' 
        OR end_date IS NULL);


-- Question 3
SELECT DISTINCT
    test_date AS date,
    SUM(passed) OVER (ORDER BY test_date) AS cumulative_passed_assessments
FROM mock_test_results
WHERE  date >= '2019-03-01'
ORDER BY date;

-- Question 4
SELECT
    unique_id,
    strftime('%m/%d/%Y', test_date) AS test_date,
    CASE 
        WHEN subject = 'Science' THEN 'Biology'
        ELSE subject
    END AS subject,
    CASE 
        WHEN passed = 1 THEN 'Passed'
        ELSE 'Not Passed'
    END AS result
FROM mock_test_results
WHERE test_date IS NOT NULL;