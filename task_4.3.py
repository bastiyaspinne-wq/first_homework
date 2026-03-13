import random
count = random.randint(3,10)
mini_list = []
for i in range(count):
    mini_list.append(random.randint(1,100))
print(mini_list)
final_list = [mini_list[0], mini_list[2], mini_list[-2]]
print(final_list)


