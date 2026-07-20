# Hashing Notes

## Dictionary
Stores data in Key → Value format.

Example
```python
d = {
    "apple": 3,
    "banana": 2
}

Average Complexity
Search : O(1)
Insert : O(1)
Delete : O(1)

## Set
Stores only unique elements.

Useful for
- Duplicate Detection
- Fast Search

## Frequency Count
Store the occurrence of every element.

Example
banana
↓
b → 1
a → 3
n → 2

## Character Mapping
Use two dictionaries.

Example
paper
↓
title
p → t
a → i
e → l
r → e

Reverse Mapping
t → p
i → a
l → e
e → r

## Complement Search
Example

Target = 9
Current = 2
Need = 7
Search 7 inside Hash Map.

## Grouping
Example

eat
↓
aet

tea
↓
aet

Both belong to the same group.