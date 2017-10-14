full = False

donations = []
full_load = 45

toys = ['robot', 'doll', 'ball', 'slinky']

while not full:
    for toy in toys:
        donations.append(toy)
        size = len(donations)
        if (size >= full_load):
            full = True
  
print('Full with', len(donations), 'toys')
print(donations)
