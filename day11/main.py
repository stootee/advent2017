from path_input import path


directions = {
    'n': (0, -1),
    'ne': (1, -1),
    'se': (1, 0),
    's': (0, 1),
    'sw': (-1, 1),
    'nw': (-1, 0)
}


x = 0
y = 0
distance = []
for move in path.split(','):
    x += directions[move][0]
    y += directions[move][1]

    distance.append(abs(x))
    distance.append(abs(y))

#part1
print max(abs(x), abs(y))

#part2
print max(distance)
