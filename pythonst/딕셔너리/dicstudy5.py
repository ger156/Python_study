# 딕셔너리에 달의 마지막 날들을 한번에 담고, values()로 value 순회출력

month_end_days = {}
month_end_days_list_ver = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i, end_day in enumerate(month_end_days_list_ver):
    month = str(i + 1) + "월"
    month_end_days[month] = end_day

for key, value in month_end_days.items():
    print(key + " : " + str(value) + "일")
    