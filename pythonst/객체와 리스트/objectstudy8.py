# 문제 : 리스드에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요
# '화'가 리스트 안에 들어있는지 알려주세요

a = ['월', '화', '수', '목', '금', '토']

if '화' in a:
  print("있습니다.")
else:
  print("없습니다.")
  
# 문제 : 리스드에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요
# '화'가 리스트 안에서 몇 번째 데이터 인지 알려주세요

a = ['월', '화', '수', '목', '금', '토']
if '화' in a:
  i = a.index('화')
  print(i)
else:
  print("찾는 요소가 없습니다.")
  
# 문제 : 리스드에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요
# '화'가 리스트 안에 있는지 if문으로 체크 후, 있다면 삭제해주세요

a = ['월', '화', '수', '목', '금', '토']

if '화' in a:
  i = a.remove('화')
else:
  print("찾는 요소가 없습니다.")

print(a)

# 문제 : 리스드에 순서대로 '월', '화', '수', '목', '금'을 한번에 담아주세요
# '토'가 리스트 안에 있는지 if문으로 체크 후, 있다면 삭제해주세요

a = ['월', '화', '수', '목', '금', '토']

if '토' in a:
  i = a.remove('토')
else:
  print("찾는 요소가 없습니다.")

print(a)