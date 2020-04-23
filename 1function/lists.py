from array import array
from sys import getsizeof

manual_list_number = [0, 1, 2, 3, 4]
dynamic_list_numbers = list(range(5))
string_list = list("Hello World")

print(manual_list_number)
print(dynamic_list_numbers)
print(string_list)


string_list_replace = list("Hello World")
string_list_replace[0] = "replace"
print(string_list_replace)


numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]
print(f"{first} {second} {third}")

first, second, third = numbers
print(f"{first} {second} {third}")

first, *other = numbers
print(f"{first} {other}")

first, *other, third = numbers
print(f"{first} {other} {third}")


get_index_with_item = ["a", "b", "c"]
for index, item in enumerate(get_index_with_item):
    print(index, item)


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12)
]
lamdba_items = items


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)


lamdba_items.sort(key=lambda item: item[1])
print(lamdba_items)


# use arrays if performance issue 10k items and want to enforce typeing
array_nums = array("i", [1, 2, 3])
print(array_nums)


# set remove duplicates
numbers_one = [1, 2, 3, 4, 4]
first = set(numbers_one)
second = {1, 5}
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)


# generator object good for looping of large list that can be calculated. Much smaller memory
values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))
values = [x * 2 for x in range(100000)]
print("gen:", getsizeof(values))


# Unpacking basically make list into indivdual items
unpack = [1, 2, 3]
print(unpack, *unpack)

first = {"x": 1}
second = {"x": 10, "y": 1}
combined = {**first, **second, "z": 1}
print(combined)
