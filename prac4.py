# 입력 : 변수에 데이터 저장하기
def menu():
    print('*'*20)
    print('1.입고')
    print('2.출고')
    print('3.목록')
    print('4.종료')
    print('*'*20)
    num = int(input('번호 입력 :'))
    return num

def in_goods():
    sang = {}
    sang['name'] = input('품명 : ')
    sang['count'] = int(input('수량 : '))
    sang['price'] = int(input('단가 : '))
    sang['tot'] = compute(sang['count'], sang['price'])
    
    list1.append(sang)
    print('입력되었습니다.')

# 재고 - 수량 >= 0  ->  재고 >= 수량
def out_goods():
    inname = input('품명 : ')
    incount = int(input('수량 : '))
    search_result = False    # True : 있음, False : 없음
    
    for item in list1:
        if inname == item['name']:          # 품명 확인
            search_result = True
            if item['count'] >= incount :   # 재고 확인
                item['count'] -= incount
                item['tot'] = compute(item['count'], item['price'])
                print('출고되었습니다.')
                break
            else:
                print('재고 수량이 부족합니다')
                break 
    
    if not search_result : print(inname, "상품이 없습니다.")

# 연산 : 저장된 데이터 가공하기
def compute(count, price):
    return count * price

# 출력 : 저장된 데이터 확인
def output_list():
    print('{:<4s}\t {:<5s}\t {:<5s}\t {:<10s}'
          .format('품명','수량', '단가', '총액'))
    for item in list1:
        print('{name:<4s}\t {count:<5d}\t {price:<5d}\t {tot:<10d}'
              .format(**item))


# 선언 : 변수 만들기
list1 = []   # 전체 상품 저장

# controller : 전체 제어
while True:
    num = menu()
    print()
    
    if num == 1:
        in_goods()
    elif num == 2:
        out_goods()
    elif num == 3:
        output_list()
    elif num == 4:
        print('프로그램을 종료합니다')
        break
    
    print()
