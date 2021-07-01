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

