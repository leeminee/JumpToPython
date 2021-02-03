
print("=" * 50)
print("My Program")
print("=" * 50)

# 오른쪽 정렬
print("오른쪽 정렬")
print("{0:>10}" .format("hi"))
print()

# 왼쪽 정렬
print("왼쪽 정렬")
print("{0:<10}" .format("hi"))
print()

# 가운데 정렬
print("가운데 정렬")
print("{0:^10}" .format("hi"))
print()

# 공백 채우기 연습
print("공백 채우기")
print("{0:=^10}" .format("hi"))
print()

# f문자열 포매팅 (파이썬 3.6버전 부터 가능)
name = '홍길동'
age = 25
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'{"hi":=^10}')
print()

# find 와 index 의 차이 (위치를 찾을 때 사용)
a = "Python is the best choice"
# find 는 없는 글자를 찾을 때 -1 반환
print(a.find('k'))
# index 는 에러 반환
# print(a.index('k'))
print()

# 문자열 삽입 (join)
print(",".join('abcd'))
print(",".join(['a', 'b', 'c', 'd']))
print()

a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)
print()

# 리스트 확장 (extend or +=)
a = [1, 2, 3]
a.extend([4, 5])
print(a)
b = [6, 7]
a.extend(b)
print(a)
a += [8, 9]
print(a)
print()

"""
* 리스트와 튜플의 차이
- 리스트는 []으로 둘러싸지만 튜플은 ()으로 둘러싼다. 
- 리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
- 튜플은 ()를 생략해도 무방하다.
- 튜플은 단지 하나의 요소만을 가질 때에도 요소 뒤에 콤마(,)를 반드시 붙여야 한다.
"""

# 튜플 더하기
t1 = (1, 2, 'a', 'b')
t1 += (3, 4)
print(t1)

"""
[딕셔너리]
- Key와 Value를 한 쌍으로 갖는 파이썬의 자료형이다.
- Key를 통해 Value를 얻는다.
- {} 로 표현한다.
- Key는 중복이 X (중복이 된다면 하나를 제외한 나머지 Key는 모두 무시된다)
- 순차적이 아니라 index 가 없다.
- Key에 리스트 값이 변할 수 있기에 사용할 수 없다.(튜플은 가능)
"""

# 딕셔너리 쌍 추가
a = {1: 'a'}
a['abc'] = 'b'
print(a)
a[3] = [1, 2, 3]
print(a)
print()

# Key 리스트 만들기
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())
print()

for k in a.keys():
    print(k)
print()

print(list(a.keys()))
print()

print(a.values())
print()

# Key, Value 쌍 얻기
print(a.items())
print()

# Key가 딕셔너리 안에 있는지 조사하기
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print('name' in a)
print('email' in a)
print()


"""
[집합 자료형]
- 중복을 허용하지 않는다.
- 순서가 없어서 index 로 값을 얻을 수 없다.
"""

# 교집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)
print(s1.intersection(s2))
print()

# 합집합
print(s1 | s2)
print(s1.union(s2))
print()

# 차집합
print(s1 - s2)
print(s2.difference(s1))
print()

# 값 1개 추가
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

# 값 여러개 추가
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)
print()

"""
[불 자료형]
- 참(True)과 거짓(False)을 나타내는 자료형
- 첫문자를 항상 대문자로 사용해야 한다.
- 문자열, 리스트, 튜플, 딕셔너리 등의 값이 비어있으면 거짓.
- 0은 거짓, 1은 참이다.
"""

# 리스트 복사 방법 1 - a가 변하면 b도 변함. 즉 객체 동일
a = [1,2,3]
b = a
print(a is b)

# 리스트 복사 방법 2 - a가 변해도 b는 변하지않는다. 즉 객체가 다름
from copy import copy
b = copy(a)
print(b is a)