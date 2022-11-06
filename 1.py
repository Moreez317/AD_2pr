print("Type first number: ")

firstNum = int(input())
numBuffer = []
numBuffer.append(firstNum)

def consoleInput(res):
    while res != 0:
        buff = int(input())
        numBuffer.append(buff)
        res = res + buff
    return 'true'

sqrtBuff = 0

if consoleInput(firstNum) == 'true':
    for items in range(len(numBuffer)):
        sqrtBuff = numBuffer[items] * numBuffer[items]

print(sqrtBuff)