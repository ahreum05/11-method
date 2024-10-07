print((lambda x, y, z : x + 2*y + 5*z)(1, 2, 3))

f = lambda x, y, z : x + 2*y + 5*z
print(f(1, 2, 3))
print('-' * 20)

# 람다함수는 다른 함수의 매개변수로 전달할 수 있다.
def test(ff) :
    print(ff(1, 2, 3))

test(f)

