def math(w,x,y):
    if w == 'add':
        z = x + y
    elif w == 'div':
        z = x / y
    elif w == 'multi':
        z = x * y
    elif w == 'sub':
        z = x - y
    elif w == 'power':
        z = x ** y
    return round(z, 2)

w = str(input('specify the operator to formulate: ')).lower()
x = float(input('enter first number to calculate: '))
y = float(input('enter second for instance: '))
print(math(w, x, y))