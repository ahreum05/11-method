def add(start=1, end=100):
    total = 0
    for i in range(start, end + 1):
        total += i
    return total

print(' 1~100사이의 합 : ', add())
print('30~100사이의 합 : ', add(30))
print('20~200사이의 합 : ', add(20,200))
print('20~200사이의 합 : ', add(start=20,end=200))