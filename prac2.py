def grade(avg) :
    if avg >= 90 and avg <= 100 : return 'A'
    elif avg >= 80 and avg < 90 : return 'B'
    elif avg >= 70 and avg < 80 : return 'C'
    elif avg >= 60 and avg < 70 : return 'D'
    elif avg >= 0 and avg < 60 : return 'F'

kor = int(input('국어 점수 입력 : '))
eng = int(input('영어 점수 입력 : '))

tot = kor + eng
avg = tot / 2

print(grade(avg), '학점입니다.')