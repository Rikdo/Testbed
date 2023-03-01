--Advanced Select
--The Pads
----------------------------------------------------------------
--After several attempts and refferencing comments from other users, I believe there is an error in the compiler check for this problem.
--The compiler outputs the first query as needed, but outputs the second query with it's collumn header inline.  
--Below you see my attempts to use a UNION clause to get around this, but couldn't get the proper grouping/ordering when I did.
--Moving on to other problem for now, and will loop back to this at a later date.

SELECT CONCAT(Name,'(',LEFT(Occupation, 1),')')
FROM OCCUPATIONS
ORDER BY Name;

SELECT CONCAT('There are a total of ',COUNT(Occupation),' ',LOWER(Occupation),'s.')
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY Count(Occupation), Occupation;

        -- Union attempt, failed
        SELECT * FROM (
            SELECT CONCAT(Name,'(',LEFT(Occupation, 1),')') AS C1
            FROM OCCUPATIONS
            ORDER BY Name
        ) AS sub
        UNION
        SELECT * FROM (
            SELECT CONCAT('There are a total of ',COUNT(Occupation),' ',Occupation,'s.') AS C2
            FROM OCCUPATIONS
            GROUP BY Occupation
            ORDER BY COUNT(Occupation), Occupation
        ) AS sub2;

        -- Order outside the union attempt, failed
        SELECT C1, "Z" AS C2 FROM (
            SELECT CONCAT(Name,'(',LEFT(Occupation, 1),')') AS C1
            FROM OCCUPATIONS
            ORDER BY Name ASC
        ) AS T1
        UNION
        SELECT C2, "Z" AS C1 FROM (
            SELECT CONCAT('There are a total of ',COUNT(Occupation),' ',Occupation,'s.') AS C2
            FROM OCCUPATIONS
            GROUP BY Occupation
            ORDER BY COUNT(*), Occupation
        ) AS T2
        ORDER BY C1, C2;

        --AI Suggestion, failed
        SELECT C1
        FROM (SELECT CONCAT(Name, '(', LEFT(Occupation, 1), ')') AS C1,
                    Occupation,
                    COUNT(*) AS C2
            FROM OCCUPATIONS
            GROUP BY Name, Occupation
            UNION
            SELECT CONCAT('There are a total of ', COUNT(*), ' ', LOWER(Occupation), 's.') AS C1,
                    Occupation,
                    COUNT(*) AS C2
            FROM OCCUPATIONS
            GROUP BY COUNT(*) Occupation) AS T
        ORDER BY C2, Occupation, C1;

--Occupations
SELECT 
    CASE WHEN Occupation LIKE "D%" THEN Name END AS Doctor,
    CASE WHEN Occupation LIKE "P%" THEN Name END AS Professor,
    CASE WHEN Occupation LIKE "S%" THEN Name END AS Singer,
    CASE WHEN Occupation LIKE "A%" THEN Name END AS Actor
FROM OCCUPATIONS
ORDER BY Doctor, Professor, Singer, Actor

        --AI
        SELECT
        IFNULL(D.Name, 'NULL') AS Doctor,
        IFNULL(P.Name, 'NULL') AS Professor,
        IFNULL(S.Name, 'NULL') AS Singer,
        IFNULL(A.Name, 'NULL') AS Actor
        FROM
        (SELECT Name, ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS RowNum
        FROM OCCUPATIONS WHERE Occupation = 'Doctor') D
        LEFT JOIN
        (SELECT Name, ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS RowNum
        FROM OCCUPATIONS WHERE Occupation = 'Professor') P
        ON D.RowNum = P.RowNum
        LEFT JOIN
        (SELECT Name, ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS RowNum
        FROM OCCUPATIONS WHERE Occupation = 'Singer') S
        ON D.RowNum = S.RowNum
        LEFT JOIN
        (SELECT Name, ROW_NUMBER() OVER (PARTITION BY Occupation ORDER BY Name) AS RowNum
        FROM OCCUPATIONS WHERE Occupation = 'Actor') A
        ON D.RowNum = A.RowNum;

        --https://dogsavestheworld.tistory.com/107
        SELECT MIN(CASE WHEN Occupation LIKE 'D%' THEN Name END)AS Docter
            , MIN(CASE WHEN Occupation LIKE 'P%' THEN Name END)AS Professor
            , MIN(CASE WHEN Occupation LIKE 'S%' THEN Name END)AS Singer
            , MIN(CASE WHEN Occupation LIKE 'A%' THEN Name END)AS Actor
        FROM (
            SELECT 
                a.Occupation as Occupation,
                a.Name as Name,
                (SELECT COUNT(*) 
                    FROM Occupations AS b
                    WHERE a.Occupation = b.Occupation AND a.Name > b.Name) as Rank_num
            FROM Occupations AS a
            ORDER BY a.Occupation, a.Name ) as tmp
        GROUP BY tmp.Rank_num

--Binary Tree Nodes
SELECT N, 
    CASE
        WHEN ISNULL(P) THEN "Root"
        WHEN N IN (SELECT P FROM BST) THEN "Inner"
        ELSE "Leaf"
    END AS Node_Type
FROM BST
ORDER BY N