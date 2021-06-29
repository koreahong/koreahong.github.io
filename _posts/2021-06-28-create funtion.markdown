---
layout: post
title: '함수생성/create function'
subtitle: '함수 만들기'
categories: sql
tags: theory
comments: True
---

> mysql에서 함수만들기


-------------------------------------------------------------------------------

# 기본적인 포맷

```sql
CREATE FUNCTION 함수이름(파라미터명, 데이터타입) RETURNS 반환값
BEGIN
  RETURN (
      쿼리문
  );
END
```

[함수생성예시참조](https://shlee0882.tistory.com/242)
[함수생성시1418에러해결](https://dzzienki.tistory.com/34)

```sql
SET GLOBAL log_bin_trust_function_creators = 1;

DELIMITER $$
CREATE FUNCTION FNC_ATTEND(attendType VARCHAR(10), empNo VARCHAR(10)) RETURNS BOOL
 
BEGIN
     DECLARE exist_flag INT;
     DECLARE returnVal  BOOL;
         SET returnVal = FALSE;
 
     -- 출석 등록
     IF 'attend'= attendType THEN
         SELECT COUNT(1)
           INTO exist_flag
           FROM EMP_ATTEND
          WHERE EMP_NO = empNo 
            AND ATTEND_YMD = DATE_FORMAT(NOW(), '%Y%m%d')
         ;
         
         IF exist_flag = 0 THEN
             INSERT INTO EMP_ATTEND(
                      ATTEND_YMD
                    , EMP_NO
             )VALUES(
                   DATE_FORMAT(NOW(), '%Y%m%d')
                     , empNo 
             );
             SET returnVal = TRUE;
         END IF;
     END IF;
      RETURN returnVal;
END $$
```

- 함수생성후 반드시 refresh 버튼을 눌러줘야 함수가 적용된다

```sql
SELECT FNC_ATTEND('attend', '1000');
```
<img width="146" alt="함수적용리턴1" src="https://user-images.githubusercontent.com/51938331/123659685-eaf6a680-d86d-11eb-9585-fd3a655208ab.png">

```sql
SELECT * FROM EMP_ATTEND;
```

<img width="126" alt="함수적용후셀렉" src="https://user-images.githubusercontent.com/51938331/123659741-f8139580-d86d-11eb-896a-71b863578c8d.png">
