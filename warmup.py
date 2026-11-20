def greet_player(name):
    print(f"Welcome to the hunt, {name}.")

greet_player("Jordan")
greet_player("Priya")

import math

def pizzas_needed(people, slices_each, slices_per_pizza):
    total_slices = people * slices_each
    return math.ceil(total_slices / slices_per_pizza)

print(pizzas_needed(12, 3, 8))

print(pizzas_needed(8, 3, 12))
print(pizzas_needed(slices_per_pizza=8, people=12, slices_each=3))