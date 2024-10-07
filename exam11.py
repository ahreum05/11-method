# 일반 함수
def square1(x) : 
    return x**2

def test() : 
    print('test')    
    
print(square1(5))
test()
print('-' * 20)

# 람다 함수 1
square2 = lambda x : x**2
test2 = lambda : print('test2')

print(square2(5))
test2()
print('-' * 20)

# 람다 함수 2
print((lambda x : x**2)(5))
(lambda : print('test2'))()
print('-' * 20)

# 사용예
lst1 = [(lambda x: x**2)(a) for a in range(5)]
print(lst1)







