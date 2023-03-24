# 문제 : 구구단 n단 ~ m단 중 홀수단만 1 ~ Limit 까지 곱 중 짝수곱만 출력해주세요.

n = 4
m = 19
limit = 11

dan = n # 구구단 시작값
while dan <= m: # 구구단 끝값
  if dan % 2 != 0: 
    print("== {}단 ==".format(dan))
  
    i = 1
    while i <= limit:
      if i % 2 == 0:
        print("{} * {} = {}".format(dan, i, dan * i))
      i += 1
  
  dan += 1
  
# 문제 : 구구단 n단 ~ m단 중 홀수단만 1 ~ Limit 까지 곱 중 짝수곱만 출력해주세요.
# 반복문 기본 포맷 만들기 (1~10까지 출력)
# 구구단 포맷 만들기
# n ~ m 단 출력하기
# 홀수단만 출력하기
# 1 ~ Limit 까지 곱 출력하기
# 짝수곱만 출력하기

#순서대로 차근차근 복습해보기