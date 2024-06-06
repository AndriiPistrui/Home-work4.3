import random


random_length = random.randint(3, 10)
random_list = [random.randint(1, 100) for _ in range(random_length)]


new_list = [random_list[0], random_list[2], random_list[-2]]

print("Початковий список:", random_list)
print("Новий список:", new_list)
