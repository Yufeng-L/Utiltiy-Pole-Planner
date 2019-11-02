#Copyright2019 Yufeng Lin yflin@bu.edu
from __future__ import absolute_import, division, print_function, unicode_literals
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import numpy as np
import matplotlib.pyplot as plt

#set size
batch_size = 64
epochs = 30
IMG_HEIGHT = 150
IMG_WIDTH = 150

PATH = '/Users/linyufeng/desktop/dataset'
#set path for dataset
train_PATH = os.path.join(PATH,'train')#'/Users/linyufeng/desktop/'
validation_PATH = os.path.join(PATH,'validation')#'/Users/linyufeng/desktop/electricpole'

#poles and validation set 

train_poles_dir = os.path.join(train_PATH,'poles')
validation_poles_dir = os.path.join(validation_PATH,'poles')

#Nopole and validation set
train_nopole_dir =os.path.join(train_PATH,'nopoles')
validatioin_nopole_dir = os.path.join(validation_PATH,'nopoles')



#calculate number of traning
num_poles_tr = len(os.listdir(train_poles_dir))
num_poles_val = len(os.listdir(validation_poles_dir))

num_nopole_tr = len(os.listdir(train_nopole_dir))
num_nopole_val = len(os.listdir(validatioin_nopole_dir))

total_train = num_poles_tr + num_nopole_tr
total_val = num_poles_val + num_nopole_val


print('Total training poles imges: ',total_train)
print('Total validation poles images: ',total_val)
print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

train_image_generator = ImageDataGenerator(rescale=1./255,rotation_range=45,width_shift_range=0.2,height_shift_range=0.2,shear_range=0.2,
                                  zoom_range=0.5,
                                  horizontal_flip=True) # Generator for our training data
validation_image_generator = ImageDataGenerator(rescale=1./255) # Generator for our validation data

train_data_gen = train_image_generator.flow_from_directory(directory=train_PATH,
                                                           batch_size=batch_size,
                                                           # directory=train_dir,
                                                           shuffle=True,
                                                           target_size=(IMG_HEIGHT, IMG_WIDTH),                           
                                                           class_mode='binary')

val_data_gen = validation_image_generator.flow_from_directory(directory=validation_PATH,
                                                              batch_size=batch_size,
                                                              # directory=validation_dir,
                                                              target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                              class_mode='binary')

#visualize training images

# sample_training_images, _ = next(train_data_gen)

# This function will plot images in the form of a grid with 1 row and 5 columns where images are placed in each column.
# def plotImages(images_arr):
#     fig, axes = plt.subplots(1, 5, figsize=(20,20))
#     axes = axes.flatten()
#     for img, ax in zip( images_arr, axes):
#         ax.imshow(img)
#         ax.axis('off')
#     plt.tight_layout()
#     plt.show()


# plotImages(sample_training_images[:5])

#create model

model = Sequential([
    Conv2D(16, (3,3), activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH ,3)),
    MaxPooling2D(2,2),
    Conv2D(32, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D(2,2),
    Conv2D(128, (3,3),activation='relu'),
    MaxPooling2D(2,2),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(1, activation='sigmoid')
])

#compile the model
model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999, amsgrad=False),
              loss ='binary_crossentropy',
              metrics =['accuracy'])

model.summary()
#train the model
history = model.fit_generator(
    train_data_gen,
    steps_per_epoch=total_train // batch_size,
    epochs= epochs,
    validation_data=val_data_gen,
    validation_steps=total_val // batch_size
)

#visualize training results

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(epochs)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training Accuracy')
plt.plot(epochs_range, val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()



