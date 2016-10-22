
# coding: utf-8

# In[1]:

import json


# In[2]:

train = json.load(open("train.json"))


# In[3]:

def sum(a):
    retVal = 0.0
    for i in a:
        retVal += a[i]
    return retVal


# In[4]:

cuisineMap = {} #Contains cuisine sum, not prob
cuisineIndex = {}
cuisineCount = 0


# In[5]:

for i in train:
    cuisine = i['cuisine']
    if cuisine in cuisineMap:
        cuisineMap[cuisine] += 1.0
    else:
        cuisineMap[cuisine] = 1.0
        cuisineIndex[cuisine] = cuisineCount
        cuisineCount += 1


# In[6]:

cuisineSum = 0
for i in cuisineMap:
    cuisineSum += cuisineMap[i]


# In[7]:

for i in cuisineMap:
    cuisineMap[i] /= cuisineSum




# In[9]:

ingredientMap = {} #Contains sum, not prob
ingredientSum = 0


# In[10]:

for i in train:
    for j in i['ingredients']:
        ingredientSum += 1.0
        if j in ingredientMap:
            ingredientMap[j] += 1.0
        else:
            ingredientMap[j] = 1.0


# In[11]:

for i in ingredientMap:
    ingredientMap[i] /= ingredientSum


# In[13]:

igc = {}
for i in range(20):
    igc[i] = {}




# In[15]:

for i in train:
    cuisine = i['cuisine']
    index = cuisineIndex[cuisine]
    ingredientList = i['ingredients']
    for ingredient in ingredientList:
        if ingredient in igc[index]:
            igc[index][ingredient] += 1.0
        else:
            igc[index][ingredient] = 1.0



# In[17]:

igcCount = {}
for i in range(20):
    igcCount[i] = 0.0


# In[18]:

for i in range(20):
    for ingredient in igc[i]:
        igcCount[i] += igc[i][ingredient]




# In[20]:

for i in igc:
    for j in igc[i]:
        igc[i][j] = igc[i][j]/igcCount[i]



# In[22]:

### Preprocess done, now the main process


# In[23]:

test = json.load(open("test.json"))


# In[24]:

def findProb(ingredients, cuisine):
    index = cuisineIndex[cuisine]
    returnVal = 1.0
    returnVal *= cuisineMap[cuisine]
    for ingredient in ingredients:
        if ingredient in igc[index]:
            returnVal *= igc[index][ingredient]/ingredientMap[ingredient]
        else:
            return 0
    return returnVal


# In[25]:

def findMax(ingredients):
    maxValue = 0.0
    cuisineSelected = 'greek'
    for cuisine in cuisineMap:
#         print cuisine
        probOfThisCuisine = findProb(ingredients,cuisine) 
        if probOfThisCuisine > maxValue:
            maxValue = probOfThisCuisine
            cuisineSelected = cuisine
    return cuisineSelected

print("id,cuisine")
for i in test:
    # a.append(findMax(i['ingredients']))
    print(str(i['id'])+ ',' +str(findMax(i['ingredients'])))    
