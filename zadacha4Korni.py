def root(a,b,c):
    D = b**2 - 4 * a * c
    if D < 0:
        print("Корней нет")
    elif D == 0:
        print(f'x1 = x2 = {-b / (2*a)}')
    else:
        print(f'x1 = {(-b-D**0.5) / (2*a)}')
        print(f'x2 = {(-b+D**0.5) / (2*a)}')

while True:
    print("Введите через пробел a b c")
    a = list(map(int,input().split()))
    root(a[0],a[1],a[2])