--Basic Selection
----------------------------------------------------
--Japanese Cities' Attributes
select * from city
where countrycode = "JPN"
--Weather Observation Station 6
select distinct city from station
where city regexp "^a|^e|^i|^o|^u"
--Weather Observation Station 7
select distinct city from station
where city regexp "a$|e$|i$|o$|u$"
--Weather Observation Station 8
select distinct city from station
where city regexp "^a|^e|^i|^o|^u"
and city regexp "a$|e$|i$|o$|u$"
--Weather Observation Station 9
select distinct city from station
where city not regexp "^a|^e|^i|^o|^u"
--Weather Observation Station 10
select distinct city from station
where city not regexp "a$|e$|i$|o$|u$"
--Weather Observation Station 11
select distinct city from station
where city not regexp "^a|^e|^i|^o|^u"
or city not regexp "a$|e$|i$|o$|u$"
--Weather Observation Station 12
select distinct city from station
where city not regexp "^a|^e|^i|^o|^u"
and city not regexp "a$|e$|i$|o$|u$"
--Higher Than 75 Marks
select name from students
where marks > 75
order by RIGHT(name, 3), id asc
--Employee Names
select name from employee
order by name asc
--Employee Salaries
select name from employee
where salary > 2000 and months < 10
order by employee_id asc


--Aggregation
----------------------------------------------------
--The Blunder
select ceiling(avg(salary)-avg(REGEXP_REPLACE(salary,"[0]","")))
from employees
--Top Earners
select (salary*months) as TE ,count(*)
from employee
group by TE
order by TE desc
limit 1
--Weather Observation Station 2
select round(sum(lat_n),2), round(sum(long_w),2)
from station
--Weather Observation Station 13
select truncate(sum(lat_n), 4)
from (select lat_n 
    from station
    where lat_n between 38.7880 and 137.2345) as rng
--Weather Observation Station 14
select truncate(max(lat_n), 4)
from (select lat_n from station where lat_n < 137.2345) as rng
--Weather Observation Station 15
select round(long_w,4) from station
where lat_n = (select max(lat_n) from station where lat_n < 137.2345)
--Weather Observation Station 16
select round(min(lat_n),4) from station
where lat_n > 38.7780
--Weather Observation Station 17
select round(long_w, 4)
from station
where lat_n > 38.7780
order by lat_n asc
limit 1
--Weather Observation Station 18
select round(((maxlat-minlat)+(maxlong-minlong)),4)
from (select 
      max(lat_n) as maxlat,
      min(lat_n) as minlat,
      max(long_w) as maxlong,
      min(long_w) as minlong
      from station) as minmax
--Weather Observation Station 18 (Alternate Solution, single select
select round(((max(lat_n)-min(lat_n))+(max(long_w)-min(long_w))),4) from station
--Weather Observation Station 19
select round(sqrt(
    pow(max(lat_n)-min(lat_n),2) +
    pow(max(long_w)-min(long_w),2) ),4)
from station

--Triangles
SELECT 
    CASE
        WHEN A + B <= C OR A + C <= B OR B + C <= A
            THEN 'Not A Triangle'
        WHEN A = B AND A = C 
            THEN 'Equilateral'
        WHEN (A = B AND B != C) OR (A != B AND B = C)
            THEN 'Isosceles'
        WHEN A != B AND A != C AND B != C
            THEN 'Scalene'
    END AS 'Output'
FROM TRIANGLES;