---
layout: post
title: 'leetcode curated SQL 70'
subtitle: '리트코드'
categories: sql
tags: practice
comments: True
---

> 리트코드 sql 문제풀이


-------------------------------------------------------------------------------

> 기간 : 21.06.30 - ing 

# 511. Game Play Analysis I
## basic

- 내풀이
```sql
select player_id, min(event_date) as first_login
from   activity
group  by player_id

```
# 512. Game Play Analysis II
## basic

- 내풀이

```sql
select player_id, device_id
from   activity
where  (player_id, event_date) in (select player_id, 
                                          min(event_date)
                                   from   activity
                                   group  by player_id)
```

# 534. Game Play Analysis III
## basic / 날짜별 누적합 구하기

- 내풀이

```sql
select a1.player_id, 
       a1.event_date, 
       sum(a2.games_played) as games_played_so_far
from   activity as a1
       inner join activity as a2
               on a1.event_date >= a2.event_date
                  and a1.player_id = a2.player_id
group  by  a1.player_id, a1.event_date
```
- [리트코드게시판에 설명등록](https://leetcode.com/problems/total-sales-amount-by-year/discuss/1306968/MySQL-solution)


# 534. Game Play Analysis IV
## datetime / 연속된 날짜 조인

- solution

```sql
SELECT Round(Count(t2.player_id) / Count(t1.player_id), 2) AS fraction
FROM   (SELECT player_id,
               Min(event_date) AS first_login
        FROM   activity
        GROUP  BY player_id) t1
       LEFT JOIN activity t2
              ON t1.player_id = t2.player_id
                 AND t1.first_login = t2.event_date - 1 
```

- 문제가 첫로그인한 날짜에 이어 연속적으로 로그인한 유저를 구하는 문제임
    1. 유저별 첫 로그인한 날짜를 구한다
    2. 첫로그인한 날짜와 나머지 날짜 - 1 조건으로 left join한다
    3. 왼쪽테이블은 전체유저가 있고 오른쪽 테이블은 연속적으로 로그인한 유저만 있음(나머지는 null) -> count를 하면 끝

# 570. Managers with at Least 5 Direct Reports
## basic / 서브쿼리생성   

- 내풀이

```sql 
select name
from   employee
where  id in (select managerid    
             from   employee    
             group  by managerid    
             having count(managerid) >= 5)    
``` 
    
# 570. Managers with at Least 5 Direct Reports    
## basic / 서브쿼리생성       
    
- 내풀이    
    
```sql     
select name    
from   employee    
where  id in (select managerid        
             from   employee        
             group  by managerid        
             having count(managerid) >= 5)        
```     
    
# 571. Find Median Given Frequency of Numbers
## basic / 중앙값 구하기     
    
- solution 1   
    
```sql     
select  avg(n.Number) median
from Numbers n
where n.Frequency >= abs((select sum(Frequency) from Numbers where Number<=n.Number) -
                         (select sum(Frequency) from Numbers where Number>=n.Number))
```     

- 왼쪽 , 오른쪽 개수를 따져서 푸는 문제인데 로직은 더 고민해봐야 할거 같다...


- solution 2
```sql   
with a as (    
    select number,    
           sum(frequency) over (order by number) - frequency as lower_num,    
           sum(frequency) over (order by number) as upper_num,    
           sum(frequency) over () / 2 as medium_num    
    from   numbers     
)    
    
select avg(number) as median    
from   a    
where  medium_num between lower_num and upper_num    
        
```   

- 그나마 직관적인 풀이 방법이다. 해당컬럼 이전까지 누적개수, 해당컬럼을 포함한 누적개수, 중앙값을 산출하는 방법


# 534. Game Play Analysis
## basic / 조인

- 내풀이 
``` sql    
select d.dept_name,   
    ifnull(student_number, 0) as student_number   

from   (select s.dept_id,   
           count(s.student_id) as student_number   
    from   student s   
           inner join department d   
                   on s.dept_id = d.dept_id   
           group  by s.dept_id) tbl_cal   
    right join department d   
            on tbl_cal.dept_id = d.dept_id   
order  by student_number desc, d.dept_name   
```     
    
- solution

```sql
SELECT
      dept_name, COUNT(student_id) AS student_number    
FROM    
      department    
      LEFT OUTER JOIN student 
                   ON department.dept_id = student.dept_id    
GROUP BY department.dept_name    
ORDER BY student_number DESC , department.dept_name    
```   
- 확실히 간결하다.
- left join, group by로 바로 계산가능한 문제
- count(컬럼명)하면 널입경우 0으로 표시되는 됨   
    
    
# 586. Customer Placing the Largest Number of Orders 
## basic / limit 활용 

- 내풀이
```sql    
select customer_number    
from   orders    
group  by customer_number    
having customer_number = (select customer_number    
                          from   (select customer_number, count(order_number) as cnt    
                                  from   orders    
                                  group  by customer_number    
                                  order  by cnt desc limit 1    
                                 ) tbl    
                         )    
```                                     

- solution 
```sql    
SELECT 
      customer_number    
FROM    
      orders    
GROUP BY customer_number    
ORDER BY COUNT(*) DESC    
LIMIT 1    
```
- 이렇게 간단한 것을.... 섭섭쿼리를 사용했네 ㅠㅠ 
- group by -> order by이므로 group by가 적용된 것을 굳이 select문이 아니라 order by에도 사용할 수 있다.


# 586. Customer Placi 
## basic / 연속적인 숫자 조인     

- solution
```sql
select distinct c1.seat_id  
from   cinema c1    
       inner join cinema c2    
               on abs(c1.seat_id -c2.seat_id) = 1    
                  and c1.free = 1    
                  and c2.free = 1   
```
- 조인시 조인옵션에 사칙연산 가능


# 607. Sales Person
## basic / 조인

- 내풀이

```sql
select name
from   salesperson
where  sales_id not in (select o.sales_id
                        from   orders o
                               inner join company c
                                       on o.com_id = c.com_id
                        where  c.name = 'RED')  
```
- 모든 부분을 조인할 필요없이 일부만 조인하고, 조인한 결과를 사용하는 형식으로 가능

# 608. Tree Node
## basic / case

- 내풀이
```sql
select  id,
        case
            when p_id is null then 'Root'
            when id in (select p_id from tree) then 'Inner'
            else 'Leaf'
        end as Type
from    tree
```
- [Discuss 등재](https://leetcode.com/problems/tree-node/discuss/1308642/simple-MySQL-with-case-function)

# 613. Shortest Distance in a Line
## basic / 조인

- 내풀이 
```sql
select min(abs(p1.x - p2.x)) as shortest
from   point p1, point p2
where  p1.x != p2.x
```

- [Discuss 등재](https://leetcode.com/problems/shortest-distance-in-a-line/discuss/1308656/Simple-MySQL-solution-with-join)


# 615. Average Salary: Departments VS Company
## basic / 조인

- 내풀이
```sql
SELECT mon_sal.pay_month,
       department_id,
       CASE
         WHEN avg_sal > dep_sal THEN 'lower'
         WHEN avg_sal < dep_sal THEN 'higher'
         ELSE 'same'
       END AS comparison
FROM   (SELECT Date_format(pay_date, '%Y-%m') AS pay_month,
               Avg(amount)                    AS avg_sal
        FROM   salary
        GROUP  BY Date_format(pay_date, '%Y-%m')) mon_sal
       INNER JOIN (SELECT Avg(s.amount)                  AS dep_sal,
                          department_id,
                          Date_format(pay_date, '%Y-%m') AS pay_month
                   FROM   salary s
                          INNER JOIN employee e
                                  ON s.employee_id = e.employee_id
                   GROUP  BY Date_format(pay_date, '%Y-%m'),
                             department_id) dep_sal
               ON mon_sal.pay_month = dep_sal.pay_month 
```


# 1045. Customers Who Bought All Products
## basic / 서브쿼리

- 내풀이 

1. 고객, 상품별 중복제거 -> 종류별로 한번씩 샀는지 카운트하기 위함
2. 상품테이블 상품개수 스칼라뷰 계산
3. 상품으로 조인 후 개수 파악하고 출력

```sql
select  customer_id
from    (select customer_id,
                product_key
         from   customer 
         group  by customer_id, product_key
        ) new_c
group   by customer_id
having  count(customer_id) = (select count(distinct(product_key))
                              from   product)      
```
- [Discuss 등재](https://leetcode.com/problems/customers-who-bought-all-products/discuss/1308723/super-simple-MySQL-solution)


# 1050. Actors and Directors Who Cooperated At Least Three Times
## super basic

- 내풀이

1. group by -> having 으로 해당 조건 찾기
```sql
select actor_id, 
       director_id
from   actordirector
group  by actor_id, director_id
having count(timestamp) >= 3
```

# 1068. Product Sales Analysis I
## super basic

- 내풀이

1. 조인 후 해당 조건 찾기
```sql
select p.product_name, 
       s.year,
       s.price
from   sales s
       inner join product p
               on s.product_id = p.product_id
```

# 1075. Project Employees I
## super basic

- 내풀이

1. 조인 후 해당 조건 찾기

```sql
select p.project_id,
       round(avg(e.experience_years),2) as average_years
from   project p
       inner join employee e
               on p.employee_id = e.employee_id
group  by p.project_id
```


# 1076. Project Employees II
## super basic

- 내풀이
1. 서브쿼리로 최대값 찾기
2. 최대값 적용
```sql
select  project_id
from    project
group   by project_id
having  count(employee_id) = (select count(p.project_id) as cnt
                              from   project p
                                     inner join employee e
                                             on p.employee_id = e.employee_id
                              group  by p.project_id 
                              order  by cnt desc limit 1
                             )  

```



#1077. Project Employees III
## basic / 윈도우 함수로 순위 구하기

- 내풀이
1. 윈도우 함수로 순위매기기
2. 순위가 1인 것만 출력하기

```sql
select   project_id,
         employee_id
         
from    (select  p.project_id,
         p.employee_id,
         (rank()
                over(
                    partition by p.project_id order by experience_years desc)) rk
         from    project p 
                 inner join employee e
                         on p.employee_id = e.employee_id
        ) rk_tbl
where   rk = 1
```

# 1082. Sales Analysis I
## super basic

- 내풀이

1. 최댓값 구하기
2. 최대값에 해당하는 셀러 춫력하기
```sql
select  seller_id
from    sales
group   by seller_id
having  sum(price) = (  select  sum(price) as sum_price
                        from    sales
                        group   by seller_id
                        order   by sum_price desc limit 1)
```
  
# `1083. Sales Analysis II`
## super basic 
  
- 내풀이

1. iphone 산사람 추출
2. s8 산사람 추출
3. 없는 사람 고르기  

```sql
select  distinct s.buyer_id
from    product p
        inner join sales s
                on p.product_id = s.product_id
where   buyer_id not in (   select  buyer_id
                            from    product p
                                    inner join sales s
                                            on p.product_id = s.product_id
                            where   p.product_name = 'iphone')
        and p.product_name = 'S8'    
```  

- solution 
```sql
SELECT  b.buyer_id
FROM    Product AS a
        INNER JOIN Sales AS b
                ON a.product_id = b.product_id 
GROUP   BY b.buyer_id 
HAVING  SUM(a.product_name = 'S8') > 0 
        and SUM(a.product_name = 'iPhone') = 0;
```
- `order by와 마찬가지로 having 절에서도 조건을 쓸 수 있다.`

# `1084. Sales Analysis III`
## basic / having절로 조건걸기

- 내풀이

```sql
# having 절로 조건 걸기

select  p.product_id,
        p.product_name
from    product p
        inner join sales s
                on p.product_id = s.product_id
group   by p.product_id
having  sum(s.sale_date between '2019-01-01' and '2019-03-31') > 0
        and sum(s.sale_date < '2019-01-01' or sale_date > '2019-03-31' ) = 0
```

# 1097. Game Play Analysis V
## basic / 조인

- 내풀이

1. 필요피쳐 : 처음 다운로드 받은 날짜와 인원수, 다음날 바로 돌아온 비율

1. 처음 다운로드 받은 날짜
2. 날짜 / 날짜 - 1 조인

```sql
select  install_dt ,
        count(ins_day.player_id) as installs,
        round(count(a.player_id) / count(ins_day.player_id),2) as Day1_retention
        # 처음 다운로드 받은 날짜
from    (select  player_id,
                 min(event_date) as install_dt
         from    activity
         group   by player_id
        ) ins_day
         # 다음날 조인(조건 플래이어 아이디, 날짜 = 날짜-1)
         left join activity a
               on datediff(event_date, ins_day.install_dt) = 1
                  and ins_day.player_id = a.player_id
group   by install_dt   
```
- [Discuss 등재](https://leetcode.com/problems/game-play-analysis-v/discuss/1308891/super-simple-MySQL-solution)


# 1098. Unpopular Books
## basic / 조인

- 내풀이
1. 필요피쳐 : 개별 sold 개수(quantity 개수), 1년-기간 (한달전은 이내는 안됨),

```sql

select  b.book_id,
        b.name
from    orders o
        right join books b
                on o.book_id = b.book_id
                   # 1년기간 산출
                   and o.dispatch_date between '2018-06-23' and '2019-06-23'
where   b.book_id NOT in (  select  book_id
                            from    books
                            where   available_from >= '2019-05-23')

group   by b.book_id
        # 개별 sold 개수
having  ifnull(sum(quantity),0) < 10
```


- solution
```sql
select  b.book_id, b.name
from    books b 
        left join orders o
               on b.book_id = o.book_id 
                  and dispatch_date between '2018-06-23' and '2019-06-23'
where   available_from < '2019-05-23'
group   by b.book_id, b.name
having  ifnull(sum(quantity),0) <10;
```





































































































































































