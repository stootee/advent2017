import tower as ti

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

print tower