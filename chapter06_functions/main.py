'''
chapter06_functions package 생성
main 생성

1. 함수(function) : 특정 작업을 수행하는 코드 블록을 정의하는 방법

예를 '사진을 찍는다'라는 행위에 대해 생각해보면,
1) 주머니에서 폰을 꺼내고,
2) 잠금 화면을 풀고,
3) 카메라를 켜고,
4) 사진을 찍고자 하는 대상에 폰을 조준하고,
5) 셔터를 누른다.

라고 볼 수 있습니다. 그런데 컴퓨터는 시키는대로만 하기 때문에 사진을 찍기 위해서
1) - 5)까지의 명령어를 입력해줘야만 합니다.

하지만 '사진을 찍는다'라는 함수 내에 1) - 5)의 명령어들을 미리 입력해두고 나서,
'사진을 찍는다'라는 명령어를 실행시키기만 하면 1) - 5)까지의 명령들을 순서대로 수행하도록
하는 것이 함수의 개념이라고 할 수 있겠습니다.

주요 수업 예시로는 reeborg's world에서 turn_right()를 정의하는 것이었습니다.

함수 정의 형식 :
def turn_right():
    turn_left()
    turn_left()
    turn_left()

함수 호출 형식 :
turn_right()

2. 함수의 종류
    1) 파이썬 내장 함수
    2) 메서드(method)
    3) 사용자 정의 함수

3. 함수 용어 정리(멘토 파이썬 교재에 있습니다)
    1) 함수 정의 : 사용자 함수를 새로 만드는 것을 의미(def : define)
    2) 인수(argument) : 함수에 전달할 입력값(input)
    3) 매개변수(parameter) : 인수를 받아서 저장하는 변수를 의미
    4) 반환값 / 결과값 / 리턴값(return) : 함수의 출력값(output)
    5) 함수 호출(call) : 함수를 실제로 사용하는 것을 의미

4. (사용자) 함수의 형식 :
def 함수_이름(매개변수):
    실행문

변수 = 함수_이름(argument)
'''
# 함수 정의
# def write_name(name):      # 정의할 때 소괄호 내에 있는 것을 parameter라고 합니다.
#     print(f"당신의 이름은 {name}입니다.")
#
# # 함수 호출
# write_name("안근수")       # 호출할 때 소괄호 내에 있는 것을 argument라고 합니다.
#
# def write_name_age(name, age):  # parameter가 복수인 사례 및 함수 정의
#     print(f"당신의 이름은 {name}이고, 나이는 {age}살입니다.")
#
# write_name_age("안근수", 38)   # 매개변수가 두 개 이기 때문에 argument도 두 개인 상황
# write_name_age(age= 10, name= "안근순")    # keyword argument라고 함.
'''
우리가 예를 들어 input("이름을 입력하세요 >>> ")을 이용해서 이것을 name이라는 변수에 담았다고 가정하면,
name = input("이름을 입력하세요 >>> ")이라고 작성해왔습니다.

즉, 저희는 여태까지 함수의 결과값을 변수에 담아오고 있었습니다.

파이썬 내장 함수는 이미 함수가 정의돼있고, 개발자들은 함수 호출만 잘 하면 됩니다.
사용자 함수는 개발자 자신이 함수를 정의하고, 그 후에 호출하는 것까지의 과정이라고 생각하시면 됩니다.

내장 함수 예시
print() / type() / int() / flat() / input()

2. 메서드(method) : 특정 객체가 가지고 있는 함수를 의미. 특정 자료형에 포함돼있는 함수.
사실 함수와 메서드는 동일한 개념이지만, 호출 방식에 있어서의 차이가 있습니다.

함수는 독립적으로 사용 가능 / 메서드는 특정 객체를 통해서만 호출 가능
'''
# eng_name = input("당신의 이름을 소문자로 입력하세요 >>> ").upper()
# # 이상의 코드에서 input()은 함수, .upper()는 메서드
# print(eng_name)     # 얘는 함수
# eng_name2 = input("당신의 이름을 소문자로 입력하세요 >>> ").title()
# print(eng_name2)
'''
함수(메서드)의 유형
'''
# # 매개변수 x / 리턴 x
# def call1():
#     print("[ x | x ]")
#
# # 매개변수 o / 리턴 x
# def call2(str_type):
#     print("[ o | x ]")
#     print(f"{str_type}이라고 입력하셨나보네요")
#
# # 매개변수 x / 리턴 o
# def call3():
#     print("[ x | o ]")
#     return 1
#
# # 매개변수 o / 리턴 o
# def call4(str_type):
#     print("[ x | o ]")
#     return f"제 이름은 {str_type}입니다."
#
# call1()
# call2("오늘 날씨 너무 추워요😥")
# call3() # 이 경우 return이 출력되지 않습니다.
# print(call3())  # 이래야 return이 출력됩니다.    -> 그럼 길게 써야하니까 불편한거 아닌가요?
# print(call3() + 1)
#
# new_element = (call3() +3) * 10
# print(new_element)
#
# call4("안근수")
# print(call4("안근수"))
'''
call3() / call4() 유형에서 함수 내에 print()를 집어넣어두면 main단계에서(들여쓰기가 되어있지 않은 단계에서)
print() 함수를 입력할 필요가 없어 훨씬 편할 것 같은데
왜 굳이 return 형태로 입력해서 main에서 일일이 print() 함수를 적용해야 하는가?

함수형 프로그래밍(Functional Programming) : 특정한 함수1의 결과값이
    또 다른 함수2의 argument로 사용되는 것을 의미합니다.
    그리고 함수2의 결과 값이 함수3의 argument로 사용되는 것이 반복된다면,
'''
# 사용자 함수를 정의
# def introduce(name, address):           # call4() 유형으로 정의
#     return f"제 이름은 {name}이고, {address}에 삽니다.😀"

# 함수1 사용 : input() -> 파이썬 내장 함수
# name = input("이름을 입력하세요 >>> ")
# address = input("주소를 입력하세요 >>> ")

# 함수1의 결과값을 함수2인 사용자 함수의 argument로 사용 -> 그 결과값을 함수3인 print()함수의 argument로 사용
# print(introduce(name, address))
'''
700원 짜리 음료수를 뽑을 수 있는 자판기 프로그램을 구현하시오. 돈을 넣으면 몇 잔의 음료수를
뽑을 수 있는지, 그리고 잔돈은 얼마인지 모든 경우의 수를 출력하도록 합니다.

함수 정의
- 반환값 : 없음(call1-4 중 어떤 유형일지 고려하세요)
- 함수이름 : vending_machine()
- 매개변수 : 정수 money

코드 구성

def vending_machine():
    # 함수 구현
    
vending_machine(3000)

실행 예
음료수 = 0개, 잔돈 = 3000원
음료수 = 1개, 잔돈 = 2300원
음료수 = 2개, 잔돈 = 1600원
음료수 = 3개, 잔돈 = 900원
음료수 = 4개, 잔돈 = 200원
'''







