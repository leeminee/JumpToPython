
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

"""
[오류 예외처리]
- 구조는 아래와 같다.
  try:
   ...
  except (발생 오류(as 오류 메시지 변수)):
   ...
  else: # 오류가 없을 경우에만 수행
   ...
- NotImplementedError 는 파이썬 내장오류로, 꼭 작성해야 하는 부분이 구현되지 않았을경우 일부러 오류를 일으키기 위해 사용한다.
"""

"""
[raise 명령어]
- 파이썬은 raise 명령어를 사용해 오류를 강제로 발생시킬 수 있다.
"""

"""
[__str__ 메서드]
- print(e)처럼 오류 메시지를 print 문으로 출력할 경우에 호출되는 메서드이다.
"""

print("[예제5]")
class MyError(Exception):
    def __str__(self):
        return '허용되지 않는 별명입니다.'
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)
try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    print(e)
print()


"""
----------------------------------------------------------------------------------------------------
<<< 내장함수 >>>

[내장함수]
- 파이썬의 내장함수는 외부모듈과 달리 import가 필요하지 않아 아무런 설정 없이 바로 사용할 수 있다.

[abs(x)]
- 어떤 숫자를 입력받았을 때, 그 숫자의 절댓값을 돌려주는 함수이다.

[all(x)]
- 반복 가능한 자료형 x를 입력 인수로 받으며 이 x의 요소가 모두 참이면 True, 하나라도 거짓이면 False를 반환.
  ※ 반복 가능한 자료형이란 for문으로 그 값을 출력할 수 있는 것을 의미한다. 
     리스트, 튜플, 문자열, 딕셔너리, 집합 등이 있다.

[any(x)]
- 반복 가능한 자료형 x를 입력 인수로 받으며 이 x의 요소 중 하나라도 참이면 True, 모두거짓일 때에만 False 반환.
- all(x)의 반대이다.

[chr(i)]
- 아스키코드 값을 입력받아 그 코드에 해당하는 문자를 출력.

[ord(c)]
- 문자의 아스키코드 값을 돌려주는 함수
- chr 함수와 반대이다.

[dir]
- 객체가 자체적으로 가지고있는 변수나 함수를 보여준다.
ex) >>> dir([1, 2, 3])
['append', 'count', 'extend', 'index', 'insert', 'pop',...]
>>> dir({'1':'a'})
['clear', 'copy', 'get', 'has_key', 'items', 'keys',...]

[divmod(a,b)]
- 2개의 숫자를 입력받고, a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수.

[enumerate]
- '열거하다' 라는 뜻이다.
- 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다. 
ex) >>> for i, name in enumerate(['body', 'foo', 'bar']):
...     print(i, name)
...
0 body
1 foo
2 bar

[eval]
- 실행가능한 문자열을 입력으로 받아 문자열을 실행한 결과값을 돌려주는 함수.
ex ) >>> eval('1+2')
3
>>> eval("'hi' + 'a'")
'hia'
>>> eval('divmod(4, 3)')
(1, 1)

[filter]
- 첫번째 인수로 함수 이름을, 두번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다.
  그리고 두번째 인수인 반복 가능한 자료형 요소가 첫번째 인수인 함수에 입력되었을 때 반환 값이 참인 것만 묶어서 돌려준다.
ex) def positive(x):
    return x > 0
print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
결과값: [1, 2, 6]

[hex]
- 정수 값을 입력받아 16진수로 변환하여 돌려주는 함수이다.

[id]
- 객체를 입력받아 객체의 고유 주소 값(레퍼런스)를 돌려주는 함수이다.

[input([prompt])]
- 사용자 입력을 받는 함수
  ※ [ ] 기호는 괄호 안의 내용을 생략할 수 있다는 관례 표기법.
  
[int(x)]
- 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수
- int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 돌려준다.

[isinstance]
- isinstance(object, class)는 첫번째 인수로 인스턴스, 두번째 인수로 클래스 이름을 받는다.
  입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를  판단하여 참이면 True, 거짓이면 False를 돌려준다.
  
[map]
- map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다.
- 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수
ex) >>> def two_times(x): 
...     return x*2
...
>>> list(map(two_times, [1, 2, 3, 4]))
[2, 4, 6, 8]

[oct(x)]
- oct(x)는 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수

[open('filename','mode')]
- 파일이름과 읽기방법을 입력받아 파일 객체를 돌려주는 함수
- 읽기방법을 생략하면 기본값인 읽기 전용모드(r)로 파일 객체를 만들어 돌려준다.
- b는 w,r,a와 함께 사용하는데 b는 바이너리 모드이다.

[pow(x,y)]
- x의 y 제곱한 결과값을 돌려주는 함수

[range([start,] stop [,step])]
- for문과 함께 자주 사용하는 함수로 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어준다.
- 시작(start) 숫자를 지정해 주지 않으면 range 함수는 0부터 시작한다.
- 끝(stop) 숫자는 해당 범위에 포함되지 않는다.

[round(number [,ndigits])]
- 숫자(number)를 입력받아 반올림해 주는 함수.
- ndigits 는 반올림해서 해당 자릿수까지 보여준다는 의미이다.

[sorted(iterable)]
- 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수.
- list 자료형에도 sort함수가 있지만, 리스트 객체 그 자체를 정렬만 할 뿐 정렬된 결과를 돌려주지는 않는다.

[str(object)]
- 문자열 형태로 객체를 변환하여 돌려주는 함수.

[type(object)]
- 입력값의 자료형이 무엇인지 알려주는 함수.

[zip(*iterable)]
- 동일한 개수로 이루어진 자료형을 묶어주는 역할을 하는 함수.
ex) >>> list(zip([1, 2, 3], [4, 5, 6]))
[(1, 4), (2, 5), (3, 6)]
>>> list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
>>> list(zip("abc", "def"))
[('a', 'd'), ('b', 'e'), ('c', 'f')]

-----------------------------------------------------------------------------
<<< 라이브러리 >>>

[sys]
- 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈.
- sys.argv : 명령행에서 인수 전달하기
- sys.exit : 강제로 스크립트 종료
- sys.path : 자신이 만든 모듈 불러와 사용하기
- sys.path.append("모듈이 있는 경로") : 이렇게 추가하면 해당 경로에 있는 파이썬 모듈을 불러와서 사용가능.

[pickle]
- 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈.
- dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장할 수도 있다.

[os]
- OS 모듈은 환경변수나 디렉터리, 파일등의 OS 자원을 제어할 수 있게 해주는 모듈.
- 내 시스템의 환경변수값을 알고 싶을 때 : os.environ
- 디렉터리 위치 변경 : os.chdir("변경위치")
- 디렉터리 위치 돌려받기 : os.getcwd()
- 시스템 명령어 호출하기 : os.system("명령어")
- 실행한 시스템 명령어의 결과값 돌려받기 : os.popen("명령어")
  : 시스템 명령어를 실행한 결과값을 읽기 모드 형태의 파일 객체로 돌려준다.
- os.mkdir(디렉터리) : 디렉터리를 생성
- os.rmdir(디렉터리) : 디텍터리를 삭제. 단, 디첵터리가 비어있어야 삭제가능.
- os.unlink(파일) : 파일삭제
- os.rename(src, dst) : src라는 이름의 파일을 dst라는 이름으로 수정.

[shutil]
- 파일을 복사해 주는 파이썬 모듈.
ex) src라는 이름의 파일을 dst로 복사. 
만약 dst가 디렉터리 이름이면 src라는 파일이름으로 dst 디렉터리에 복사하고 동일한 이름이 있을 경우에는 덮어쓴다.
>>> import shutil
>>> shutil.copy("src.txt", "dst.txt")

[glob]
- 특정 디렉터리 안의 파일들을 읽어서 돌려준다.
- *, ? 등 메타 문자를 써서 원하는 파일만 읽어 들일 수도 있다.
>>> import glob
>>> glob.glob("c:/doit/mark*")
['c:/doit\\marks1.py', 'c:/doit\\marks2.py', 'c:/doit\\marks3.py']

[tempfile]
- 파일을 임시로 만들어서 사용할때 유용한 모듈
- tempfile.mkstemp() : 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다.
- tempfile.TemporaryFile() : 임시 저장공간으로 사용할 파일 객체를 돌려준다. 
  : 이 파일은 기본적으로 바이너리 쓰기모드(wb)를 갖는다. 
  : f.close()가 호출되면 이 파일 객체는 자동으로 사라진다.

[time]
time.time()
: 현재시간을 실수 형태로 돌려주는 함수이다.
: 1970년 1월1일 0시0분0초를 기준으로 시간을 초단위로 돌려준다.
time.localtime(time.time())
: time.time()이 돌려준 실수 값을 사용해서 연도,월,일,시,분,초 ...의 형태로 바꾸어주는 함수.
time.asctime()
: time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수.
time.ctime
: time.asctime(time.localtime(time.time())) 을 time.ctime() 을 사용해 간편하게 표시할 수 있다.
: ctime은 항상 현재 시간만을 돌려준다.
time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))
: 시간에 관계된 것을 세밀하게 표현하는 여러가지 포맷코드를 제공.
time.sleep(i)
: 주로 루프 안에서 많이 사용.
: 일정한 시간 간격을 두고 루프를 실행할 수 있다.

[calendar]
- 파이썬에서 달력을 볼 수 있게 해주는 모듈.
calendar.weekday(연,월,일) 
: 그 날짜에 해당하는 요일 정보를 돌려준다.
: 0이 월요일이다.
calendar.monthrange(연,월)
: 입력받은 달의 1일이 무슨 요일인지와 그 달이 며칠까지 있는지를 튜플 형태로 돌려준다.

[random]
: 난수(규칙이 없는 임의의 수)를 발생시키는 모듈.
random.choice(data)
: 입력으로 받은 리스트에서 무작위로 하나를 선택하여 돌려준다.

[webbrowser]
- 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈.
webbrowser.open("URL")
: 웹 브라우저가 이미 실행된 상태라면 입력 주소로 이동.
: 그렇지 않은 상태라면 새로 웹 브라우저를 실행한 후 해당 주소로 이동.

"""

print("[예제6]")
import time
import threading  # 스레드를 생성하기 위해서는 threading 모듈이 필요하다.

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)  # 스레드를 생성한다.
    threads.append(t)

for t in threads:
    t.start()  # 스레드를 실행한다.

for t in threads:
    t.join()  # join으로 스레드가 종료될때까지 기다린다.

print("End")
print()

print("[예제7]")
print()

print("[예제8]")
print()

print("[예제9]")
print()

print("[예제10]")
print()
