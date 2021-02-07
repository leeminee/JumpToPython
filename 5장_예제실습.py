
print("[예제1]")
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
cal1 = Calculator()
cal2 = Calculator()
print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
print()

"""
[클래스와 객체]
- 클래스(Class) : 붕어빵 틀
        : 똑같은 무엇인가를 계속해서 만들어 낼 수 있는 설계 도면.
- 객체(Object) : 클래스로 만든 피조물
               : 동일한 클래스로 만든 객체들은 서로 전혀 영향을 주지 않는다.  
"""

"""
[객체와 인스턴스]
a = Cookie()
- 클래스로 만든 객체를 인스턴스라고도 한다.
- a는 객체이다. 그리고 a 객체는 Cookie의 인스턴스이다.
"""

print("[예제2]")
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = FourCal(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print()

"""
[생성자(Constructor)]
- 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다.
- 객체에 초깃값을 설정해야 할 필요가 있을때 
  다른 메서드를 호출하여 초깃값을 설정하는것보다 생성자를 구현하는 것이 안전한 방법이다.
- 파이썬 메서드 이름으로 __init__ 이 생성자이다.
- __init__ 을 선언하면 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출된다.
"""

"""
[상속(Inheritance]
- 어떤 클래스를 만들때 다른 클래스의 기능을 물려받을 수 있게 만드는 것이다.
- 클래스를 상속하기 위해서는 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어주면 된다.
   class 클래스 이름(상속할 클래스 이름)
- 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황에 상속을 사용해야 한다.
"""

print("[예제3]")
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
a = MoreFourCal(4,2)
print(a.pow())
print()

"""
[메서드 오버라이딩(Overriding, 덮어쓰기)]
- 부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것
- 위와 같이 메서드를 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.
"""

"""
[import]
- import는 이미 만들어 놓은 파이썬 모듈을 사용할 수 있게 해주는 명령어이다.
- 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가 저장된 디렉터리에 있는 모듈만 불러올 수 있다.
- 파이썬 라이브러리는 파이썬을 설치할 때 자동으로 설치되는 파이썬 모듈을 말한다.
- 도트 연산자(.)를 사용해서 import a.b.c처럼 import할 때 가장 마지막 항목인 c는 반드시 모듈 또는 패키지여야만 한다.
- 모듈이름은 .py 확장자를 제거하고 적어야 한다.
  import 모듈이름 
  or 
  from 모듈이름 import 모듈함수
  or 
  from 모듈이름 import *
"""

"""
[if __name__ == "__main__"]
- python mod1.py 처럼 직접 파일을 실행했을 때는 참이 되어 if문 다음 문장이 수행된다.
  반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는 거짓이 되어 if문 다음 문장이 수행되지 않는다.
"""

"""
[__name__ 변수]
- 파이썬이 내부적으로 사용하는 특별한 변수 이름이다.
- python mod1.py 처럼 직접 파일을 실행할 경우 mod1.py의 __name__ 변수에는 __main__ 이 저장된다.
  하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import 할 경우에는 mod1.py의 __name__ 변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.
"""

print("[예제4]")
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
a = SafeFourCal(4,0)
print(a.div())
print()

"""
[sys.path.append("모듈을 저장한 디렉터리")]
- sys.path 는 파이썬 라이브러리가 설치되어 있는 디렉터리를 보여준다.
- sys.path.append를 사용해서 사용할 모듈의 저장된 디렉터리를 추가하여 해당 모듈울 불러와 사용할 수 있다. 
- 'set PYTHONPATH = 모듈을 저장한 디렉터리' 를 사용하면 디렉터리 이동이나 별도의 모듈 추가 작업 없이 해당 모듈을 불러와서 사용할 수 있다. 
"""

"""
[__init__.py 의 용도]
- __init__.py 파일은 해당 디렉터리가 패키지의 일부임을 알려주는 역할을 한다.
- 패키지에 포함된 디렉터리에 __init__.py 파일이 없다면 패키지로 인식되지 않는다.
※ python3.3 버전부터는 해당 파일이 없어도 패키지로 인식하지만, 
   하위 버전 호환을 위해 __init__.py 파일을 생성하는 것이 안전하다.
"""

"""
[특정 디렉터리의 모듈을 * 사용하여 import 할때]
- 해당 디렉터리의 __init__.py 파일에 __all__ 변수를 설정하고 import 할 수 있는 모듈을 정의해 주어야한다.
ex ) # C:/doit/game/sound/__init__.py
       __all__ = ['echo']
- __all__ 과 상관없이 무조건 import 되는 경우는 from a.b.c import * 에서 from의 마지막 항목인 c가 모듈인 경우이다.
"""

"""
[relative 한 접근자]
- .. : 부모 디렉터리
- . : 현재 디렉터리
- .. 과 같은 relative 한 접근자는 모듈 안에서만 사용해야 한다.
"""

print("[예제5]")
print()

print("[예제6]")
print()

print("[예제7]")
print()

print("[예제8]")
print()

print("[예제9]")
print()

print("[예제10]")
print()
