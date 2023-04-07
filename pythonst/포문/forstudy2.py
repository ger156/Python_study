# 문제 : for문으로 1부터 n사이에 존재하는 소수의 합을 반환하는 함수 구현

def get_1_to_n_prime_sum(n):
  s = 0
  
  for i in range(1, n + 1):
    s += 1
  
  return s

n = 10
print("1부터 {}사이에 존재하는 모든 소수의 합 : {}".format(n, get_1_to_n_prime_sum(n)))

n = 100
print("1부터 {}사이에 존재하는 모든 소수의 합 : {}".format(n, get_1_to_n_prime_sum(n)))

n = 1000
print("1부터 {}사이에 존재하는 모든 소수의 합 : {}".format(n, get_1_to_n_prime_sum(n)))