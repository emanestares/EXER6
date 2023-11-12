# Author : Frederick Emmanuel S. Estares
# Date : October 16, 2023
# Description : Exercise 6 - Linear Classification using Perceptron

from prettytable import PrettyTable

# checks if all feature vectors are equal
# if yes, return true, false if not
def didConverge(rowsList, weight, length):
    converged = True

    if len(rowsList) == 1:
        return False

    for row in rowsList[1:-1]:
        if row[length:length*2] != weight:
            converged = False
            break

    return converged 

# initializes all the variables 
a = 0
bias = 0
index = 0
learningRate = 0
threshold = 0
x0 = 0
x1 = 0
y = 0
z = []
noOfIterations = 1
weight = []
rowXXB = []
currentRowParam = []
tempList = []
tempRow = []
labelList = []
iterationList = []

# opens the input.txt file
fileP = open("input.txt", "r")

# iterates through the lines of the file
# assigns the values to the appropriate variables
for line in fileP:
    row = 0
    tempRow = []

    if index == 0:
        learningRate = float(line)
    elif index == 1:
        threshold = float(line)
    elif index == 2:
        bias = int(line)
    else:
        row = line.split(" ")
        
        z.append(int(row[len(row)-1]))

        for num in row[0:len(row)-1]:
            tempRow.append(int(num))
        tempRow.append(bias)

        rowXXB.append(tempRow)
    
    index += 1
fileP.close()

# creates a list for the label of the table
# based on the number of feature vectors
index = 0
for ind in range(0, len(row)):
    weight.append(0)
    if ind == len(row)-1:
        labelList.append("b")
    else:
        labelList.append("x"+str(ind))

for ind in range(0, len(row)):
    if ind == len(row)-1:
        labelList.append("wb")
    else:
        labelList.append("w"+str(ind))

labelList += ["a", "y", "z"]

# creates / overwrites the file for output
fileOutput = open("output.txt", "w")

# repeatedly performs the algorithm for perceptron
# until the vectors converges
# if non converging, repeats up to 1500 iterations.
# then prompts the user.
while(True):
    print("\nIteration ", noOfIterations, ":")
    fileOutput.write("\nIteration " + str(noOfIterations) + ":\n")
    index = 0
    iterationList = []
    table = PrettyTable()
    table.field_names = labelList

    while(True):
        tempList = []
        currentRowParam = rowXXB[index]
        tempList+= currentRowParam
        tempList += weight
        a = 0

        for ind in range(0, len(weight)):
            a += currentRowParam[ind]*weight[ind]

        if a >= threshold:
            y = 1
        else:
            y = 0

        tempList+=[a, y, z[index]]
        
        for ind in range(0, len(weight)):
            weight[ind] = (weight[ind] + learningRate*currentRowParam[ind]*(z[index]-y))

        index+=1

        iterationList.append(tempList)

        if index == len(rowXXB):
            break

    # writes the table on both output.txt and terminal
    noOfIterations += 1
    table.add_rows(iterationList)
    print(table)
    fileOutput.write(table.get_string())

    if didConverge(iterationList, weight, len(weight)):
        print(str(noOfIterations-1), "iterations final weight: ", weight)
        fileOutput.write("\n" + str(noOfIterations-1) +  " iterations final weight: " + str(weight))
        break
    
    if noOfIterations > 1500:
        print("Non Converging")
        break

fileOutput.close()