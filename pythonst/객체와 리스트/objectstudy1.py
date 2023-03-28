a = ['a1', 'a2', 'a3', 'a4', 'a5']

if 'a6' in a: # a 이라는 결과에 a1이 존재하는지 여부를 묻는다 결과 값이 있다면 True 없다면 False
  i = a.index('a1')
  print("i = {}".format(i))
else:
  print("찾는 요소가 없습니다.")

# print(len(a)) # len = 리스트의 길이(갯수)를 반환해서 준다.

# print(a.index('a1')) # index = 값이 어디에 있는지 찾아준다.
# a[0]
# a[1]
# a[2]
# a[3]
# a[4]