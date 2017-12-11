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

root = list(set(tower.keys()) - set(child_parent.keys()))
root = root[0]
print root


balance = {}
for x in tower:
    weights = []
    for y in tower[x]['children']:
        weights.append((y, tower[y]['weight']))

    if weights:
        balance[x] = weights

print balance
print tower


for x in balance.iteritems():
    print x

tower2 = {}
prog = root
layer = 0
platform = 0
tower2[str(layer) + ':' + str(platform)] = [(prog, tower[prog]['weight'])]
children = balance[prog]

while layer < 1000:
    layer += 1
    for x, prog in enumerate(children):
        tower2[str(layer) + ':' + str(x)] = [(prog, tower[prog]['weight'])]

print tower2





#print (root, tower[root]['weight'])


