

def cStructToBitStreamFormat(struct):
    noTypeDef = struct.split('{')[1].lstrip()
    structCore, structTail = noTypeDef.split('}')
    structName = structTail.lstrip().split(';')[0]
    structCore = structCore.splitlines()
    structCore = [x.lstrip().replace('unsigned int', 'uint')
                  for x in structCore]

    BitSFmtList = []
    for sCore in structCore:
        if ':' in sCore:
            typee, name, length = sCore.split()
        else:
            typee, name = sCore.split()
            length = ''

        BitSFmtList.append((typee + length, name))

    return structName, BitSFmtList


def isThatType(typee, entry):
    (t, _) = entry
    return (typee in t)


def replaceType(struct, fmtList):
    structName = struct['name']
    new_fmtList = []
    for fmt in fmtList:
        if isThatType(structName, fmt):
            new_fmtList.extend(struct['fmt'])
        else:
            new_fmtList.append(fmt)
    return new_fmtList


def replaceAll(allParstStructs):
    for oStruct in allParstStructs:
        for inStruct in allParstStructs:
            inStruct['fmt'] = replaceType( oStruct, inStruct['fmt'])


with open('preppadeDevLog.h') as f:
    l = f.read()

l = l.split('typedef ')
l = [s for s in l if "struct" in s]

allParstStructs = []
for i in l:
    name, fmt = cStructToBitStreamFormat(i)
    allParstStructs.append({'name': name, 'fmt': fmt})

print [i["name"] for i in allParstStructs]


#print isThatType(allParstStructs[0]['name'], allParstStructs[4]['fmt'][18])
new_fmt = replaceType(allParstStructs[0], allParstStructs[4]['fmt'])
#print allParstStructs[4]['fmt']
#print
#print new_fmt
    # print structCore, structName

    #notUINT = [s for s in structCore if not "unsigned int" in s]
    # print notUINT
a = 7
print 
for i in allParstStructs[a:(a+1)]:
    print i['name']
    print i['fmt']
    print ''

replaceAll(allParstStructs)
for i in allParstStructs[a:a+1]:
    print i['name']
    print i['fmt'][:]
    print ''

# splitlines()
