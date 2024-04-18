import os
import cv2
import numpy as np
from tqdm import tqdm
from sklearn.utils import shuffle


from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

def dataset(path): #put path till the highest directory level
    train = list(os.walk(path))
    label_names = train[0][1]
    dict_labels = dict(zip(label_names, list(range(len(label_names)))))
    images = []
    labels = []
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']  # Add more extensions if needed

    for folder in tqdm(os.listdir(path)):
        value_of_label = dict_labels[folder] # dict_labels is the dictionary whose key:value pairs are classes:numbers representing them

        for file in os.listdir(os.path.join(path, folder)):
            if any(file.lower().endswith(ext) for ext in image_extensions):
                path_of_file = os.path.join(os.path.join(path, folder), file)

                image = cv2.imread(path_of_file)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = cv2.resize(image, (150, 150))
                images.append(image)
                labels.append(value_of_label)

    images = np.array(images, dtype='float32') / 255.0
    labels = np.array(labels)

    return images, labels

def create_data_generators(path_data, image_size=(115, 115), batch_size=32):
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.4,
        zoom_range=0.4,
        horizontal_flip=True,
        vertical_flip=True,
        validation_split=0.2
    )

    train_ds = train_datagen.flow_from_directory(
        path_data,
        target_size=image_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='training',
        color_mode="rgb"
    )

    val_ds = train_datagen.flow_from_directory(
        path_data,
        target_size=image_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation',
        color_mode="rgb"
    )

    return train_ds, val_ds
def show_images(train_ds):
    fig, ax = plt.subplots(nrows=1, ncols=5, figsize=(15,15))

    for i in range(5):
        image = next(train_ds)[0][0]
        image = np.squeeze(image)
        ax[i].imshow(image)
        ax[i].axis(False)