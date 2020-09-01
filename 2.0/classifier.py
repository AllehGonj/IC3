import random 
import imageio
import numpy as np

from PIL import Image 
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier 

def saveImage(path, name, image):
    imageio.imwrite(path + name, image)

def readImage(name):
    image = Image.open(name).convert("L") 
    return np.array(image.getdata(), np.uint8).reshape(-1, 64)

def saveAsUniqueImage(path, image, target):
    target = str(target)
    extension = '.png'
    name = target + extension
    saveImage(path, name, image)

def saveDataSet(path, dataset):
    for i, image in enumerate(dataset.images):
        target = dataset.target[i]
        saveAsUniqueImage(path, image, target)

def shape_data(data):
    n_samples = len(data)
    return data.reshape((n_samples, -1))

def loadDataset(data):
    sample_index = random.sample(range(len(data)),len(data)//5) 
    valid_index = [i for i in range(len(data)) if i not in sample_index] 
    return sample_index, valid_index

def loadTestData(x, sample_index, valid_index):
    sample_images = [x[i] for i in sample_index] 
    valid_images = [x[i] for i in valid_index]
    return sample_images, valid_images

def loadTestTarget(y, sample_index, valid_index):
    sample_target = [y[i] for i in sample_index] 
    valid_target = [y[i] for i in valid_index]
    return sample_target, valid_target

def train_classifer(data, target):
    classifier = RandomForestClassifier()
    classifier.fit(data, target)  
    return classifier
    
def calculate_score(classifier, data, target):
        return classifier.score(data, target)

def predict(classifier, data):
    return classifier.predict(data)

digits_path = 'digits/'
digits_dataset = datasets.load_digits()

# Saving Sklearn hand-written digits, if already stored comment the line below
# saveDataSet(digits_path, digits_dataset)

# Loading data from Sklearn dataset
data = shape_data(digits_dataset.images)
target = digits_dataset.target

# Generating random data from dataset for model training
sample_index, valid_index = loadDataset(data)
sample_images, valid_images = loadTestData(data, sample_index, valid_index)
sample_target, valid_target = loadTestTarget(target, sample_index, valid_index)

# Training classifier and Score calculating
classifier = train_classifer(sample_images, sample_target)
score = calculate_score(classifier, valid_images, valid_target)

# Read image selection and print model prediction
name = input('\nWhat digit do you want to verify? Please review the `digits` folder. \nEnter only the digit: ')
image = readImage(digits_path  + name + '.png')
prediction = predict(classifier, image)

print('\nRESULTS', end = '\n\n')
print('Score: ' + str('%.3f' % (score * 100)) + '%')
print('Prediction: ' + str(prediction[0]))