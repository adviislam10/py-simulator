import random

print("Mario Kart Mystery Box Simulator")

# Input
number = int(input("Number of times you want to simulate:"))
number = int(number)

# Process
banana = 0
greenShell = 0
star = 0
goldenMushroom = 0

for i in range(number):
    if random.random() <= 0.45:
        banana += 1
    elif random.random() <= 0.80:
        greenShell += 1
    elif random.random() <= 0.95:
        star += 1
    elif random.random() <= 99:
        goldenMushroom += 1

# Output
print("# of Bananas:", banana)
print("# of Green Shells:", greenShell)
print("# of Stars:", star)
print("# of Golden Mushrooms:", goldenMushroom)
