# jumin = "960915-1783018"

# print("성별 : " + jumin[7]) # index는 0부터 시작
# print("연 : " + jumin[0:2]) # 0부터 2직전까지
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# print("생년월일 : " + jumin[0:6])
# print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지
# print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:])


# #문자열

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)

# index = python.index("n", index + 1)
# print(index)

# print(python.find("Java"))

# print(python.count("n"))

#문자열 포맷

# print("a" + "b")
# print("a", "b")

# # 방법 1
# print("나는 %d살입니다." % 20) #d 는 정수값
# print("나는 %s을 좋아해요." % "파이썬") #s 는 문자열
# print("Apple 은 %c로 시작해요. " % "A") #c 는 캐릭터값(하나만 표시함)

# print("나는 %s색과 %s색을 좋아해요." %("파란", "빨강"))

# # 방법 2
# print("나는 {}살 입니다.".format(20))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨강"))

# # 방법 3
# print("나는 {color}살이며, {age}색을 좋아해요.".format(age = 20, color = "빨강"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨강"))

# #방법 4
# age = 20
# color = "빨강"
# print(f"나는 {age}살이며, {color}색을 좋아해요.") # f는 실제 지정된 변수의 값을 불러옴

# # 탈출문자


# # \n : 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타")


# # \" or\' : 문장 내에서 따옴포
# # 저는 "나도코딩"입니다.
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")

# # \\ : 문장 내에서 \
# print("C:\\Users\\손원재\\Desktop\\PythonWorkspace>")

# #\r : 커서를 맨 앞으로 이동
# print("Red Apple \r Pine")

# # \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# # \t : 탭
# print("Red\tApple")


# # Quiz)_사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# # 예) http://naver.com
# # 규칙1 : http:// 부분은 제외 => naver.com
# # 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# # 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성

# url = "http://naver.com"
# my_str = url.replace("http://", "") # 규칙1
# my_str = my_str[:my_str.index(".")] # my_str[0:5] -> 0 ~ 5 직전까지
# print(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

# print("{0}의 비밀번호는 {1}입니다.".format(url, password))


# 리스트 [] 순서를 가지는 객체의 집합

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10,20,30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# # 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하")
# print(subway)

# # 정형돈씨를 유재석씨와 조세호씨 사이에 태워봄
# subway.insert(1, "정형돈")
# print(subway)

# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# # print(subway.pop())
# # print(subway)

# # print(subway.pop())
# # print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석")

# # 정렬도 가능
# num_list = [5, 2, 4, 3, 1]
# num_list.sort()
# print(num_list)

# # 순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# # 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
# num_list = [5, 2, 4, 3, 1]
# mix_list = ["조세호", 20, True]
# print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)

# #사전
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5]) # 뒤의 값 출력 x
# print(cabinet.get(5)) # 뒤의 값 출력
# print(cabinet.get(5, "사용 가능"))
# print("hi")

# print(3 in cabinet) # True
# print(5 in cabinet) # False

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# # 손님 빠빠이
# del cabinet["A-3"]
# print(cabinet)

# # key들만 출력
# print(cabinet.keys())

# # value 들만 출력
# print(cabinet.values())

# # Key, value 쌍으로 출력
# print(cabinet.items())

# #목욕탕 폐점
# cabinet.clear()
# print(cabinet)



# # 튜플

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# # menu.add("생선까스") 튜플은 추가 안됨

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)



# # 세트

# # 집합 (set)
# # 중복 안됨, 순서 없음
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# # 교집합 (jave와 python을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# # 합집합 (java도 할 수 있거나 python을 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# # 차집합 (java는 할 수 있지만 python을 할 줄 모르는 개발자)
# print(java - python)
# print(java.difference(python))

# # python을 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 잊은 사람
# java.remove("김태호")
# print(java)


# # 자료구조의 변경

# menu = {"커피", "우유", "주스"}
# print(menu, type(menu)) # 세트형태

# menu = list(menu)
# print(menu, type(menu)) # 리스트형태

# menu = tuple(menu)
# print(menu, type(menu)) # 튜플형태

# menu = set(menu)
# print(menu,type(menu)) # 세트형태



# Quiz) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명의 커피 쿠폰을 받게 됩니다.

# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다. --

# (활용예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1)) # 리스트 중에서 무작위로'1'개 뽑음

# from random import *
# users = range(1, 21) # 1부터 20까지 숫자 생성
# # print(type(users))
# users = list(users)
# # print(type(users))
# shuffle(users)

# winners = sample(users, 4) #4명 중에서 1명은 치킨 3명은 커피당첨자

# print(" -- 당첨자 발표 -- ")
# print(" 치킨 당첨자 : {0} ".format(winners[0]))
# print(" 커피 당첨자 : {0} ".format(winners[1:]))
# print(" -- 축하합니다 -- ")


# 분기(if)

# weather = "미세먼지"
# if weather == "비":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else :
#     print("준비물 필요 없어요")

# weather = input("오늘 날씨는 어때요?")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else :
#     print("준비물 없어요")

# temp = int(input("기온은 어때요?"))
# if 30 <= temp:
#     print("너무 더워요, 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날시에요")
# elif 0 <= temp and temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지마세요")



# 반복문(for)

# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in range(1, 6): # 1, 2, 3, 4, 5
#     print("대기번호 :{0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))


# 반복문(while)

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")


# 무한루프

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer,index))
#     index += 1



# # 반복문 탈출

# customer = "토르"
# person = "Unknown"

# while person != customer :
#     print("{0}, 커피가 준비되었습니다.".format(customer,))
#     person = input("이름이 어떻게 되세요?")


# # continue 와 break

# absent = [2, 5] # 결석
# no_book = [7] # 책을 깜빡했음
# for student in range(1, 11): #1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}은 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))


# 한줄 for

 #출석번호가 1, 2, 3, 4, 앞에 100을 붙이기로 함 -> 101, 102, 103 ~
# students = [1, 2, 3, 4, 5]
# print(students)
# students = [ i+100 for i in students]
# print(students)

# # 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# # 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)


# Quiz) 당신은 cocoa 서비스를 이용하는 택시기사님입니다.
# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.

# 조건 1 : 승객별 운행소요 시간은 5분 ~ 50분 사이의 난수로 정해집니다.
# 조건 2 : 당신은 소요 시간 5분 ~ 15분 사이의 승객만 매칭해야 합니다.

# (출력문 예제)
# [O] 1번째 손님 (소요시간 : 15분)
# [ ] 2번째 손님 (소요시간 : 50분)
# [O] 3번째 손님 (소요시간 : 5분)
# ...
# [ ] 50번째 손님 (소요시간 : 16분)

# 총 탑승 승객 : 2 분

# from random import *
# cnt = 0 # 총 탑승 승객 수
# for i in range(1,51): # 1 ~ 50이하의 수 (승객)
#     time = randrange(5,51) # 5분 ~ 50분 소요 시간
#     if 5 <= time <= 15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         cnt += 1
#     else :
#         print ( " [ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

# print ("총 탑승 승객 : {0}분".format(cnt))


# 함수

# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money): # 입금
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money


# balance = 0 # 잔액
# balance = deposit(balance, 1000)
# print(balance)

# def withdraw(balance, money): # 출금
#     if balance >= money: # 잔액이 출금보다 많으면
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
#         return balance

# balance = 1000 # 잔액
# balance = deposit(balance, 1000)
# balance = withdraw(balance, 2000)


# (활용예제)
# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst, 1)) # 리스트 중에서 무작위로'1'개 뽑음