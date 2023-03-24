# 문제 : 매개변수의 개수를 맞춰주세요.
# 조건 : 함수호출 시 사용한 인자에 따라 함수를 적절하게 잘 만들어 주세요.
# 조건 : 오류가 나지 않으면 성공입니다.

def hello(num):
  if num == 1:
    print("안녕하세요")
  elif num ==2:
    print("하이")
  else:
    print("봉쥬르")

hello(1)
hello(2)
hello(3)

def hello_v2(num, cnt):
  i = 1
  if num == 1:
    while i <= cnt:
      print("안녕하세요")
      i += 1
  elif num == 2:
    while i <= cnt:
      print("하이")
      i += 1
  else:
    while i <= cnt:
      print("봉쥬르")
      i += 1
      
hello_v2(3, 3)
hello_v2(2, 4)
hello_v2(1, 5)