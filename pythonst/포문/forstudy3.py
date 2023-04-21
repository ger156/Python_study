# 문제 : 리스트에 2, 1, 5, 6, 7를 담고, for문으로 요소들을 역순으로 출력, len 사용

a = [2, 1, 5, 6, 7]

# for i in (a):
#   print(a)
# 편한방식으로 사용하면 됨
  
# for i in range(len(a)):
#   print(a[i])

# 역순으로 나타내기
for i in range(len(a) -1, -1, -1):
  print(a[i])