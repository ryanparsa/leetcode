drop table if exists Person;

Create table If Not Exists Person
(
    id    INT PRIMARY KEY AUTO_INCREMENT,
    email varchar(255)
);

insert into Person (email)
values ('a@b.com'),
       ('c@d.com'),
       ('a@b.com');

-- Write a solution to report all the duplicate emails.
-- Note that it's guaranteed that the email field is not NULL.

-- return email and count
select email, count(email) as count
from Person
group by email;

-- list of row with same email but different id
select p1.id, p1.email
from Person as p1
         join Person as p2 on p1.email = p2.email
where p1.id != p2.id;


-- the answer using group by
explain analyze
select email
from Person
group by email
having count(email) > 1;
# | -> Filter: (count(person.email) > 1)  (actual time=0.0485..0.0495 rows=1 loops=1)
#     -> Table scan on <temporary>  (actual time=0.0463..0.0469 rows=2 loops=1)
#         -> Aggregate using temporary table  (actual time=0.0453..0.0453 rows=2 loops=1)
#             -> Table scan on Person  (cost=0.55 rows=3) (actual time=0.0208..0.025 rows=3 loops=1)



-- answer with join
explain analyze
select distinct p1.email
from Person as p1
         join Person as p2 on p1.email = p2.email
where p1.id != p2.id;
# | -> Table scan on <temporary>  (cost=2.85..4.54 rows=3) (actual time=0.0565..0.0568 rows=1 loops=1)
#     -> Temporary table with deduplication  (cost=2..2 rows=3) (actual time=0.0555..0.0555 rows=1 loops=1)
#         -> Filter: ((p1.id <> p2.id) and (p2.email = p1.email))  (cost=1.7 rows=3) (actual time=0.039..0.043 rows=2 loops=1)
#             -> Inner hash join (<hash>(p2.email)=<hash>(p1.email))  (cost=1.7 rows=3) (actual time=0.0362..0.0392 rows=5 loops=1)
#                 -> Table scan on p2  (cost=0.118 rows=3) (actual time=0.00354..0.00495 rows=3 loops=1)
#                 -> Hash
#                     -> Table scan on p1  (cost=0.55 rows=3) (actual time=0.0149..0.0184 rows=3 loops=1)
