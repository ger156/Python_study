# 딕셔너리에 달의 마지막 날들을 한번에 담고, keys()로 key, value 순회출력

month_end_days = {}
month_end_days_list_ver = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i, end_day in enumerate(month_end_days):
    month = str(i + 1) + "월"
    month_end_days[month] = end_day

for month in month_end_days.keys():
    end_day = month_end_days[month]
    # print("{} 은 {}까지 있습니다.".format(month, end_day))
    print(month + "은" + str(end_day) + "까지 있습니다.")