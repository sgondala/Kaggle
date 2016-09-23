import numpy as np
import math

class neuralNetwork:
    numberOfLayers = 0 #Input neurons are counted as one layer
    lengthOfFirstLayer = 0 #Including bias
    lengthOfLastLayer = 0 #Including bias
    learningRate = 0.1
    activationVals = {}
    thetaVals = {}
    delVals = {}
    
    def __init__(self,numberOfLayers, lengthOfFirstLayer, lengthOfLastLayer):
        self.numberOfLayers = numberOfLayers
        self.lengthOfFirstLayer = lengthOfFirstLayer
        self.lengthOfLastLayer = lengthOfLastLayer
        self.learningRate = 0.1
        self.initializeTheta()
        self.initializeActivation()

    def initializeTheta(self): #Should put random numbers between -1 and 1
        for i in range(1,self.numberOfLayers-1):
            self.thetaVals[i] = np.matrix(np.random.randn(self.lengthOfFirstLayer, self.lengthOfFirstLayer))
        self.thetaVals[self.numberOfLayers-1] = np.matrix(np.random.randn(self.lengthOfLastLayer, self.lengthOfFirstLayer))

    def initializeActivation(self):
        for i in range(1,self.numberOfLayers):
            self.activationVals[i] = np.matrix(np.zeros((self.lengthOfFirstLayer,1)))
        self.activationVals[self.numberOfLayers] = np.matrix(np.zeros((self.lengthOfLastLayer,1)))
    
    def g(self, product):
        try:
            result = 1/(1+math.exp(-product))
            return result
        except OverflowError:
            if product < 0:
                return 0.0000001
            else:
                return 0.9999999
        
    def printVals(self):
        print self.numberOfLayers, self.lengthOfFirstLayer, self.lengthOfLastLayer
        print self.thetaVals
        print self.activationVals
    
    #Input is a matrix of single column
    def softmax(self,x):
        assert(x.shape[1] == 1)
        returnVal = x.getT().getA()[0] #Getting the array
        returnVal = np.exp(returnVal) / np.sum(np.exp(returnVal), axis=0)
        returnVal = np.matrix(returnVal).getT()
        return returnVal
    
    # Mostly working
    # Can use vectorize - came to know about it later
    def forwardPropagation(self, features): #Features includes no bias
        assert(features.shape[1]==1)
        self.activationVals[1] = np.append(np.zeros((1,1)),features,axis=0) #Added bias
        self.activationVals[1][0] = 1
        assert(self.activationVals[1].shape[0] == features.shape[0] + 1)
        assert(self.activationVals[1].shape[1] == 1)
        
        for layer in range(2, self.numberOfLayers + 1):
            self.activationVals[layer] = self.thetaVals[layer-1] * self.activationVals[layer-1]
            self.activationVals[layer][0] = 1
            numberOfNeurons = self.lengthOfFirstLayer
            if layer == self.numberOfLayers:
                numberOfNeurons = self.lengthOfLastLayer
            for neuronNumber in range(1, numberOfNeurons):
                self.activationVals[layer][neuronNumber] = self.g(self.activationVals[layer][neuronNumber])
        
        updateVal = self.softmax(self.activationVals[self.numberOfLayers][1:,0])
        self.activationVals[self.numberOfLayers] = np.append(np.zeros((1,1)),updateVal,axis=0)

    #Ran forwardProp algo separately before
    def backPropagation(self, expectedResult):
        expectedResultWithBias = np.append(np.zeros((1,1)),expectedResult,axis=0)
        # expectedResultWithBias[0] = 1
        resultGot = self.activationVals[self.numberOfLayers]
        assert(expectedResultWithBias.shape == resultGot.shape)
        self.delVals[self.numberOfLayers] = self.activationVals[self.numberOfLayers] - expectedResultWithBias
        assert(self.delVals[self.numberOfLayers][0] == 0)
        for layer in list(reversed(range(2,self.numberOfLayers))):
            derivativeTerm = np.multiply(self.activationVals[layer], 1 - self.activationVals[layer])
            nonDerivativeTerm = self.thetaVals[layer].getT()*self.delVals[layer+1]
            self.delVals[layer] = np.multiply(nonDerivativeTerm, derivativeTerm)
            assert(self.delVals[layer][0] == 0)

    def changeTheta(self):
        for layer in range(1,self.numberOfLayers):
            activationValsTranspose = self.activationVals[layer].getT()
            DelMatrix = self.delVals[layer+1]*activationValsTranspose
            DelMatrix = self.learningRate*DelMatrix
            assert(self.thetaVals[layer].shape==DelMatrix.shape) 
            self.thetaVals[layer] = self.thetaVals[layer] - DelMatrix



"""        
    def changeTheta(self):
        for layer in range(1,self.numberOfLayers-1): #If 3 layers, we have to do only 1
            for i in range(self.lengthOfFirstLayer):
                for j in range(self.lengthOfFirstLayer):
                    self.thetaVals[layer][i,j] = self.thetaVals[layer][i,j] - self.learningRate*self.activationVals[layer][j]*self.delVals[layer+1][i]
        layer = self.numberOfLayers-1
        for i in range(self.lengthOfLastLayer):
            for j in range(self.lengthOfFirstLayer):
                self.thetaVals[layer][i,j] = self.thetaVals[layer][i,j] - self.learningRate*self.activationVals[layer][j]*self.delVals[layer+1][i]


a = neuralNetwork(3,4,3)
features = np.matrix([1,1,1]).getT()
a.forwardPropagation(features)
b = np.matrix([[1],[0]])
a.backPropagation(b)
a.changeTheta()
a.thetaVals
"""
