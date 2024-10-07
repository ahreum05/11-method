def star(n) :
    for i in range(n) :
        print('*', end='')
    print()
    
star(1)
star(2)

# 피라미드 탑
def pyramid(n) :
    for i in range(n):
        print(' ' * (n - i + 1), end='')  # 공백문자 출력
        for j in range(2 * i + 1):    # 별문자 출력
            print('*', end='')
        print()  # 1줄 넘김

pyramid(5) # 5층 피라미드탑 출력하기
pyramid(7) # 7층 피라미드탑 출력하기  



    