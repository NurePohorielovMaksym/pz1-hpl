def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

number = int(input("Введіть число: "))

if is_prime(number):
    print(f"{number} — просте число")
else:
    print(f"{number} — не просте число")