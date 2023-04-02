# 문제 - 사용자에게 숫자 3개를 입력받아서, 더한 결과를 출력해주세요
# map, strip를 사용해주세요.
print("문장을 입력 해주세요: ", end = '') # end = 줄바꿈을 하지 않겠다 라는 뜻
a, b, c = map(int, input().strip().split(' '))
print("a: {}".format(a))
print("b: {}".format(b))
print("c: {}".format(c))

print("a + b + c = {}".format(a + b + c))

d = list(map(int, input().strip().split(' ')))
print(d[0] + d[1] + d[2])

# 복습하기