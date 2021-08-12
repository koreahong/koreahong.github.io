---
layout: post
title: '(SQL)update 구문'
#subtitle: ''
categories: sql
tags: theory
comments: True
---

> update 구문 작성하기


-------------------------------------------------------------------------------

#기본포맷

```sql
UPDATE table명
SET 필드이름1 = 데이터값1 ....
where 필드이름 = 데이터값
```


- mysql workbench에서 안전모드를 풀어줘야 업데이트를 할 수 있다
```sql
set sql_safe_updates=0;
```

#활용
```sql
SELECT * FROM EMP_ATTEND;
```
<img width="126" alt="함수적용후셀렉" src="https://user-images.githubusercontent.com/51938331/123659741-f8139580-d86d-11eb-896a-71b863578c8d.png">

```sql
UPDATE emp_attend
SET attend_ymd = 20210629
where attend_ymd = 20210628
```

```sql
SELECT * FROM EMP_ATTEND;
```
<img width="128" alt="업데이트적용후셀렉" src="https://user-images.githubusercontent.com/51938331/123740360-4adb6480-d8e3-11eb-8bfe-bb7551b703dc.png">