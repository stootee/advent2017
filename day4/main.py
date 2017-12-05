import passphrase

counter = 0

for row in passphrase.passphrases.split('\n'):
    row = row.split(' ')
    newlist = []
    oldlist = []

    for passphrase in row:
        pp = []
        for x in passphrase:
            pp.append(x)
            pp.sort()
        if pp not in newlist:
            newlist.append(pp)
    if len(newlist) == len(row):
        counter += 1

    print row
    print newlist

print counter