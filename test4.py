test_string = "rishabhs"

half_idx = len(test_string) // 2

res = test_string[:half_idx] + test_string[half_idx:].upper()

print("output = ", res)