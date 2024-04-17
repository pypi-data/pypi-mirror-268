import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from utils.process_data import create_data_generators
from utils.train import train, save_model
from utils.predict import predictor
PATH_DATA = "data"
train_ds,val_ds = create_data_generators(PATH_DATA)
model = train(path=PATH_DATA, train_ds=train_ds, val_ds=val_ds)
save_model(path="model.hdf5", model=model)
predictor(img="data/cats/cat.1.jpg", model=model, data_dir=PATH_DATA)
