def is_valid(num, comparator):
    digits = list(str(num))
    return True if digits == sorted(digits) and len([d for d in digits if comparator(digits.count(d))]) else False

print("Part 1")
print(len([num for num in range(256310, 732736) if is_valid(num, lambda x: x>=2)]))

print("Part 2")
print(len([num for num in range(256310, 732736) if is_valid(num, lambda x: x==2)]))
