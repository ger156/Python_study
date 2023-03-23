# 반복문

i = 1   # 시작값
while i <= 10:    # 조건부
  print(i)
  i += 1   # 보폭(?) - 주고싶은값(1)을 주면 값이 달라짐

print("i :", i)

i = 10
while i >= 1:
  print(i)
  i -= 1
  
i = 1
while i <= 10:
  print(i)
  # 여기에 증감식을 쓰지않을경우 무한루프가 걸리기 때문에 무조건 증감식을 써주기.
# 조건식이 거짓일 경우 멈춘다.
  
# 증감연산자
# a = 1
# print(a)
# a = a + 1
# print(a)
# a += 1      # += 1 씩 증가시킨다는 의미, 반대로 감소시키고 싶을 경우 -= 쓰면됨.
# print(a)