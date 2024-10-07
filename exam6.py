def inputNum(n) :
    for i in range(len(n)):
        n[i]=int(input('%s번째 숫자입력 : '%(i+1)))
        
def outputNum(n) :
    for i in range(len(n)):
        print(n[i], end=' ')

n = [0 for i in range(5)]
inputNum(n)
outputNum(n)

