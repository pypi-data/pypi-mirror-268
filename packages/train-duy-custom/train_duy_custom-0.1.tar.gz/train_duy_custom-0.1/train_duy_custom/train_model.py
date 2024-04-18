from train import train
from utils import save_model
from process_data import create_data_generators
# Load data
def Train(path_data, image_size=(115,115), batch_size=32, epochs=20, path_model="model.hdf5"):
    train_ds, val_ds = create_data_generators(path_data=path_data, image_size=image_size, batch_size=batch_size)
    
    # Train model
    model = train(path=path_data, train_ds=train_ds, val_ds=val_ds, epochs=epochs)
    save_model(path_model, model)
    return model

