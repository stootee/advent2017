target = 361527
#target = 49

centre = 1

corners = {
    1: {
        'seed': 2,
        'coords': [1, 1],
        'reposition': [0, -1],
        'level': 0,
        'value': centre
    },
    2: {
        'seed': 4,
        'coords': [1, -1],
        'reposition': [1, 0],
        'level': 0,
        'value': centre
    },
    3: {
        'seed': 6,
        'coords': [-1, -1],
        'reposition': [0, 1],
        'level': 0,
        'value': centre
    },
    4: {
        'seed': 8,
        'coords': [-1, 1],
        'reposition': [-1, 0],
        'level': 0,
        'value': centre
    }
}


def coordinate(list1, list2, func='m'):
    if func == 'm':
        return [_a * _b for _a, _b in zip(list1, list2)]
    if func == 'a':
        return [_a + _b for _a, _b in zip(list1, list2)]

level = 0
corner_found = None
exact_corner = False
current_value = centre
while current_value <= target:
    level += 1
    for corner in range(1, 5):
        corners[corner]['value'] += corners[corner]['seed'] + ((level - 1) * 8)
        current_value = corners[corner]['value']
        corners[corner]['level'] = level
        if corners[corner]['value'] >= target:
            corner_found = corner
            break

print corners
print "corner %s :" % corner_found, "level %s :" % level, "value %s" % corners[corner_found]['value']

if corner_found == 1:
    previous_corner = 4
else:
    previous_corner = corner_found - 1

distance_from_corner = corners[corner_found]['value'] - target

reposition = coordinate([distance_from_corner, distance_from_corner], corners[corner_found]['reposition'])
coords = coordinate([level, level], corners[corner_found]['coords'])

coords = coordinate(coords, reposition, 'a')

print reposition, coords
print distance_from_corner, coords

print abs(coords[0]) + abs(coords[1])
