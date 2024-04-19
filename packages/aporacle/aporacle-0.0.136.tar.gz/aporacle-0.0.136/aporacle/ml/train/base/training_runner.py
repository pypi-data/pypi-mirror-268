import logging
import pickle
import uuid
from typing import Optional, List

import numpy as np
import pandas as pd
import pendulum
from komoutils.core import KomoBase
from komoutils.core.time import the_time_in_iso_now_is
from pydantic import BaseModel
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split


def get_rmse(y_test, y_pred):
    rmse = np.sqrt(np.mean((y_test - y_pred) ** 2))
    # print(y_test-y_pred)
    return rmse


def get_r2(y_test, y_pred):
    r2 = 1 - (np.sum((y_test - y_pred) ** 2) / np.sum((y_test - y_test.mean()) ** 2))
    return r2


class ModelResult(BaseModel):
    executor_id: str
    chain: str
    tso: str
    label: str
    target: list
    rmse: float
    r2: float
    model: bytes
    model_version: str
    model_type: str
    parameters: dict
    features: list
    symbols: list
    data_size: int
    time: str


class TrainingRunner(KomoBase):
    def __init__(self, feed: str, input_data: pd.DataFrame, symbols: list, target: str):
        self.feed: Optional[str] = feed
        self.input_data: pd.DataFrame = input_data
        self.symbols: Optional[list] = symbols
        self.target: Optional[str] = target

        self.X = None
        self.y = None
        self.X_train = self.X_test = self.y_train = self.y_test = None
        self.train_size = 0.8
        self.name: str = None
        self.key = uuid.uuid4().hex
        self.executor_id = None

        self.results: list = []

    def _preprocess_inputs(self):
        try:
            # Train-test split
            X_train, X_test, y_train, y_test = train_test_split(self.X,
                                                                self.y,
                                                                train_size=self.train_size,
                                                                shuffle=True,
                                                                random_state=1)

            return X_train, X_test, y_train, y_test
        except Exception as e:
            self.log_with_clock(log_level=logging.ERROR, msg=f"Error during input processing. {e}")
            return None, None, None, None

    def _train(self, alpha: float = 0.1):
        try:
            self.name = 'ridge'
            self.executor_id = f"{self.feed}_{self.key}_{self.target}"
            parameters = {
                'alpha': alpha,
            }
            model = Ridge(alpha=parameters['alpha'])

            model.fit(self.X_train, self.y_train)
            y_pred = model.predict(self.X_test)
            y_test = self.y_test.to_numpy().reshape(1, -1)

            r2 = get_r2(y_test, y_pred)
            rmse = get_rmse(y_test, y_pred)

            chain = "combined"
            model_file_name = f"model_{self.key}_{self.target}_{self.name}".lower()

            pickled_model = pickle.dumps(model)
            result = {
                "executor_id": self.executor_id,
                "chain": chain,
                "asset": self.feed,
                "label": model_file_name,
                "target": self.target,
                "rmse": rmse,
                "r2": r2,
                "model": pickled_model,
                "model_version": f"{chain}_{pendulum.now().timestamp()}",
                "model_type": self.name,
                "parameters": parameters,
                "features": self.X.columns.to_list(),
                "symbols": sorted(self.symbols),
                "data_size": len(self.X),
                "time": the_time_in_iso_now_is()
            }

            self.results.append(ModelResult(**result))

        except Exception as e:
            self.log_with_clock(log_level=logging.ERROR, msg=f"Error during training. {e}")
            return None

    def run(self, alphas: list) -> List[ModelResult]:
        # unpack columns looking for 'features' and 'target' tags.
        columns_names = self.input_data.columns.to_list()
        features = [col for col in columns_names if 'features' in col.lower()]
        target = [col for col in columns_names if 'target' in col.lower()]

        self.X = self.input_data[features].sort_index(axis=0)
        self.y = self.input_data[target]

        self.symbols = self.symbols

        for alpha in alphas:
            self._train(alpha=alpha)

        return self.results
