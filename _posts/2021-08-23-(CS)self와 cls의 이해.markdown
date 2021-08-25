---
layout: post
title: 'self와 cls의 이해'
subtitle: '(CS)구조화된 코드는 어떤 거인가'
categories: Computer_Science
tags : software
comments: False
---

> self와 cls의 이해
> 해당내용은 인프런 파이썬 객체프로그래밍 출처입니다

# 목적
- 인스턴스와 클래스의 개념을 파악.  

# 내용
- self는 instance 자체이다.  
- cls는 class 자체.  

```python  
class SelfTest:
    name = 'hong'
    
    def __init__(self, x):
        self.x = x
    
    @classmethod
    def func1(cls):
        print(f"cls: {cls}")
        print("func1")
    
    def func2(self):
        print(f"self: self}")
        print("class안의 Self 주소: ", id(self))
        print("fucn2")
  
test_obj = SElfTest(17)
test_obj.func2()
SelfTest.func1()
test_obj.func1()
print("인스턴스의 주소: ", id(test_obj)
```
- test_obj.func1()가 가능한 이유는 파이썬이 동적으로 인스턴스와 클래스 네임스페이스에 해당하는 것을 찾아 실행함.  
- 하지만, 반대로 클래스에서 인스턴스의 네임스페이스로는 갈 수 없음