def doubleNum(a,b):
    return a%b==0

a = int(input("정수 입력 : "))
b = int(input("정수 입력 : "))

if doubleNum(a,b):
    print("%d(은)는 %d의 배수입니다."%(a,b))
else:
    print("%d(은)는 %d의 배수가 아닙니다."%(a,b))
    
