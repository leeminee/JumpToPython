
print("[예제1]")
result = 0
for n in range(1,1000):
    if n % 3 == 0 or n % 5 == 0:
        result += n
print(result)
print()

print("[예제2]")
totalPage = 0
def getTotalPage(m, n):
    if m % n != 0:
        totalPage = int(m/n) +1
    else:
        totalPage = int(m/n)
    return totalPage
print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(25,10))
print(getTotalPage(30,10))
print()

