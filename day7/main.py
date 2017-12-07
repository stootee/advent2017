import tower as ti


def kids(program, children):
    pass


tower = {}

for x in ti.towerinput.split('\n'):
    tower[x[:x.find(' ')]] = {
        'weight': int(x[x.find('(') + 1: x.find(')')]),
    }
    childmarker = x.find('->')
    if childmarker > 0:
        tower[x[:x.find(' ')]]['children'] = (x[x.find('->') + 3:]).split(', ')
    else:
        tower[x[:x.find(' ')]]['children'] = []

child_parent = {}
for prog in tower:
    for x in tower[prog]['children']:
        child_parent[x] = prog

print list(set(tower.keys()) - set(child_parent.keys()))
