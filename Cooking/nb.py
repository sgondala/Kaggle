igc = {0:{'a':1.0,'b':2.0}, 1:{'a':3.0,'b':4.0}}
igcCount = {}
for i in range(2):
    igcCount[i] = 0.0
for i in range(2):
    for ingredient in igc[i]:
        igcCount[i] += igc[i][ingredient]
for i in igc:
    for j in igc[i]:
        igc[i][j] = igc[i][j]/igcCount[i]
tempSum = 0
for i in igc[0]:
    tempSum += igc[0][i]
print tempSum