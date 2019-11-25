import os
import pickle
import random

import numpy as np
import pandas as pd
import sklearn.model_selection as ms


class Predictor:
    '''Predictor serves as a class for generating predictions'''

    def __init__(self):
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        self.model = pickle.load(
            open(os.path.join(curr_dir, 'RF_model.pkl'), 'rb'))

    def predict_proba(self, data: pd.DataFrame):
        return self.model.predict_proba(data)

    def predict(self, **kwargs):
        data = {
            "hs_eng": [kwargs['eng']],
            "hs_math": [kwargs['math']],
            "hs_bio": [kwargs['bio']],
            "hs_chem": [kwargs['chem']],
            "hs_phy": [kwargs['phy']],
            "hs_econ": [kwargs['econ']],
            "hs_geo": [kwargs['geo']],
            "hs_soc": [kwargs['soc']],
            "hs_final": [kwargs['fin']],
            "major_name": [kwargs['major_name']]
        }
        data = pd.DataFrame(data)
        
        result = self.predict_proba(data)[:,0].tolist()[0]*100
            
        return result