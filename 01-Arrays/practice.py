# Creating an Array (Python List)

arr = [10, 20, 30, 40, 50]
print(arr)

# -----------------------------

# Accessing Elements O(1)

print(arr[0])
print(arr[2])

# -----------------------------

# Updating Elements O(1)

arr[2] = 99
print(arr)

# -----------------------------

# Traversing O(n)

for num in arr:
    print(num)

# -----------------------------

# Searching O(n)

target = 40

for i in range(len(arr)):
    if arr[i] == target:
        print(f"Found at index {i}")
        break

# -----------------------------

# Insertion O(n)

arr.insert(2, 25)
print(arr)

# -----------------------------

# Append   Amortized(1)

arr.append(60) 
print(arr)

# -----------------------------

# Deletion O(1)

arr.pop()
print(arr)

arr.remove(25)   #O(n)
print(arr)