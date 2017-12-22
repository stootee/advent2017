input = "147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70"
#input = "3,4,1,5"
#input = "AoC 2017"

extra_lengths = [17, 31, 73, 47, 23]

input_ascii = []
for x in input:
    input_ascii.append(ord(x))
input_ascii += extra_lengths

#print input_ascii

lengths = []
for x in input.split(','):
    try:
        lengths.append(int(x))
    except:
        pass


def element_generator(rng=256):
    elements = []
    for _x in range(0, rng):
        elements.append(_x)

    return elements


def bitwisexor(lst=[]):
    _lst = []
    for _x in lst:
        _lst.append(str(_x))
    _a = '^'.join(_lst)

    return "%0.2x" % eval(_a)


def knot_hash(_lengths, _elements, pointer=0, skip=0):

    for length in _lengths:
        subset = []
        for y in range(0, length):
            subset.append(_elements[(pointer + y) % len(_elements)])

        for z, element in enumerate(list(reversed(subset))):
            _elements[(pointer + z) % len(_elements)] = element

        pointer += (skip + length)
        pointer = pointer % len(_elements)

        skip += 1

        #print _elements, pointer, skip

    return _elements, pointer, skip

# part 1
a, ptr, skp = knot_hash(lengths, element_generator())
print("part1"), (a[0] * a[1]), (skp)


# part 2
ptr = skp = 0
a = element_generator()
for x in range(0, 64):
    a, ptr, skp = knot_hash(input_ascii, a, ptr, skp)

hashed_input = ""
for x in range(0, 16):
    hashed_input += bitwisexor(a[x * 16:(x + 1) * 16])

print hashed_input
