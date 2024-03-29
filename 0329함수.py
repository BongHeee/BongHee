def calculate_y(a,b,t):

    result = a**2 * x + b

    return result

a = float(input(f'a 값 입력:'))
b = float(input(f'b 값 입력:'))
t = int(input(f'x의 최대값 입력:'))

x = 0

while x <= t:
    y = calculate_y(a,b,x)
    print(f"x = {x}, y = {y}")
    x += 1
