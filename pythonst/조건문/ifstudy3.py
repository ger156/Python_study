# 문제 : 할인 대상인지 아닌지 출력해주세요.
# 조건 : 나이가 19세 이하이거나 60세 이상이면 할인 대상입니다.
# 조건 : and, or 없이 풀어야 합니다.
# 조건 : 2가지 이상의 방법으로 풀어야 합니다.

age = 33

print("== 정답 v1 ==")
if age <= 19:
  print("할인 대상입니다.")
  
if age >= 60:
  print("할인 대상이 아닙니다.")
  
if age > 20:
  if age <60:
    print("할인 대상이 아닙니다.")
    
print("== 정답 v2 ==")
if age <= 19:
  print("할인 대상입니다.")
elif age >= 60:
  print("할인 대상이 아닙니다.")  
else:
    print("할인 대상이 아닙니다.")

# and연산자 와 or연산자 없이 풀어봤습니다!