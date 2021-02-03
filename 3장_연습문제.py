print()

"""
[문제1]
다음 코드의 결과값은 무엇일까?
a = "Life is too short, you need python"
if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
"""
print("[문제1]")
print("shirt")
print()

"""
[문제2]
while 문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
"""
print("[문제2]")
number = 0
result = 0
while number < 1001:
    number += 1
    if number%3 == 0:
        result += number
print(result)
print()

"""
[문제3]
while 문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
*
**
***
****
*****
"""
print("[문제3]")
star = "*"
i = 1
while i < 6:
    print(star*i)
    i += 1
print()

"""
[문제4]
for 문을 사용해 1부터 100까지의 숫자를 출력해 보자.
"""
print("[문제4]")
for number in range(1,101):
    print(number)
print()

"""
[문제5]
A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for 문을 사용하여 A 학급의 평균 점수를 구해 보자.
"""
print("[문제5]")
res = 0
grades = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for grade in grades:
    res += grade
print(res/len(grades))
print()

"""
[문제6]
리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다.
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)
위 코드를 리스트 내포(list comprehension)를 사용하여 표현해 보자.
"""
print("[문제6]")
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 != 0]
print(result)
print()
