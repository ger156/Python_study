# 문제 : 10대, 20대, 30대 중 나이에 맞는 변수를 출력해주세요.

age = 10

if age >= 10 and age <= 19: # 나이가 10이상, 19이하
  print('10대 입니다')
elif age >= 20 and age <= 29: # 나이가 20이상, 29이하
  print('20대 입니다')
else: # 빠져나오는 코드로 클린하게 정리 가능
# 밑 코드도 맞지만, 원하는 값에 의해서 원하는 조건을 출력해줌
# elif age >= 30 and age <= 39: # 나이가 30이상, 39이하
  print('30대 입니다')