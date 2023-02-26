-- The Pads
----------------------------------------------------------------
--After several attempts and refferencing comments from other users, I believe there is an error in the check for this problem.
--The compiler outputs the first query as needed, but outputs the second query with it's collumn header inline.  
--Below you see my attempts to use a UNION clause to get around this, but couldn't get the proper grouping/ordering when I did.
--Moving on to other problems for now, and will loop back to this at a later date.

SELECT CONCAT(Name,'(',LEFT(Occupation, 1),')')
FROM OCCUPATIONS
ORDER BY Name;

SELECT CONCAT('There are a total of ',COUNT(Occupation),' ',LOWER(Occupation),'s.')
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY Count(Occupation), Occupation;

        -- Union attempt
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

        -- The Pads
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

        --AI Suggestion
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


