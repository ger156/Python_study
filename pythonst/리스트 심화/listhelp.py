# 리스트를 이용해 데이터를 관리하는 프로그램을 만들어보겠습니다.
# 입력값에 help를 입력하면 아래처럼 나오게 해주세요
# 명령어를 입력해주세요: 는 exit를 치기 전까지 계속 나와야합니다.

# (입출력 예시)

# 명령어를 입력해주세요 : help

# add : 데이터 추가
# read : 데이터 조회
# update : 데이터 수정
# delete : 데이터 삭제

# 명령어를 입력해주세요:

# TodoList
# 1. 명령어를 입력해주세요. 출력
# 2. 입력값에 help를 입력하고, 입력한 내용 출력[.]
# 3. 각각의 명령어 도움말 출력하기
# 4. 지금 구조를 반복문을 통해 무한실행해보기
# 5. help를 입력하면 입력한 명령어에 맞는 내용 출력
# 6. exit를 입력해서 간단한 메세지 출력해보기
# 7. exit를 입력하면 프로그램 종료하기

while True:
  print("명령어를 입력해주세요. :", end = '')
  cmd = input()

  if cmd == "help":
    print("add : 데이터 추가")
    print("read : 데이터 조회")
    print("update : 데이터 수정")
    print("delete : 데이터 삭제")
  
  elif cmd == "exit":
    print("프로그램을 종료합니다.")
    break