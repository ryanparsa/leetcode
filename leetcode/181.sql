drop table if exists Employee;
Create table If Not Exists Employee
(
    id        int,
    name      varchar(255),
    salary    int,
    managerId int
);
insert into Employee (id, name, salary, managerId)
values ('1', 'Joe', '70000', '3');
insert into Employee (id, name, salary, managerId)
values ('2', 'Henry', '80000', '4');
insert into Employee (id, name, salary, managerId)
values ('3', 'Sam', '60000', NULL);
insert into Employee (id, name, salary, managerId)
values ('4', 'Max', '90000', NULL);


-- Write a solution to find the employees who earn more than their managers.
select a.name as Employee
from Employee as a
         left join Employee as b on a.managerId = b.id
where a.salary > b.salary;
