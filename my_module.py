def sum_numbers(num):
    total = 0
    for i in range(1, num + 1, 2):
        total += i
    return total

def gcd_simple(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Числа должны быть натуральными")
    for d in range(min(a, b), 0, -1):
        if a % d == 0 and b % d == 0:
            return d
def count_vowels(text):
    vowels = "аеёиоуыэюяaeiou"
    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1
    return count