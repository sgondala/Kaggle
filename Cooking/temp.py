import json
import NN
import numpy as np
import pandas as pd


trainData = json.load(open("train.json", 'r'))
cuisineMap = {}
cuisineInverseMap = {}
cuisineCount = 0
ingredientMap = {}
ingredientCount = 0

for data in trainData:
    if data["cuisine"] not in cuisineMap:
        cuisineMap[data['cuisine']] = cuisineCount
        cuisineInverseMap[cuisineCount] = cuisineMap[data['cuisine']]
        cuisineCount = cuisineCount + 1

    for ingredient in data["ingredients"]:
        if ingredient not in ingredientMap:
            ingredientMap[ingredient] = ingredientCount
            ingredientCount = ingredientCount + 1 

df = pd.read_json('train.json')

def makeInput(l):
    a = np.zeros((ingredientCount))
    for ingredient in l:
        a[ingredientMap[ingredient]] = 1
    return a

def makeOutput(cuisine):
    a=np.zeros((cuisineCount))
    a[cuisineMap[cuisine]] = 1
    return a

firstLayerLength = ingredientCount + 1
lastLayerLength = cuisineCount + 1

nn = NN.neuralNetwork(3,firstLayerLength,lastLayerLength)

for i in range(100):
    if i%100==0:
        print i
    nn.forwardPropagation(np.matrix(makeInput(df['ingredients'][i])).getT())
    nn.backPropagation(np.matrix(makeOutput(df['cuisine'][i])).getT())
    nn.changeTheta()

testdf = pd.read_json('test.json')

for i in range(len(testdf)):
    resultVal = nn.forwardPropagation(np.matrix(makeInput(testdf['ingredients'][i])).getT())
    indexOfMax = np.argmax(resultVal)
    print testdf['id'][i], cuisineInverseMap[indexOfMax]