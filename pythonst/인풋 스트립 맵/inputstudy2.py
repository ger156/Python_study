# 문제 - 사용자에게 숫자 2개를 입력받아서, 더한 결과를 출력해주세요
print("문장을 입력 해주세요: ", end = '') # end = 줄바꿈을 하지 않겠다 라는 뜻
line = input().strip().split(' ')
line[0] = int(line[0])
line[1] = int(line[1])
print(line[0] + line[1])