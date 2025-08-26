import random

seed = []
counter1 = 0

while counter1 < 5:
    for number in range(5):
        if number not in seed:
            seed.append(random.randint(1, 1001))
            counter1 += 1
        else:
            pass

print(seed)

not_sorted = True

while not_sorted:
    counter2 = 0
    for number in range(5):
        try:
            if seed[number] > seed[number + 1]:
                counter2 += 1
                container1 = seed[number]
                container2 = seed[number + 1]
                seed[number] = container2
                seed[number + 1] = container1
        except IndexError:
            if counter2 > 0:
                counter2 = 0
            elif counter2 == 0:
                not_sorted = False

print(seed)