from input import scanners
#from input import testscanners as scanners

def scannerpos1(rng, stp):
    rng -= 1

    if rng == -1:
        return False
    elif rng == 0:
        return True
    elif stp / (rng * 2.0) == stp / (rng * 2):
        return True
    else:
        return False

wait = 0

# for x in range(wait, 10 + wait):
#     print x

while 1 == 1:
    if (wait * 1.0) / 100000 == wait / 100000:
        print wait

    severity = 0
    for step in range(wait, max(scanners.keys()) + wait + 1):
        pos = step - wait

        try:
            aa = scanners[pos]
        except:
            aa = 0

        if scannerpos1(aa, step):
            severity += (step * aa)

    if severity == 0:
        print("wait: %s, severity: %s" % (wait, severity))
        break
    else:
        wait += 1
