# 문제 - 사용자에게 문장 1개를 입력받아서, 출력해주세요
print("문장을 입력 해주세요: ", end = '') # end = 줄바꿈을 하지 않겠다 라는 뜻
line = input()
print(line)

# 문제 - 사용자에게 문장 1개를 입력받아서, ','를 기준으로 나눠주세요

print("문장을 입력 해주세요: ", end = '')
line = input().split(',')
l = line.split(',')
print(l)

l = []
l.append(1)
l.append(2)
l.append(3)

l = '1,2,3'.split(',')
print(l)