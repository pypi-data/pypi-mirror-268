import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import cv2
import numpy as np
from tqdm import tqdm
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
import seaborn as sns

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import BatchNormalization, Input, Lambda, Dense, Flatten, Activation, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras import applications

def train(path:str, train_ds, val_ds, epochs, use_gpu=True):
    if use_gpu and tf.test.is_gpu_available():
        print("GPU device is available")
        device = '/gpu:0'  
    else:
        print("GPU device is not available or not requested, falling back to CPU")
        device = '/cpu:0'  
    with tf.device(device):
        no_labels = sum(1 for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)))
        vgg_base = applications.VGG16(weights = 'imagenet', include_top = False, input_shape = (115, 115, 3))
        vgg_base.trainable = False
        inputs = Input(shape=(115, 115, 3))

        x = vgg_base(inputs, training=False)
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dense(1024, activation = 'relu')(x)
        x = layers.Dropout(0.5)(x)
        outputs = layers.Dense(no_labels, activation = 'sigmoid')(x)
        vgg_model = Model(inputs, outputs)
        vgg_model.summary()
        vgg_model.compile(
            optimizer=keras.optimizers.Adam(),
            loss= keras.losses.CategoricalCrossentropy(from_logits = True),
            metrics= [keras.metrics.CategoricalAccuracy()],
        )
        early_stopping = EarlyStopping(monitor='val_loss', patience=4, restore_best_weights=True)
        vgg_model.fit(train_ds, epochs=epochs, validation_data=val_ds, callbacks=[early_stopping])
        return vgg_model

class PyDataset(tf.data.Dataset):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
def save_model(path, model):
    #hdf5
    abs_path = os.path.abspath(path)
    model.save(abs_path)