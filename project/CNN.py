import numpy as np
import pickle
import nibabel as nib
import csv
import os
import glob
from keras import layers
from keras import models
from keras import optimizers
from random import shuffle, randint, seed
np.random.seed(10)
seed(10)

# Import metadata to know who is a PD patient
with open('final_collection_11_28_2017.csv','r') as f:
	metadata = csv.reader(f)
	metadata_dict = {row[1]:row[2] for row in metadata}
	del metadata_dict['Subject']

# Get list of all image files and divide them into training and validation sets
fileList = glob.glob('./ep2d/**/*_ep2d_RESTING_STATE_*.nii',recursive=True)
shuffle(fileList)
nSubjects = len(fileList)
trainingRatio = 0.8
training_fileList = fileList[:int(nSubjects*trainingRatio)]
validation_fileList = fileList[int(nSubjects*trainingRatio):]
ntraining = len(training_fileList)
nvalidation = len(validation_fileList)

# Used for loading image files into the model one at a time
def training_data_gen():
	while True:
		for f in training_fileList:
			patientID = f[7:11]
			img = nib.load(f)
			img = img.get_data()
			img = np.array(img)
			shp0,shp1,shp2,shp3 = img.shape
			# Put the time channel together with the depth channel
			img = np.reshape(img,(1,shp0,shp1,shp2*shp3))
			# Label each subject
			if metadata_dict[patientID] == "PD":
				label = 1
			elif metadata_dict[patientID] == "Control":
				label = 0
			else:
				print("No metadata for patient")
				raise ValueError()

			yield (img,np.array([label]))

# Same but for the validation set
def validation_data_gen():
        while True:
                for f in validation_fileList:
                	patientID = f[7:11]
                	img = nib.load(f)
                	img = img.get_data()
                	img = np.array(img)
                	shp0,shp1,shp2,shp3 = img.shape
                	img = np.reshape(img,(1,shp0,shp1,shp2*shp3))
                	if metadata_dict[patientID] == "PD":
                        	label = 1
                	elif metadata_dict[patientID] == "Control":
                        	label = 0
                	else:
                        	print("No metadata for patient")
                        	raise ValueError()

                	yield (img,np.array([label]))


# Neural network definition
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu',
                        input_shape=(68, 66, 40*210), batch_size=1))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(128, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.summary()

model.compile(loss='binary_crossentropy',
              optimizer=optimizers.RMSprop(lr=1e-4),
              metrics=['acc'])

train_gen = training_data_gen()
val_gen = validation_data_gen()
history = model.fit_generator(
      train_gen,
      steps_per_epoch=ntraining, validation_data=val_gen, validation_steps=nvalidation, epochs=10)

# save the model and history for later visualization
model.save('model_10_epoch2.h5')
with open('./trainHistoryDict', 'wb') as file_pi:
        pickle.dump(history.history, file_pi)
