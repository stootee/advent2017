input = "10	3	15	10	5	15	5	15	9	2	5	8	5	2	3	6"
#input = "0\t2\t7\t0"

input = input.split('\t')

print input

for x in range(0, len(input)):
    input[x] = int(input[x])

redistribute = [input]

foundlist = []
counter = 0

while 1 == 1:
    counter += 1
    _rd = redistribute[counter - 1]
    _val = max(_rd)
    _pos = _rd.index(_val)
    _newlist = list(_rd)
    _newlist[_pos] = 0

    for x in range(0, _val):

        if _pos < len(_newlist) - 1:
            _pos += 1
        else:
            _pos = 0

        _newlist[_pos] += 1

    if counter < 10:
        print (counter, _newlist)

    if (counter * 1.0) / 10000 == counter / 10000:
        print (counter)

    if _newlist in redistribute:
        if not foundlist:
            print("Found!! Steps:", counter, _newlist)
            foundlist.append(_newlist)
            _f = counter
        elif foundlist[0] == _newlist:
            print("Found twice!! Steps:", counter, counter - _f, _newlist)
            break
    elif counter > 100000000:
        print ("Gone a bit too far for my liking")
        break

    redistribute.append(_newlist)


