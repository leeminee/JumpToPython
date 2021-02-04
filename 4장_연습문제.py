print()

"""
[문제1]
주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
"""
print("[문제1]")
# def is_odd(number):
#     if number % 2 == 0:
#         return "짝수"
#     else:
#         return "홀수"
# #print(is_odd(int(input())))
# print(is_odd(27))
# print()
is_odd = lambda x: "짝수" if x % 2 == 0 else "홀수"
#print(is_odd(int(input())))
print(is_odd(3))
print()

"""
[문제2]
입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. 
(단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
※ 평균 값을 구할 때 len 함수를 사용해 보자.
"""
print("[문제2]")
def multi_number(*numbers):
    result = 0
    for i in numbers:
        result += i
    return result/len(numbers)
print(multi_number(1,2,3,4,5))
print()

"""
[문제3]
다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.
----------------------------------------
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")
total = input1 + input2
print("두 수의 합은 %s 입니다" % total)
----------------------------------------
이 프로그램을 수행해 보자.
첫번째 숫자를 입력하세요:3
두번째 숫자를 입력하세요:6
두 수의 합은 36 입니다
3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다. 이 프로그램의 오류를 수정해 보자.
※ int 함수를 사용해 보자.
"""
print("[문제3]")
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")
total = int(input1) + int(input2)
print("두 수의 합은 %d 입니다" % total)
print()

"""
[문제4]
다음 중 출력 결과가 다른 것 한 개를 골라 보자.
1. print("you" "need" "python")
2. print("you"+"need"+"python")
3. print("you", "need", "python")
4. print("".join(["you", "need", "python"]))
"""
print("[문제4]")
print("정답 : 3번  / 얘만 yum need python. 다른얘들은 youneedpython 으로 출력됨")
print()

"""
[문제5]
다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
----------------------------------------
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f2 = open("test.txt", 'r')
print(f2.read())
----------------------------------------
이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 
우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.
"""
print("[문제5]")
# f1 = open("test.txt", 'w')
# f1.write("Life is too short")
# f1.close()
# f2 = open("test.txt", 'r')
# print(f2.read())
with open("test.txt", 'w') as f1:
    f1.write("Life is too short\nyou need java")
with open("test.txt", 'r') as f2:
    print(f2.read())
print()

"""
[문제6]
사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자. 
(단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.)
"""
# print("[문제6]")
# with open("test.txt", 'a') as f3:
#     print(f3.write(input("저장할 내용을 입력하세요 : ")))
# print()

"""
[문제7]
다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
----------------------------------------
Life is too short
you need java
----------------------------------------
※ replace 함수를 사용해 보자.
"""
print("[문제7]")
f = open("test.txt",'r')
body = f.read()
f.close()
body = body.replace('java', 'python')
f = open('test.txt', 'w')
f.write(body)
f.close()
print()
