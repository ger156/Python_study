# 연산자 : 사칙(산술)연산자, 비교연산자, 논리연산자

# 사직연산자 : +, -, *, /(나눈 몫), //(몫의 정수부분), %(나눈 나머지), **(제곱)

# print(10 + 10)
# print(20 - 10)
# print(10 * 10)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)

# 순서대로 나타내어 봤습니다.

# 비교연산자 : 결과 값 --> True(참), False(거짓)
#             >=, >, <=, <, ==, != 이렇게 있습니다.

# print(10 >= 10)
# print(10 > 10)
# print(10 <= 10)
# print(10 < 10)
# print(10 == 10)
# print(10 != 10)

# 논리연산자 : and, or
# and : 양쪽의 비교한 결과 값이 둘다 True인 경우 True이다.
#       - 양쪽의 비교한 결과 값 중 하나라도 False인 경우 False이다.
a = 20
b = 10
print(a > b and a != b) # 결과 값 True
print(a < b and a != b) # 결과 값 False

# or : 양쪽의 비교한 결과 값이 둘다 False인 경우 False이다.
#       - 양쪽의 비교한 결과 값 중 하나라도 True인 경우 True이다.
print(a < b or a == b) # 결과 값 False
print(a > b or a == b) # 결과 값 True