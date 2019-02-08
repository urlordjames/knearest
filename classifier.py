import math

def pyt(point1, point2):
    assert (len(point1) == len(point2)), "data size mismatch"
    dims = len(point1)
    stuffs = []
    total = 0
    for i in range(0, dims):
        val = point1[i]
        val2 = point2[i]
        val3 = val - val2
        stuffs.append(val3 ** 2)
    for i in range(0, len(stuffs)):
        total = total + stuffs[i]
    return math.sqrt(total)

def closest(numfrom, dataset):
    closestamt = 123456789
    index = 0
    for i in range(0, len(dataset)):
        amt = pyt(numfrom, dataset[i])
        if closestamt > amt:
            closestamt = amt
            index = i
    return closestamt, index
