print()

"""
[조건문 다음에 콜론(:)]
- if, while, for, def, class 문의 문장 끝에 콜론(:)이 항상 들어간다.
"""

"""
[파이썬에서 들여쓰기]
- : 다음 수행되어야 할 코드에 들여쓰기를 하지 않으면 오류발생
- 들여쓰기를 했지만 하나라도 너비가 다르다면 오류발생
- 들여쓰기(Tab)는 공백(Space) 4개와 동일하다. 어느것을 해도 상관은 없으나 2가지를 혼용해서 쓰지는 말자.
"""

print("[ex1]")
money = True
if money:
    print("택시를")
    print("타고")
    print("가라")
print()

print("[ex2]")
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
print()

print("[ex3]")
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")
print()

"""
[조건부 표현식]
- 다음과 같이 정의한다.
조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
- 조건부 표현식은 가독성에 유리하고 한 줄로 작성할 수 있어 활용성이 좋다.
"""
print("[ex4]")
score = 100
message = "success" if score >= 60 else "failure"
print()

# print("[ex5]")
# prompt = """1. Add
# 2. Del
# 3. List
# 4. Quit
#
# Enter number:
# """
# number = 0
# while number != 4:
#     print(prompt)
#     number = int(input())
# print()

# print("[ex6]")
# coffee = 10
# while True:
#     money = int(input("돈을 넣어 주세요 : "))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee - 1
#     elif money > 300:
#         print("거스름돈 %d를 주고 커피를 줍니다." % (money - 300))
#         coffee = coffee - 1
#     else:
#         print("돈을 다시 돌려주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d개 입니다." % coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
#         break
# print()

print("[ex7]")
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
print()

print("[ex8]")
a = [(1,2), (3,4), (5,6)]
for (first,last) in a:
    print(first+last)
print()

print("[ex9]")
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print(f"{number}번 학생은 불합격입니다.")
print()


print("[ex10]")
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    print(f"{number}번 학생 축하합니다. 합격입니다.")
print()

print("[ex11]")
add = 0
for i in range(1,11):
    add += i
print(add)
print()

print("[ex12]")
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print(f"{number+1}번 학생 축하합니다. 합격입니다.")
print()

print("[ex13]")
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print()
print()

print("[ex14]")
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)
print()

print("[ex15]")
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)
print()

"""
[리스트 내포 문법]
- 표현식 for 항목 in 반복가능객체 if 조건문
- if 조건문은 생략 가능하다.
"""

print("[ex16]")
result = [x*y for x in range(2,10) for y in range(1,10)]
print(result)
print()


