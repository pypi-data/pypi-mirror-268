import pickle
import numpy as np
import os
import asyncio
import aiofiles
import imblearn

class LEOID():
    """Level-based Ensemble for Overcoming Imbalanced Data"""

    def __init__(self):
        asyncio.run(self._load_models())

    async def _load_models(self):
        current_dir = os.path.dirname(__file__)
        stage_1_path = os.path.join(current_dir, "stage_1.pkl")
        stage_2_path = os.path.join(current_dir, "stage_2.pkl")
    
        async with aiofiles.open(stage_1_path, "rb") as f:
            model_1_data = await f.read()
            self.model_1 = pickle.loads(model_1_data)

        async with aiofiles.open(stage_2_path, "rb") as f:
            model_2_data = await f.read()
            self.model_2 = pickle.loads(model_2_data)

    def predict(self, X):
        X = np.array(X)
        if X.ndim == 1:
            X = X.reshape(1, -1)
            
        model_1_predictions = self.model_1.predict(X)
        predictions = []
        for index, model_1_prediction in enumerate(model_1_predictions):
            if model_1_prediction == 1:
                model_2_prediction = self.model_2.predict(X[index].reshape(1, -1))[0]
                if model_2_prediction == 1:
                    predictions.append(2)
                else:
                    predictions.append(1)
            else:
                predictions.append(model_1_prediction)
                
        return np.array(predictions)
