import random

def weighted_lottery(weights):
    container_list = []

    for (name, weight) in weights.items():
        for _ in range(weight):
            container_list.append(name)
        
    return random.choice(container_list)

my_mentor = {
        'Orc' : 5,
        'Human' : 5,
        'Elf': 5,
        'Dwarf': 5

}

print(weighted_lottery(my_mentor))