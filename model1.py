import tensorflow as tf
import cv2
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
import matplotlib.pyplot as plt
import pickle
import os
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.optimizers import RMSprop

train = ImageDataGenerator(rescale=1/255)
train_dataset = train.flow_from_directory('D:/Malek/Projects/stage/Croping images/cropped/', target_size= (200,200),
                                           batch_size = 3,
                                           class_mode = 'binary')

validation_dataset = train.flow_from_directory('D:/Malek/Projects/stage/Croping images/cropped/', target_size= (200,200),
                                           batch_size = 3,
                                           class_mode = 'binary')
train_dataset.class_indices

model = tf.keras.models.Sequential([tf.keras.layers.Conv2D(16,(3,3),actvation = 'relu', input_shape = (200,200,3)),
                                    tf.keras.layers.MaxPool2D(2,2),
                                    tf.keras.layers.Conv2D(32,(3,3),actvation = 'relu'),
                                    tf.keras.layers.MaxPool2D(2,2),
                                    tf.keras.layers.Conv2D(64,(3,3),actvation = 'relu'),
                                    tf.keras.layers.MaxPool2D(2,2),
                                    tf.keras.layers.Flatten(),
                                    tf.keras.layers.Conv2D(512, (3, 3), actvation='relu'),
                                    tf.keras.layers.Dense(1, activation='sigmoid')
                                    ])