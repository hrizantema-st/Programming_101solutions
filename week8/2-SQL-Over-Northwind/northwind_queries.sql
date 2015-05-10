#All queries are going to be some form of SELECT:

    #List all employees with their first name, last name and title.
SELECT FirstName, LastName, Title FROM employees

    #List all employees from Seattle.
select * from employees where City = 'Seattle'

    #List all employees from London.
select * from employees where City = 'London'

    #List all employees that work in the Sales department.
select * from employees where Title like "%Sales%"

    #List all females employees that work in the Sales department.
select * from employees where Title like "%Sales%"  and TitleOfCourtesy = 'Ms.' or TitleOfCourtesy = 'Mrs.'

    #List the 5 oldest employees.
select  *  from employees order by BirthDate asc limit 5;

    #List the first 5 hires of the company.
select  *  from employees order by HireDate asc limit 5;

    #List the employee who reports to no one (the boss)
select  *  from employees where ReportsTo is null;

    #List all employes by their first and last name, and the first and last name of the employees that they report to.
select a.FirstName, a.LastName, b.FirstName, b.LastName from  employees as a INNER JOIN employees as b on b.EmployeeID=a.ReportsTo;

    #Count all female employees.
select count(*) from employees where TitleOfCourtesy in ('Ms.', 'Mrs.') ;

    #Count all male employees.
select count(*) from employees where TitleOfCourtesy in ('Dr.', 'Mr.') ;

    #Count how many employees are there from the different cities. For example, there are 4 employees from London.
#select count(distinct  City) from employees;
select City, count(City) from employees group by City;

    #List all OrderIDs and the employees (by first and last name) that have created them.
select a.OrderID, b.FirstName, b.LastName from orders as a inner join employees as b on b.EmployeeID=a.EmployeeID;

    #List all OrderIDs and the shipper name that the order is going to be shipped via.
select a.OrderID, b.CompanyName from orders as a inner join shippers as b on a.ShipVia=b.ShipperID;

    #List all contries and the total number of orders that are going to be shipped there.
select ShipCountry as ship_country, count(ShipCountry) as number_of_orders  from orders group by ShipCountry;

    #Find the employee that has served the most orders.
select EmployeeID as employee_id , count(EmployeeID) as number_of_orders
from orders
group by EmployeeID
order by count(EmployeeID) desc limit 1;

    #Find the customer that has placed the most orders.
select CustomerID as customer_id , count(CustomerID) as number_of_orders
from orders
group by CustomerID
order by count(CustomerID) desc limit 1;

    #List all orders, with the employee serving them and the customer, that has placed them.
select a.OrderID as order_id, b.FirstName || " " || b.LastName as employee_name , c.ContactName as customer_contact_name
from orders as a
 JOIN employees as b ON a.EmployeeID=b.EmployeeID
 JOIN customers as c ON a.CustomerID=c.CustomerID;

    #List for which customer, which shipper is going to deliver the order.
select a.CustomerID as customer , c.CompanyName as shipping_company
from customers as a
join orders as b on b.CustomerID = a.CustomerID
join  shippers as c on b.ShipVia = c.ShipperID;
