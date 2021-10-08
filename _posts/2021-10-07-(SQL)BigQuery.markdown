---
layout: post
title:  "(SQL)data analystic with BigQuery"
subtitle:   "빅쿼리공부"
categories: sql
tags: theory
comments: true
---
> 해당내용을 모든 출처는 '구글빅쿼리 완벽가이드'입니다

목차

1. Why BigQuery
2. BigQuery만의 특수 쿼리
3. Bigquery와 다른 프로그램 연동하기
   1. 스프레드시트 / tableau
   2. python(colab)

# Why BigQuery

1. 빅쿼리는 서버리스이다.
   - 이는 곧 모든 데이터를 자유롭게 사용가능하다는 것.
2. 애드혹 쿼리에 적합
   - 기존 OLTP는 쓰기와 읽기의 트레이드오프가 있었지만 OLAP인 빅쿼리는 읽기에 최적화된 애드혹 쿼리를 사용할 수 있음
   - [컬럼기반베이스](https://datalibrary.tistory.com/32) / OLAP에 적합한 스토리지
3. 분산 SQL엔진
   - 여러 SQL문을 병렬처리 가능
4. 예측 가능한 툴(강력한 데이터 분석)
   - 머신러닝으로 예측가능
5. 구글 클라우드 플랫폼 서비스와 통합하여 사용 가능   

# BigQuery만의 특수 쿼리

빅쿼리는 기존 쿼리에서 사용했던 기능(SQL 2011기준)을 그대로 유지하고 있다.  
추가로 다음과 같이, 배열과 관련된 기능들이 가능하다.   

> ARRAY_AGG  

- 상황: 특정그룹을 연도별로 추출하고 싶음  
- 주의사항: NULL값이 있다면 임시테이블로 저장할 수 없음  
```SQL
SELECT 
  gender
  , ARRAY_AGG(numtrips order by year) AS numtrips
FROM (
  SELECT
    gender
    , EXTRACT(YEAR FROM starttime) AS year
    , COUNT(1) AS numtrips
  FROM
    `bigquery-public-data`.new_york_citibike.citibike_trips
  WHERE gender != 'unknown' AND starttime IS NOT NULL
  GROUP BY gender, year
  HAVING year > 2016
)
GROUP BY gender
```
![](../assets/img/bigquery2_25.jpg)   

> STRUCT

- 상황: 배열 풀기  
```SQL
SELECT * FROM UNNEST(
  [
    STRUCT('male' AS gender, [9306602, 3955871] AS numtrips)
    , STRUCT('female' AS gender, [3236735, 1260893] AS numtrips)
  ]) 
```

참고, [변성윤님 깃헙블로그 / 빅쿼리 배열함수](https://zzsza.github.io/gcp/2020/04/12/bigquery-unnest-array-struct/)

# Bigquery와 다른 프로그램 연동하기
1. 빅쿼리와 스프레드시트 / tableau 연계
- 문제상황
  1. public 버전은 빅쿼리와 연결할 수 없음 -> 스프레드시트로 저장후 tableau에서 별도로 연결해야 함
  2. 스프레드시트 또한 OWOX로만 연결이 가능, Data Connector는 G Suite사용해야 사용 가능


- OWOX 설치 프로세스
   1. 새로운 스프레드시트 생성
   2. 부가기능 탭에서 부가기능 설치하기 클릭
   3. 검색 창에서 'OWOX' 검색 후 설치    

참고, [변성윤님 깃헙블로그 / 빅쿼리와 스프레드시트 연결](https://zzsza.github.io/gcp/2019/07/20/bigquery-with-spreadsheet/)

- 쿼리 작성 후 데이터 연계
  1. create 클릭 후 쿼리작성    


- tableau Public 연계  
  1. 구글 스프레드시트 연결 후 인증

  
2. 빅쿼리와 python 연계  
    1. Json 형식으로 key로 연결
    2. 이메일 인증
    
    1번 같은 경우 협업시에 key보관에 대한 이슈 발생 가능성이 농후함

- 조회하는 경우  
```python
from google.colab import auth
auth.authenticate_user()

%load_ext google.colab.data_table ### bigquery 형식으로 출력
%unload_ext google.colab.data_table ### 기존 df 형식으로 출력

### 쿼리 구문
%%bigquery --project yourprojectname
SELECT 
  gender
  , ARRAY_AGG(numtrips order by year) AS numtrips
FROM (
  SELECT
    gender
    , EXTRACT(YEAR FROM starttime) AS year
    , COUNT(1) AS numtrips
  FROM
    `bigquery-public-data`.new_york_citibike.citibike_trips
  WHERE gender != 'unknown' AND starttime IS NOT NULL
  GROUP BY gender, year
  HAVING year > 2016
)
GROUP BY gender
```

- 데이터를 메모리에 저장하는 경우  
```python
from google.cloud import bigquery
project_id = 'yourprojectname'
client = bigquery.Client(project=project_id)

df = client.query('''
SELECT 
  gender
  , ARRAY_AGG(numtrips order by year) AS numtrips
FROM (
  SELECT
    gender
    , EXTRACT(YEAR FROM starttime) AS year
    , COUNT(1) AS numtrips
  FROM
    `bigquery-public-data`.new_york_citibike.citibike_trips
  WHERE gender != 'unknown' AND starttime IS NOT NULL
  GROUP BY gender, year
  HAVING year > 2016
)
GROUP BY gender
''').to_dataframe()
```
참고1, [변성윤님 깃헙블로그 / 빅쿼리과 코랩 연동](https://zzsza.github.io/gcp/2019/03/17/pandas-gbq-auth/)  
참고2, [colab - bigquery guide](https://colab.research.google.com/notebooks/bigquery.ipynb#scrollTo=ONI1Xo0-KtAD)






        
        



