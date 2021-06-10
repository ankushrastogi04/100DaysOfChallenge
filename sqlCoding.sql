/*Table: Activity

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| machine_id     | int     |
| process_id     | int     |
| activity_type  | enum    |
| timestamp      | float   |
+----------------+---------+
The table shows the user activities for a factory website.
(machine_id, process_id, activity_type) is the primary key of this table.
machine_id is the ID of a machine.
process_id is the ID of a process running on the machine with ID machine_id.
activity_type is an ENUM of type ('start', 'end').
timestamp is a float representing the current time in seconds.
'start' means the machine starts the process at the given timestamp and 'end' means the machine ends the process at the given timestamp.
The 'start' timestamp will always be before the 'end' timestamp for every (machine_id, process_id) pair.
 

There is a factory website that has several machines each running the same number of processes. Write an SQL query to find the average time each machine takes to complete a process.

The time to complete a process is the 'end' timestamp minus the 'start' timestamp. The average time is calculated by the total time to complete every process on the machine divided by the number of processes that were run.

The resulting table should have the machine_id along with the average time as processing_time, which should be rounded to 3 decimal places.

The query result format is in the following example:

 

Activity table:
+------------+------------+---------------+-----------+
| machine_id | process_id | activity_type | timestamp |
+------------+------------+---------------+-----------+
| 0          | 0          | start         | 0.712     |
| 0          | 0          | end           | 1.520     |
| 0          | 1          | start         | 3.140     |
| 0          | 1          | end           | 4.120     |
| 1          | 0          | start         | 0.550     |
| 1          | 0          | end           | 1.550     |
| 1          | 1          | start         | 0.430     |
| 1          | 1          | end           | 1.420     |
| 2          | 0          | start         | 4.100     |
| 2          | 0          | end           | 4.512     |
| 2          | 1          | start         | 2.500     |
| 2          | 1          | end           | 5.000     |
+------------+------------+---------------+-----------+

Result table:
+------------+-----------------+
| machine_id | processing_time |
+------------+-----------------+
| 0          | 0.894           |
| 1          | 0.995           |
| 2          | 1.456           |
+------------+-----------------+

There are 3 machines running 2 processes each.
Machine 0's average time is ((1.520 - 0.712) + (4.120 - 3.140)) / 2 = 0.894
Machine 1's average time is ((1.550 - 0.550) + (1.420 - 0.430)) / 2 = 0.995
Machine 2's average time is ((4.512 - 4.100) + (5.000 - 2.500)) / 2 = 1.456


*/

/* Write your T-SQL query statement below */

with cte as (
select *,LAG(timestamp,1) OVER (partition by machine_id,process_id
		ORDER BY activity_type
	) next_month_sales from Activity
    
    )
    select machine_id,round(sum(next_month_sales-timestamp)/count(*),3) as processing_time from cte 
     where next_month_sales is not null
    group by machine_id




/*
Table: Customers

+---------------------+---------+
| Column Name         | Type    |
+---------------------+---------+
| customer_id         | int     |
| customer_name       | varchar |
+---------------------+---------+
customer_id is the primary key for this table.
customer_name is the name of the customer.
 

Table: Orders

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| order_id      | int     |
| customer_id   | int     |
| product_name  | varchar |
+---------------+---------+
order_id is the primary key for this table.
customer_id is the id of the customer who bought the product "product_name".
 

Write an SQL query to report the customer_id and customer_name of customers who bought products "A", "B" but did not buy the product "C" since we want to recommend them buy this product.

Return the result table ordered by customer_id.

The query result format is in the following example.

 

Customers table:
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 1           | Daniel        |
| 2           | Diana         |
| 3           | Elizabeth     |
| 4           | Jhon          |
+-------------+---------------+

Orders table:
+------------+--------------+---------------+
| order_id   | customer_id  | product_name  |
+------------+--------------+---------------+
| 10         |     1        |     A         |
| 20         |     1        |     B         |
| 30         |     1        |     D         |
| 40         |     1        |     C         |
| 50         |     2        |     A         |
| 60         |     3        |     A         |
| 70         |     3        |     B         |
| 80         |     3        |     D         |
| 90         |     4        |     C         |
+------------+--------------+---------------+

Result table:
+-------------+---------------+
| customer_id | customer_name |
+-------------+---------------+
| 3           | Elizabeth     |
+-------------+---------------+
Only the customer_id with id 3 bought the product A and B but not the product C.
*/

/* Write your T-SQL query statement below */


select * from Customers where customer_id in 
(
select customer_id from Orders where product_name='A')  

and customer_id in 
(select customer_id from Orders where product_name ='B')

and customer_id not in 
(select customer_id from Orders where product_name ='C')


/*
Write an SQL query to find the number of unique orders and the number of unique customers with invoices > $20 for each different month.

Return the result table sorted in any order.

The query result format is in the following example:

Orders
+----------+------------+-------------+------------+
| order_id | order_date | customer_id | invoice    |
+----------+------------+-------------+------------+
| 1        | 2020-09-15 | 1           | 30         |
| 2        | 2020-09-17 | 2           | 90         |
| 3        | 2020-10-06 | 3           | 20         |
| 4        | 2020-10-20 | 3           | 21         |
| 5        | 2020-11-10 | 1           | 10         |
| 6        | 2020-11-21 | 2           | 15         |
| 7        | 2020-12-01 | 4           | 55         |
| 8        | 2020-12-03 | 4           | 77         |
| 9        | 2021-01-07 | 3           | 31         |
| 10       | 2021-01-15 | 2           | 20         |
+----------+------------+-------------+------------+

Result table:
+---------+-------------+----------------+
| month   | order_count | customer_count |
+---------+-------------+----------------+
| 2020-09 | 2           | 2              |
| 2020-10 | 1           | 1              |
| 2020-12 | 2           | 1              |
| 2021-01 | 1           | 1              |
+---------+-------------+----------------+
In September 2020 we have two orders from 2 different customers with invoices > $20.
In October 2020 we have two orders from 1 customer, and only one of the two orders has invoice > $20.
In November 2020 we have two orders from 2 different customers but invoices < $20, so we don't include that month.
In December 2020 we have two orders from 1 customer both with invoices > $20.
In January 2021 we have two orders from 2 different customers, but only one of them with invoice > $20.
*/


/* Write your T-SQL query statement below */


select count(distinct customer_id) as customer_count, count(distinct order_id) as order_count,left(order_date,7) as month 
from Orders
where invoice>20
group by left(order_date,7)











