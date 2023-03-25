# 문제 : 입력받은 정수의 모든 약수의 합을 리턴하는 함수를 구현해주세요.

def get_divisors_sum(num):
  s = 0
  i = 1
  
  while i <= num:
    if num % i == 0:
      s += i
      print(s)
    i += 1
  
  return s
  
s = get_divisors_sum(1000)

print("정수 1000의 약수의 합 : {}".format(s))

'''
변수
내장함수 : print, int, str, float, format...print() -> 내장함수

사용자 정의 함수 : def로 생성
요소
- 지역변수
- 매개변수 (데이터 투입구)
- 리턴 (데이터 배출구)
def fuc1(a,b): 매개변수 == 지역변수
  d = 10 일반지역변수
  return a+b
a = 10 -> 전역변수

조건문(if, elif, else)
반복문(while)
알고리즘문제풀어보기
'''