currentNumber = 0
while currentNumber < 2**16:
    currentNumber += 1
    if currentNumber % 2 != 0:
        continue

    print(currentNumber)
