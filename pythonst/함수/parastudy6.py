# 함수 - 매개변수, 리턴
# 리턴 - 파이썬에서는 결과를 의미함

# def plus(a, b):
#   return 5

# x = plus(20, 30) + 5
# print(x)

def is_adult(age):
  if age >= 20:
    return True
  return False
  
print("20 is adult age : {}".format(is_adult(20)))
print("15 is adult age : {}".format(is_adult(15)))