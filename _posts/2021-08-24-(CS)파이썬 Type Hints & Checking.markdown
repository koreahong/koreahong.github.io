---
layout: post
title: '파이썬 Type 힌트와 체킹'
subtitle: '(CS)구조화된 코드는 어떤 거인가'
categories: Computer_Science
tags : software
comments: False
---

> 파이썬 타입힌트와 확인에 대한 이해
> 해당내용은 인프런 파이썬 객체프로그래밍 출처입니다

# 목적
- 타입힌트와 체킹을 하는 이유와 방법 파악하기

# 내용

## 타입힌트 

정의 : 말 그대로 파이썬 코드를 작성할 때 타입에 대한 메타 정보를 제공하는 것

### 힌트
1. What?
    - 타입 힌트
2. How?
    - 변수: 타입 = 값
    - isinstance(객체, 타입)
    - 함수를 정의해서 타입을 확인
    - mypy 라이브러리 활용 [mypy 공문](https://mypy.readthedocs.io/en/stable/getting_started.html)
    - pyright 라이브러리 활용 [pyright 공문](https://github.com/microsoft/pyright)
    - unitest를 사용해서 기능별로 쪼개서 pyright, mypy를 사용하면 더욱 수월함 
3. Why?
    - 협업을 하는 경우에 여러 개발자간에 타입에 대한 오류를 방지하여 생산성을 높임

```python 
  from typing import List, Tuple, Dict
  #code 생략
  def type_check(obj, typer) -> None:
      if isinstance(obj, typer):
          pass
      else:
          raise TypeError(f"Type Error : {typer}")
```

- mypy 명령어 : mypy 이름.py && python 이름.py

### Generic Type
1. What?
   - Generic Type
   - 하나의 값이 여러 다른 데이터 타입을 가질 수 있는 기술
2. How?
   - 받는 데이터에 따라서 타입변수를 다르게함. 인스턴스를 선언할때 타입변수와 같이 선언함
3. Why?
   - 데이터 형식에 의존하지 않기 위함.
   - 암호화를 시켜 정보를 맞추지 않게 하기 위함

```python 
#어떤 타입이 올 수 있는지 설정하기
ARM = TypeVar("ARM", int, float, str)
HEAD = TypeVar("HEAD", int, float, str)
class Robot(Generic[ARM]):
   def __init__(self, arm: ARM, head: HEAD)"
      self.arm = arm
      self.head = head
      
   def decode(self)"
      bbb: Optional[ARM] = None
      pass

#인스턴스를 선언할때 타입을 지정해서 보냄
robot1 = Robot[int, int](123456, 12355123)
robot2 = Robot[str, int]("12345523", 4341251234)
```