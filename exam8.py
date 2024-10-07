def sumAndMul(a, b) :
    tot = a + b
    mul = a * b
    return tot, mul  # 리턴값이 여러개 일 경우
                     # 튜플로 리턴한다.
# 튜플로 사용
result = sumAndMul(5, 7) 
print(result)
print(type(result))
# 인덱싱 사용
print(result[0])
print(result[1])
print('-' * 20)

# unpacking 사용
tot, mul = sumAndMul(5, 7)
print(tot)
print(mul)
print('-' * 20)