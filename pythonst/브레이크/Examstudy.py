# i = 1
# while True:
#   print(i)
  
#   if i == 100:
#     break
  
#   i += 1

# i = 1
# while i != 100:
#   print(i)
#   i += 1
# 이렇게 사용이 가능하다.

# 브레이크 문은 반복문을 끝내고 빠져나오게 끔 해줍니다.

i = 1
dan = 8
while i <= 9:
  if i == 4:
    i += 1
    continue
  print("{} * {} = {}".format(dan, i, dan * i))
  i += 1