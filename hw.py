def misterio1():
    x = 0
    while True:
        y = int(input('valor m1: '))
        if y < 0: break
        x += y
        print(f'x {x}')
    return x

def misterio2():
    x = 0
    while True:
        y = int(input('valor m2: '))
        if y < 0: continue
        x += y
        print(f'x {x}')
    return x

a = misterio1()
b = misterio2()
print(a,b)