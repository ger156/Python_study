# 문제 : 매개변수의 개수를 맞춰주세요.
# 조건 : 함수호출 시 사용한 인자에 따라 함수를 적절하게 잘 만들어 주세요.
# 조건 : 오류가 나지 않으면 성공입니다.

def a():
  print("a함수실행")

def b(a1, a2, a3):
  print("b함수실행")
  print("a1 :", a1)
  print("a1 :", a2)
  print("a1 :", a3)
  
def c(a1, a2, a3, a4):
  print("함수c실행")
  print("a1 :", a1)
  print("a2 :", a2)
  print("a3 :", a3)
  print("a4 :", a4)
  
a()
b(1, 2, 3)
c("안녕", 1 == 1, 550, 600)