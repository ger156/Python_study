# 문제 : 1부터 100사이의 짝수만 출력해주세요.

# v1
i = 2
while i <= 100:
  print(i)
  i += 2
  
# v2
i = 1
while i <= 100:
  if i % 2 == 0:
    print(i)
  i += 1
  
# 문제 : 1부터 1000사이의 수 중에서 3의 배수만 출력해주세요.
# v1
i = 3
while i <= 1000:
  print(i)
  i += 3

# v2
i = 1
while i <= 1000:
  if i % 3 == 0:
    print(i)
  i += 1
