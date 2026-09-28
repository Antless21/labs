# main.py
from my_module import sum_numbers, gcd_simple, count_vowels, gcd_euclid


print(sum_numbers(10))
print(gcd_simple(48, 18))
print(gcd_simple(17, 5))
print(count_vowels("Привет, мир!"))
print(count_vowels("Hello World"))
print(gcd_euclid(48, 18))
print(gcd_euclid(17, 5))
print(gcd_simple(1071, 462) == gcd_euclid(1071, 462))