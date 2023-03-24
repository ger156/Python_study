# 문제 : 구구구단 출력하세요

dan = 1
while dan <= 3:
  print("== {}단 ==".format(dan))
  
  i = 1
  while i <= 3:
    
    j = 1
    while j <= 3:
      print("{} * {} * {} = {}".format(dan, i, j, dan * i * j))
      j += 1
    
    i += 1
  
  dan += 1

