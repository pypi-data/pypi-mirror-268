import numpy as np
import pandas as pd

from datetime import datetime
from tqdm import tqdm
from typing import Union

from hygeoclas.utils.numeric import dct

class DataCompressor:
    def __init__(self, M: int, *lists: Union[tuple, list]):
        self.M = M
        self.lists = lists

    def process_supervised(self, recordList: np.array, label: str) -> None:
        for record in tqdm(recordList, desc=f"Performing compression of {label} datasets", unit=" dataset"):
            if len(record) < self.M:
                continue
            else:
                coefficients = dct(record, self.M)

                data = {"Label": label}
                for m in range(1, self.M+1):
                    data[f"Coefficient {m}"] = coefficients[m-1]
                dataFrame = pd.DataFrame(data, index=[0])

                self.database = pd.concat([self.database, dataFrame], ignore_index=True)

    def process_unsupervised(self, recordList: np.array) -> None:
        self.listOfCompressedRecordIndexes = []
        for i, record in enumerate(tqdm(recordList, desc="Performing compression of datasets", unit=" dataset")):
            if len(record) < self.M:
                continue
            else:
                self.listOfCompressedRecordIndexes.append(i)
                coefficients = dct(record, self.M)

                data = {}
                for m in range(1, self.M+1):
                    data[f"Coefficient {m}"] = coefficients[m-1]
                dataFrame = pd.DataFrame(data, index=[0])

                self.database = pd.concat([self.database, dataFrame], ignore_index=True)

    def execute(self) -> pd.DataFrame:
        if all(isinstance(item, tuple) for item in self.lists):
            columns = ["Label"] + [f"Coefficient {m}" for m in range(1, self.M+1)]
            self.database = pd.DataFrame(columns=columns)

            for recordList, label in self.lists:
                self.process_supervised(recordList, label)

        elif all(isinstance(item, list) for item in self.lists):
            columns = [f"Coefficient {m}" for m in range(1, self.M+1)]
            self.database = pd.DataFrame(columns=columns)

            for recordList in self.lists:
                self.process_unsupervised(recordList)
        else:
            raise TypeError("Lists were entered with and without labels.")
        
        return self.database
        
    def save(self, savePath: str, threshold: int) -> None:
        dati = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        self.database.to_csv(f"{savePath}Database P{threshold} q{self.M} {dati}.csv", index=False, encoding="utf-8-sig")