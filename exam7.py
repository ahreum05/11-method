# *변수명 : 매개변수는 튜플로서 동작함
def total(*args) :
    #print(args)
    #print(type(args))
    return sum(args)

print(total())
print(total(2))
print(total(20, 30))
print(total(10, 20, 30))
print(total(10, 20, 30, 40))
print(total(10, 20, 30, 50, 60))

