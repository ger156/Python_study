# 문제 : a와 b가 가지고 있는 값을 서로 뒤바꿔주세요.
# 조건 : 아래와 같이 출력 되도록 해주세요.

# 문제시작
a = 5
b = 10

# 구현시작
temp = a #임시 변수
a = b
b = temp
# 구현끝

print("a : {}".format(a))
# 출력 => a : 10

print("b : {}".format(b))
# 출력 => b : 5

# 문제끝