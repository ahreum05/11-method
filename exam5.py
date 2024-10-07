def total(start, end) :
    tot = 0
    for i in range(start, end+1) :
        tot += i
        
    return tot

# 함수명은 가급적 내장함수와 이름이 중복되는 것은 피하는 것이 좋음
print(total(1, 10))
print(sum([1, 2, 3, 4, 5]))

