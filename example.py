import classifier
data = [[1,1,1], [2,2,2], [3,3,3]]
results = [1, 0, 0]
num1 = int(input("num1 =\n"))
num2 = int(input("num2 =\n"))
num3 = int(input("num3 =\n"))
closestamt, index = classifier.closest([num1, num2, num3], data)

print("closest is " + str(data[index]) + " dist of " + str(closestamt))
print("type is most likely " + str(results[index]))
