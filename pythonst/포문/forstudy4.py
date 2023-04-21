# 문제 : 리스트에 각 달의 끝 날짜를 담고, '1월은 31일까지'와 같은 양식으로 출력

end_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

current_month = 1

for end_day in end_days:
  print("{}월은 {}일까지".format(current_month, end_day))
  current_month += 1