dogs = [9, 45, 42, 39, 28, 25, 20, 18, 50]
dogs[dogs.index(max(dogs))], dogs[dogs.index(min(dogs))] = dogs[dogs.index(min(dogs))], dogs[dogs.index(max(dogs))]
print(dogs)