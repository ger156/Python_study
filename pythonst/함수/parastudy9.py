# 문제 : 온도단위 섭씨를, 화씨로 바꿔주는, 함수 c_to_f 를 구현해주세요.
# 조건 : 공식 = 섭씨온도 * (9 / 5) + 32 => 화씨온도

def c_to_f(c):
  f = c * (9 / 5) + 32 # 구현
  return f

print(c_to_f(10))
print(c_to_f(20))
print(c_to_f(30))