'''
int plus(int a, int b) {
    return a + b;
}
double plus(int a, double b) {
    return a + b;
}
double plus(double a, int b) {
    return a + b;
}
double plus(double a, double b) {
    return a + b;
}
'''
def plus(a, b) :
    return a+b

def minus(a, b) :
    return a-b

print("100 + 200 = %s" %plus(100, 200))
print("10 - 20 = %s" %minus(10, 20))

print("100.5 + 200.7 = %s" %plus(100.5, 200.7))
print("10.5 - 20.7 = %s" %minus(10.5, 20.7))