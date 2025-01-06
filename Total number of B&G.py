data = [
    {"name": "John", "gender": "boy", "age": 20},
    {"name": "Alice", "gender": "girl", "age": 14},
    {"name": "Tom", "gender": "boy", "age": 22},
    {"name": "Lucy", "gender": "girl", "age": 15},
    {"name": "Emma", "gender": "girl", "age": 16},
]
boys_count = 0
girls_count = 0
boys_above_18 = 0
girls_above_11 = 0
for person in data:
    if person["gender"] == "boy":
        boys_count += 1
        if person["age"] > 18:
            boys_above_18 += 1
    elif person["gender"] == "girl":
        girls_count += 1
        if person["age"] > 11:
            girls_above_11 += 1
print(f"Total Boys: {boys_count}")
print(f"Total Girls: {girls_count}")
print(f"Boys above 18: {boys_above_18}")
print(f"Girls above 11: {girls_above_11}")
