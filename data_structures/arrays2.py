max = int(input(" enter a number:"))

odd_numbers = []

for i in range(0, max):
    if i % 2 == 1:
        odd_numbers.append(i)

print("odd number in the range of 0 to:", {max}, odd_numbers )