import h5py
import os
import numpy as np
# from wandb import magic
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras import models, layers, callbacks

EPOCHS = 8
MODEL_FILE = 'AITNetwork.keras'
PATIENCE = int(EPOCHS * .2)

# Load data from H5 file
with h5py.File(os.path.join('data', 'final_numpy_data.h5'), 'r') as h5_file:
    images = h5_file['images'][:]
    labels_str = h5_file['labels'][:]

# Convert string labels to one-hot encoded vectors
label_encoder = LabelEncoder()
labels_encoded = label_encoder.fit_transform(labels_str)
labels_one_hot = np.eye(len(np.unique(labels_encoded)))[labels_encoded]

# Split the data into training and testing sets
training_images, testing_images, training_labels, testing_labels = train_test_split(
    images, labels_one_hot, test_size=0.2, random_state=42)
training_images, testing_images = training_images / 255, testing_images / 255  # Scales values to be between 0-1

# The labels that the neural network can identify given an image
class_names = label_encoder.classes_

# Model layers
model = models.Sequential()

# Convolutional layers
model.add(layers.Reshape((80, 190, 1), input_shape=(80, 190)))
model.add(layers.Conv2D(32, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D(2, 2))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D(2, 2))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

# Flatten layer
model.add(layers.Flatten())

# Dense layers
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(len(class_names), activation='softmax'))  # Number of classifications

# Define loss function and metric
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# call backs to stop training when val_loss is low enough and val_accuracy is high
es = callbacks.EarlyStopping(monitor='val_loss', mode='min', verbose=1, patience=PATIENCE)
mc = callbacks.ModelCheckpoint(MODEL_FILE, monitor='val_accuracy', mode='max', verbose=1, save_best_only=True)

# Training the model
model.fit(training_images, training_labels, epochs=EPOCHS, validation_data=(testing_images, testing_labels), callbacks=[es, mc])

# Retrieve final loss and accuracy values for the trained neural network
loss, accuracy = model.evaluate(testing_images, testing_labels)
print(f"Loss: {loss}  Accuracy: {accuracy}")