import map as mp

mp = mp.m.split('\n')

pos = 0
steps = 0
while pos >= 0 and pos <= len(mp):
    try:
        move = int(mp[pos])
    except:
        break

    inc = 1
    if int(mp[pos]) > 2:
        inc = -1

    mp[pos] = int(mp[pos]) + inc
    pos = pos + move
    steps += 1

print steps, pos