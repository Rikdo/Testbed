--LeetCode SQL Schema
--595. Big Countries
select name, population, area
from world
where area >= 3000000
or population >= 25000000
--1757. Recyclable and Low Fat Products
select product_id from products
where low_fats = 'Y' and recyclable = 'Y'
--584. Find Customer Referee
select name from customer
where referee_id <> 2 or referee_id is null
--183. Customers Who Never Order
select name as Customers from customers
where not id in (select customerid from orders)
--1873. Calculate Special Bonus
select employee_id, if(mod(employee_id,2) != 0 and not name like "M%", salary, 0) as bonus 
from employees
order by employee_id
--627. Swap Salary

--196. Delete Duplicate Emails