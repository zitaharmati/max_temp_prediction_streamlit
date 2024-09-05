from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from pathlib import Path
import os
import sys

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config
import prediction_model.processing.preprocessing as pp 
from sklearn.ensemble import RandomForestRegressor
import numpy as np


temp_max_pred_pipeline = Pipeline(
    [
        #('DomainProcessing',pp.DomainProcessing(variable_to_add = config.FEATURE_TO_ADD)),
        #('DropFeatures', pp.DropColumns(variables_to_drop=config.DROP_FEATURES)),
        ('LabelEncoder',pp.CustomLabelEncoder(variables=config.CAT_FEATURES)),
        #('Standardscaler',StandardScaler(), config.NUM_FEATURES),
        #('LogTransform',pp.LogTransforms(variables=config.LOG_FEATURES)),
        ('Randomforestregressor',RandomForestRegressor(n_estimators=200, max_depth=30,max_leaf_nodes=100,random_state=0))
    ]
)