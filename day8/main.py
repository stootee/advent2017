from input import jumps

instructions = []
registers = {}
for x in jumps.split('\n'):
    y = x.split(" ")
    instructions.append(y)
    registers[y[0]] = 0

print instructions

regvals = []

for register, inc, val, _if, regif, condif, valif in instructions:
    val = int(val)
    if inc == 'dec':
        val *= -1

    condition = " ".join([str(registers[regif]), condif, valif])

    if eval(condition):
        try:
            registers[register] += val
            regvals.append(registers[register])
        except Exception, ex:
            print register, inc, val, _if, regif, condif, valif
            print condition
            print ex


print max(registers.values())
print max(regvals)





