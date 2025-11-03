numbers = list(range(1, 101))
filtered_numbers = [n for n in numbers if not (n%2 != 0 and n%3 == 0)]
print(filtered_numbers)
print(len(filtered_numbers))