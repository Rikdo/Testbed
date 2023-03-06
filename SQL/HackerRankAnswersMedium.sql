--Advanced Select: The Pads
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

--Advanced Select: Occupations
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

--Advanced Select: Binary Tree Nodes
SELECT N, 
    CASE
        WHEN ISNULL(P) THEN "Root"
        WHEN N IN (SELECT P FROM BST) THEN "Inner"
        ELSE "Leaf"
    END AS Node_Type
FROM BST
ORDER BY N

--Advanced Select: New Companies 
SELECT C.company_code, C.founder, E.LM, E.SM, E.MM, E.EM
FROM
    (SELECT company_code, founder
    FROM Company) AS C
    LEFT JOIN
    (SELECT company_code, 
        COUNT(DISTINCT lead_manager_code) AS LM, 
        COUNT(DISTINCT senior_manager_code) AS SM,
        COUNT(DISTINCT manager_code) AS MM,
        COUNT(DISTINCT employee_code) AS EM
    FROM Employee
    GROUP BY company_code) AS E
    ON C.company_code = E.company_code
ORDER BY C.company_code

--Alternative Queries: Print Prime Numbers
--SO Solution
drop temporary table if exists n;
create temporary table if not exists n engine=memory
    select t2.c*100 + t1.c*10 + t0.c + 1 as seq from 
    (select 0 c union all select 1 c union all select 2 c union all select 3 c union all select 4 c union all select 5 c union all select 6 c union all select 7 c union all select 8 c union all select 9 c) t0,
    (select 0 c union all select 1 c union all select 2 c union all select 3 c union all select 4 c union all select 5 c union all select 6 c union all select 7 c union all select 8 c union all select 9 c) t1,
    (select 0 c union all select 1 c union all select 2 c union all select 3 c union all select 4 c union all select 5 c union all select 6 c union all select 7 c union all select 8 c union all select 9 c) t2
    having seq > 2 and seq % 2 != 0; --Creates a table from 1-1000, removing 1 and all even digits

drop temporary table if exists q;
create temporary table if not exists q engine=memory
    select *
    from n
    where seq <= 32; --32 is the smallest number that can be squared to > 1000
alter table q add primary key seq (seq);

select 2 as p union all
select n.seq
from n
where not exists (
    select 1
    from q
    where q.seq < n.seq
      and n.seq mod q.seq = 0
);

select 2 as p union all
select n.seq
from n
left join q
    on  q.seq < n.seq
    and n.seq mod q.seq = 0
where q.seq is null;

--AI Solution, Failed
SELECT GROUP_CONCAT(prime_number SEPARATOR '&')
FROM (
  SELECT DISTINCT a.num AS prime_number
  FROM (
    SELECT a.num, COUNT(b.num) AS factors
    FROM (
      SELECT num
      FROM (
        SELECT (a+b*10+c*100) AS num
        FROM (
          SELECT 0 AS a UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9
        ) AS a
        JOIN (
          SELECT 0 AS b UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9
        ) AS b
        JOIN (
          SELECT 0 AS c UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9
        ) AS c
      ) AS nums
      WHERE num BETWEEN 2 AND 1000
    ) AS nums
    LEFT JOIN (
      SELECT a.num AS num, b.num AS factor
      FROM (
        SELECT num
        FROM (
          SELECT (a+b*10+c*100) AS num
          FROM (
            SELECT 0 AS a UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9
          ) AS a
          JOIN (
            SELECT 0 AS b UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9
          ) AS b
          JOIN (
            SELECT 0 AS c UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9
          ) AS c
        ) AS nums
        WHERE num BETWEEN 2 AND 1000
      ) AS a
      JOIN (
        SELECT num
        FROM (
          SELECT (a+b*10+c*100) AS num
          FROM (
            SELECT 0 AS a UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9
          ) AS a
          JOIN (
            SELECT 0 AS b UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9
          ) AS b
          JOIN (
            SELECT 0 AS c UNION SELECT 1 UNION SELECT 2 UNION SELECT 3 UNION SELECT 4 UNION SELECT 5 UNION SELECT 6 UNION SELECT 7 UNION SELECT 8 UNION SELECT 9
          ) AS c
        ) AS nums
        WHERE num BETWEEN 2 AND 31
      ) AS b
      ON a.num % b.num = 0
    ) AS factors
    ON nums.num = factors.num
    WHERE factors IS NULL
    ORDER BY nums.num ASC
  ) AS a
) AS primes

--Aggregation - Weather Observation Station 20
  --ynyeh0221 solution
  Select round(S.LAT_N,4) 
  from station AS S 
  where (select count(Lat_N) 
        from station 
        where Lat_N < S.LAT_N ) = (select count(Lat_N) 
                                  from station 
                                  where Lat_N > S.LAT_N);

  --Codingbroz solution
  SET @r = 0;
  SELECT ROUND(AVG(Lat_N), 4)
  FROM (SELECT (@r := @r + 1) AS r, Lat_N FROM Station ORDER BY Lat_N) Temp
  WHERE
      r = (SELECT CEIL(COUNT(*) / 2) FROM Station) OR
      r = (SELECT FLOOR((COUNT(*) / 2) + 1) FROM Station)