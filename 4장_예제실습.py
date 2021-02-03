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

print("[ex9]")
print()

print("[ex10]")
print()