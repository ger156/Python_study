# 문제 : 구구단8단을 출력해주세요
# 조건 : for, while문을 사용할 수 없습니다.

print("== 8단 ==")
print("8 * 1 = 8")
print("8 * 2 = 16")
print("8 * 3 = 24")
print("8 * 4 = 32")
print("8 * 5 = 40")
print("8 * 6 = 48")
print("8 * 7 = 56")
print("8 * 8 = 64")
print("8 * 9 = 72")

# 문제 : 구구단8단을 출력해주세요
# 조건 : 숫자 1 이외의 값을 사용할 수 없습니다. 소스코드를 수정해주세요.
# 조건 : for, while문을 사용할 수 없습니다.

dan = 8

i = 1

print("== {}단 ==".format(dan))
print("{} * {} = {}".format(dan, i, dan * i))
i = i + 1
print("{} * {} = {}".format(dan, i, dan * i))
i = i + 1
print("{} * {} = {}".format(dan, i, dan * i))
i += 1
print("{} * {} = {}".format(dan, i, dan * i))
i += 1
print("{} * {} = {}".format(dan, i, dan * i))
i += 1
print("{} * {} = {}".format(dan, i, dan * i))
i += 1
print("{} * {} = {}".format(dan, i, dan * i))
i += 1
print("{} * {} = {}".format(dan, i, dan * i))
i += 1
print("{} * {} = {}".format(dan, i, dan * i))