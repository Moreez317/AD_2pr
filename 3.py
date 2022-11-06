import numpy as np

matrixArray = np.random.rand(3, 3)

finalArray = []

for i in range(len(matrixArray)):
    for a in range(len(matrixArray[i])):
        finalArray.append(matrixArray[i][a])

print(matrixArray)
print(finalArray)