print("[문제1]")
a = 'a:b:c:d'
temp = a.split(':')
print("#".join(temp))
print()

# print("[문제2]")
# def dictionaryEx(i):
#     a = {'A':90, 'B':80}
#     print(a.get(i, 70))
# dictionaryEx(input())
# print()

print("[문제3]")
print("+ 는 주소값이 변하고, extend는 주소값이 변하지 않는다")
print()

print("[문제4]")
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
result = 0
for number in A:
    if number >= 50:
        result += number
print(result)
print()

# print("[문제5]")
# def fibo(i):
#     if i == 0: return 0
#     if i == 1: return 1
#     return fibo(i-2) + fibo(i-1)
# for n in range(int(input())):
#     print(fibo(n))
# print()

# print("[문제6]")
# a = input()
# b = a.split(',')
# print(b)
# result = 0
# for num in b:
#     result += int(num)
# print(result)
# print()

# print("[문제7]")
# num = input("구구단을 출력할 숫자를 입력하세요(2~9): ")
# dan = int(num)
# for i in range(1,10):
#     print(dan*i, end=' ')
# print()

# print("[문제8]")
# f = open('abc.txt', 'w')
# data = """AAA
# BBB
# CCC
# DDD
# EEE"""
# f.write(data)
# f.close()
# f = open('abc.txt', 'r')
# lines = f.readlines()
# f.close()
# lines.reverse()
# f = open('abc.txt', 'w')
# for line in lines:
#     line = line.strip()
#     f.write(line)
#     f.write('\n')
# f.close()
# print()

print("[문제9]")
f = open('sample.txt', 'w')
data = """70
60
55
75
95
90
80
80
85
100"""
f.write(data)
f.close()
f = open('sample.txt', 'r')
lines = f.readlines()
f.close()
sum = 0
avg = 0
count = 0
for line in lines:
    line = line.strip()
    count += 1
    sum += int(line)
avg = sum/count
f = open('result.txt', 'w')
f.write(str(avg))
f.close()

print()

print("[문제10]")
print()

print("[문제11]")
print()

print("[문제12]")
print()

print("[문제13]")
print()

print("[문제14]")
print()

print("[문제15]")
print()

print("[문제16]")
print()

print("[문제17]")
print()

print("[문제18]")
print()

print("[문제19]")
print()

print("[문제20]")
print()