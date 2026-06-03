def find_min(a, b, c):
    if a <= b and a <= c:
        print(f"Найменше число: {a}")
    elif b <= a and b <= c:
        print(f"Найменше число: {b}")
    else:
        print(f"Найменше число: {c}")

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))

find_min(a, b, c)