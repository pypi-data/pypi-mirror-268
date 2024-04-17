import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def create_class_indices_dict(data_dir):
    class_indices = {}
    classes = sorted(os.listdir(data_dir))
    for i, class_name in enumerate(classes):
        class_indices[class_name] = i
    return class_indices
def predictor(img, model, data_dir):
    img_path = os.path.abspath(img)
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, (224, 224))
    image = np.array(image, dtype = 'float32')/255.0
    plt.imshow(image)
    image = image.reshape(1, 224,224,3)
    # label_names = train_ds.class_indices
    label_names = create_class_indices_dict(data_dir)
    dict_class = dict(zip(list(range(len(label_names))), label_names))
    clas = model.predict(image).argmax()
    name = dict_class[clas]
    print('The given image is of \nClass: {0} \nSpecies: {1}'.format(clas, name))