def calc_area(radius) :
    global area   # 전역변수 area를 사용하겠다는 선언
    area = 3.15 * radius** 2
    
area = 50  # 전역변수
r = float(input('원의 반지름 : '))
calc_area(r)
print('원의 넓이 :', area)

##############################
dict1 = {}

def ex() :
    dict1['name'] = '홍길동'   # 전역변수
