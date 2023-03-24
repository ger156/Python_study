# 문제 : 1부터 100까지의 수 중에서 짝수의 합을 출력해주세요.

# i = 1
# sum = 0
# while i <= 100:
#   if i % 2 == 0:
#     sum = sum + i
#     print(sum)
#   i += 1
  
# print("sum : {}".format(sum))

# 문제 : 1부터 100까지의 수 중에서 짝수이고 3의 배수가 아닌 수의 합을 출력해주세요.

i = 1
sum = 0
while i <= 100:
  if i % 2 == 0 and i % 3 != 0:
    sum += i
  i += 1
  
print("sum : {}".format(sum))