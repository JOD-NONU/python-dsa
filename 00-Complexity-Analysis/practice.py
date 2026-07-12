# O(1)--->
x = 5
print(x)

# O(n)--->
n = 5
for i in range(n):
    print(i)

# O(n²)--->
for i in range(n):
    for j in range(n):
        print(i, j)


# O(log n)--->
i = n

while i > 1:
    i //= 2
    print(i)


# O(n) Time | O(1) Space--->
arr = [1, 2, 3, 4, 5]

total = 0

for num in arr:
    total += num

print(total)


# O(n) Time | O(n) Space--->
new_arr = []

for num in arr:
    new_arr.append(num * 2)

print(new_arr)