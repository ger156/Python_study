# 딕셔너리
ages = {
    "철수": 10, # key : value 로 이루어져있음
    "영희": 20,
    "영수": 30,
}
print("철수 나이 :",ages = ["철수"])
print("영희 나이 :",ages = ["영희"])
print("영수 나이 :",ages = ["영수"])

print("== 딕셔너리 반복 v1 ==")
for name in ages:
    age = ages[name]
    print("{}나이 : {}".format(name, age))

print("== 딕셔너리 반복 v2 ==")
for name in ages.keys():
    age = ages[name]
    print("{}나이 : {}".format(name, age))
    # print(name)

print("== 딕셔너리 반복 v3 ==")
for name in ages.keys():
    print("나이 : {}".format(age))

print("== 딕셔너리 반복 v4 ==")
for name, age in ages.items():
    print("나이 : {}".format(name, age))

del ages["철수"]
print("== 딕셔너리 반복 v4(철수 삭제 후) ==")
for name, age in ages.items():
    print("나이 : {}".format(name, age))

# ages["수민"] = 40 # 데이터 추가
# print(ages)

# ages["수민"] = 50 # 데이터 수정
# print(ages)

# 데이터를 여러개 묶을 때 사용
# 콜렉션, 객체
# 콜렉션(객체)
# -리스트, 딕셔너리
# 객체

# 리스트의 장점
# 데이터를 넣을 때 편하다.

# 딕셔너리 장점
# 데이터를 가져올 때 편하다.
