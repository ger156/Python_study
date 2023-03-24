# 함수를 사용해서 중복을 제거, 8단 출력

def print8Dan():
  dan = 8
  
  i = 1
  while i <= 9:
    print("{} * {} = {}".format(dan, i, dan * i))
    i += 1
    
i = 1
while i <= 10:
  print("== {}번째 구구단 8단 출력 ==".format(i))
  print8Dan()
  i += 1