import pandas as pd
import numpy as np 
from pathlib import Path
import os
import sys
import joblib

# # Adding the below path to avoid module not found error
PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

# # Then perform import
from prediction_model.config import config  
from prediction_model.processing.data_handling import load_dataset,save_pipeline,separate_data,split_data
import prediction_model.processing.preprocessing as pp 
import prediction_model.pipeline as pipe 
import sys

def perform_training():
    dataset = load_dataset(config.FILE_NAME)
    print("Colums after loading",dataset.columns)
    X,y = separate_data(dataset)
    print("Separate data cols: ",X.columns)
    y = y.replace(0, np.nan)
    y = np.log(y)
    y = y.replace(np.nan, 0)
    #y = y.apply(lambda x: 1 if x.strip() == "Approved" else 0)
    X_train,X_test,y_train,y_test = split_data(X,y)
    test_data = X_test.copy()
    test_data[config.TARGET] = y_test
    test_data.to_csv(os.path.join(config.DATAPATH,config.TEST_FILE))
    print("X train shape",X_train.columns)
    print("Y train shape",y_train.shape)
    pipe.temp_max_pred_pipeline.fit(X_train,y_train)
    save_pipeline(pipe.temp_max_pred_pipeline)



if __name__=='__main__':
    perform_training()