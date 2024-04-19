import numpy as np
import pandas as pd
import torch

from pickle import load
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from torch.nn import Module

from hygeoclas.utils.numeric import Equal

def reset_weights(module: Module) -> None:
    """
    Resets the weights of a given PyTorch module.

    If the module has a method called 'reset_parameters', it resets its parameters using that method.
    If the module is a Fire1D layer, it recursively resets the weights of its child modules.

    Args:
        module (torch.nn.Module): The PyTorch module whose weights are to be reset.
    """
    if hasattr(module, "reset_parameters"):
        module.reset_parameters()
    else:
        for child in module.children():
            reset_weights(child)

def classify(net: Module, data: pd.DataFrame, namePaths: str, percentagePaths: str, conversionType: str, **kwargs):
    """
    Classifies the data using a given PyTorch model.

    Args:
        net (Module): The PyTorch model to use for classification.
        data (pd.DataFrame): The data to classify.
        namePaths (str): The path to the file containing the names.
        percentagePaths (str): The path to the file containing the percentages.
        conversionType (str): The type of conversion to perform. Options are "SqueezeNet1D", "ResNet1D", and "DiNet".

    Kwargs:
        distributionMethod (str): The method to use for distribution. Options are "normalization" and "standardization". Default is None.
        XTrain (np.ndarray): The training data. This is required if distributionMethod is not None.

    Returns:
        pd.DataFrame: A DataFrame containing the names, percentages, and classifications.

    Note:
        This function uses the predict method of the PyTorch model to classify the data.
        The classifications are either "Presencia de Agua" or "No Presencia de Agua".
    """
    with open(namePaths, "rb") as file:
        names = load(file)
    
    with open(percentagePaths, "rb") as file:
        percentages = load(file)

    scalers = {
        None: Equal(),
        "normalization": MinMaxScaler(feature_range=(-1, 1)),
        "standardization": StandardScaler()
    }

    conversions = {
        "SqueezeNet1D": lambda x: x.unsqueeze(1).repeat(1, 3, 1),
        "ResNet1D": lambda x: x.unsqueeze(1),
        "DiNet": lambda x: x.unsqueeze(1)
    }

    data = np.array(data)

    scaler = scalers[kwargs.get("distributionMethod", None)]
    scaler.fit(kwargs.get("XTrain", None))
    scaledData = scaler.transform(data)

    conversionFunc = conversions[conversionType]
    dataAsTensor = conversionFunc(torch.tensor(scaledData.astype(np.float32)))
    classifications = net.predict(dataAsTensor)

    hydroclassifications = [
        "Presence of Water" if classification.item() == 1 else
        "No Presence of Water"
        for classification in classifications
    ]

    results = pd.DataFrame({
        "Names": names,
        "Percentage with 100 Ωm": percentages,
        "Classification": hydroclassifications
    })

    return results

class EarlyStopper:
    def __init__(self, patience=1, minDelta=0):
        self.patience = patience
        self.minDelta = minDelta
        self.counter = 0
        self.minValidationLoss = np.inf
        self.bestWeights = None

    def early_stop(self, model, validationLoss):
        if validationLoss < self.minValidationLoss:
            self.minValidationLoss = validationLoss
            self.counter = 0
            self.bestWeights = model.state_dict()
        elif validationLoss > (self.minValidationLoss + self.minDelta):
            self.counter += 1
            if self.counter >= self.patience:
                model.load_state_dict(self.bestWeights)
                return True
        return False