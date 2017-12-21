from stream import stream as stream
import json

chars = []
for x in stream:
    if x not in chars:
        chars.append(x)

for x in range(33, 126):
    if chr(x) not in chars:
        escapechar = chr(x)
        break

cleanstream = ""
escaped = False
for x in range(0, len(stream)):
    if not escaped:
        cleanstream += stream[x]
    else:
        cleanstream += escapechar

    if stream[x] == "!" and not escaped:
        escaped = True
    else:
        escaped = False

cleanstream2 = ""
garbagechars = ""
garbage = False
for x in cleanstream:
    if x == '>':
        garbage = False

    if not garbage:
        cleanstream2 += x
    else:
        garbagechars += x

    if x == '<':
        garbage = True

print stream
print cleanstream
print cleanstream2
# cleanstream2 = cleanstream2.replace(',<>,', '')
# cleanstream2 = cleanstream2.replace(',<>', '')
# cleanstream2 = cleanstream2.replace('<>,', '')
print cleanstream2.replace(',', '').replace('<', '').replace('>', '')

runningsum = 0
score = 0
cleanstream3 = ""
for x in cleanstream2.replace(',', '').replace('<', '').replace('>', ''):
    if x == '{':
        score += 1
        cleanstream3 += x + str(score)
        runningsum += score
    if x == '}':
        score -= 1
        cleanstream3 += x

print score
print runningsum
print cleanstream3
print garbagechars
print len(garbagechars.replace('!#', ''))



