# 문제 : 구구단 출력하세요

dan = 2
while dan <= 9:
  print("== {}단 ==".format(dan))
  
  i = 1
  while i <= 9:
    print("{} * {} = {}".format(dan, i, dan * i))
    i += 1
  
  dan += 1

