# 문제 : 리스트에 각 달의 끝 날짜를 담고,
# '1월은 31일까지'와 같은 양식으로 출력, enumerate
end_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i, end_days in enumerate(end_days):
  month = i + 1
  print("{}월은 {}일까지".format(month, end_days))