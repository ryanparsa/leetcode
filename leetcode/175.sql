drop table if exists Person;
drop table if exists Address;

Create table If Not Exists Person
(
    personId  int,
    firstName varchar(255),
    lastName  varchar(255)
);
Create table If Not Exists Address
(
    addressId int,
    personId  int,
    city      varchar(255),
    state     varchar(255)
);


insert into Person (personId, lastName, firstName)
values ('2', 'Alice', 'Bob');
insert into Person (personId, lastName, firstName)
values ('1', 'Wang', 'Allen');
insert into Address (addressId, personId, city, state)
values ('1', '2', 'New York City', 'New York');
insert into Address (addressId, personId, city, state)
values ('2', '3', 'Leetcode', 'California');



select person.firstName,
       person.lastname,
       address.city,
       address.state
from person
         left join address on person.personId = address.personId;
