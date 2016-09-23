import json
import NN
import numpy as np
import pandas as pd 


trainData = json.load(open("train.json", 'r'))
cuisineMap = {}
cuisineCount = 0
ingredientMap = {}
ingredientCount = 0
for data in trainData:
    if data["cuisine"] not in cuisineMap:
        cuisineMap[data['cuisine']] = cuisineCount
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

for i in range(len(df)):
    if i%100==0:
        print i
    nn.forwardPropagation(np.matrix(makeInput(df['ingredients'][0])).getT())
    #print "Forward done"
    nn.backPropagation(np.matrix(makeOutput(df['cuisine'][0])).getT())
    #print "Backward done"
    nn.changeTheta()



"""
a = np.matrix(np.zeros((6715,1)))
b = np.matrix(np.zeros((1,6715)))
c = a*b
print c.shape
"""


# for i in range(6500):
# 	for j in range(6500):
# 		a = 1
