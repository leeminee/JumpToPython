
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

print("[예제4]")
print()

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
