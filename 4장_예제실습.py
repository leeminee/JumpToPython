print()

"""
[매개변수(parameter)와 인수(arguments)]
- 매개변수는 함수에 입력으로 전달된 값을 받는 변수이다.
- 인수는 함수를 호출할 때 전달하는 입력값을 의미한다.
"""

print("[ex1]")
def add(a, b): # a,b 는 매개변수
    return a+b
print(add(3, 4)) # 3,4 는 인수
print()

print("[ex2]")
def add(*many):
    result = 0
    for i in many:
        result += i
    return result
print(add(1,2,3,4,5,6,7,8,9,10))
print()

print("[ex3]")
def add_multi(choice, *numbers):
    if choice == "add":
        result = 0
        for i in numbers:
            result += i
    elif choice == "mul":
        result = 1
        for i in numbers:
            result *= i
    return result
print(add_multi("add", 1,2,3,4,5))
print(add_multi("mul", 1,2,3,4,5))
print()

"""
[키워드 파라미터]
- 매개변수 앞에 별 두개(**)를 붙여 사용한다.
- **keywords 에서 keywords 는 딕셔너리가 되고 모든 key=value 형태의 결과값이 그 딕셔너리에 저장된다.
ex) def print_key(**keywords):
        print(keywords)
    >>> print_key(a=1, name='foo')
    {'a' : 1, 'name' : 'foo'}
"""

print("[ex4]")
def add_and_mul(a,b):
    return a+b, a*b
result = add_and_mul(3,4)
print(result)
print()

print("[ex5]")
def say_nick(nick):
    if nick == '바보':
        return
    print(f"나의 별명은 {nick}입니다")
say_nick('야호')
say_nick('바보')
print()

"""
[매개변수에 초기값 미리 설정]
- 초기값을 설정해 놓은 매개변수 뒤에 초기값을 설정해 놓지 않은 매개변수는 사용할 수 없다.
- 즉, 매개변수로 (name, old, man=True)는 되지만 (name, man=True, old)는 안된다.
- 초기화 시키고 싶은 매개변수를 항상 뒤쪽에 놓자.
"""

print("[ex6]")
def say_myself(name, old, man=True):
    print(f"나의 이름은 {name}입니다.")
    print(f"나이는 {old}살 입니다.")
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")
say_myself('박응용',25)
say_myself('박응용',25,False)
print()

"""
[global 명령어]
함수안에서 global a 와 같이 사용하면 함수 밖의 a 변수를 직접 사용하겠다는 의미이다.
하지만 함수는 독립적으로 존재하는것이 좋고, 외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니다.
그러므로 가급적 global 명령어는 피하자.
"""

"""
[lambda(람다)]
- 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다.
- 함수를 간결하게 만들 때 사용한다.
- def를 사용해야 할 정도로 복잡하지 않거나 def 를 사용할 수 없는 곳에 주로 사용한다.
- return 명령어가 없어도 결과값을 반환한다.
- 사용법은 다음과 같다.
※ lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식
"""

print("[ex7]")
add = lambda a, b: a+b
print(add(3,4))
print()

print("[ex8]")
print("life" "is" "too short")
print("life"+"is"+"too short")
print("life","is","too short")
print()

"""
[한 줄에 여러 결과값 출력]
- 한 줄에 결과값을 계속 이어서 출력하려면 매개변수 end를 사용해서 끝 문자를 지정해야 한다.
ex) for i in range(10):
        print(i, end=' ')
    0 1 2 3 4 5 6 7 8 9
"""

"""
[파일 생성]
파일 객체 = open(파일이름, 파일 열기 모드)
-with 문과 같이 사용하면 with 블록을 벗어나는 순간 열린 파일 객체가 자동으로 close 된다.
※ 파일 열기 모드
 - r : 읽기모드 - 파일을 읽기만 할 때 사용
 - w : 쓰기모드 - 파일에 내용을 쓸 때 사용
                - 파일이 존지할 경우 원래 있던 내용이 모두 사라짐
 - a : 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용
"""

"""
[파일 읽기 종류]
- readline : 파일 내부의 한 줄 읽기
- readlines : 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 반환.
- read : 파일의 내용 전체를 문자열로 반환. 즉 파일의 전체 내용이다.
"""

print("[ex9]")
f = open("파일생성.txt", 'w')
for i in range(1,11):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()
print()

print("[ex10]")
f = open("파일생성.txt", 'r')
while True:
    line = f.readline()
    if not line :
        break
    print(line)
f.close()
print()

print("[ex11]")
f = open("파일생성.txt", 'r')
lines = f.readlines()
print(lines)
for line in lines:
    print(line)
f.close()
print()

print("[ex12]")
f = open("파일생성.txt", 'r')
data = f.read()
print(data)
f.close()
print()

print("[ex13]")
f = open("파일생성.txt", 'a')
for i in range(11,21):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()
print()

print("[ex14]")
with open("foo.txt", 'w') as f:
    f.write("Life is too short, you need python")
print()

print("[ex15]")
import sys

args = sys.argv[1:]
for i in args:
    print(i)
print()
