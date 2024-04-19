import glob
import numpy as np
import pandas as pd
import torch

from datetime import datetime
from scipy.stats import shapiro
from sklearn.metrics import confusion_matrix, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from tqdm import tqdm

from hygeoclas.utils.crawl import get_udf_record
from hygeoclas.utils.methods import DataCompressor

class Filter:
    """
    A class used to filter and clean datasets for training, validation, and testing.

    Attributes:
        filePathOfNWPresence (str): The file path of the dataset with presence of unwanted elements.
        filePathOfWPresence (str): The file path of the dataset with presence of wanted elements.
        filePathForTesting (str): The file path of the dataset for testing.
    """
        
    def __init__(self, **kwargs):
        """
        The constructor for Filter class.

        Kwargs:
            filePathOfNWPresence (str): The file path of the dataset with presence of unwanted elements. Default is None.
            filePathOfWPresence (str): The file path of the dataset with presence of wanted elements. Default is None.
            filePathForTest (str): The file path of the dataset for testing. Default is None.
        """
        self.filePathOfNWPresence = kwargs.get("filePathOfNWPresence", None)
        self.filePathOfWPresence = kwargs.get("filePathOfWPresence", None)
        self.filePathForTesting = kwargs.get("filePathForTest", None)

    def list_values(self, pathOfTheDatasets: str) -> None:
        """
        Lists the values of the electrical resistivity measurements from the datasets.

        Args:
            pathOfTheDatasets (str): The path of the datasets.
        """
        self.listOfRhoaValues = []
        self.filePaths = glob.glob(f"{pathOfTheDatasets}/*")
        for filePath in tqdm(self.filePaths, desc="Listing values of the electrical resistivity measurements", unit=" file"):
            rhoa = get_udf_record(filePath, "rhoa", cleaned=True)
            self.listOfRhoaValues.append(rhoa)

    def normality_test(self) -> None:
        """
        Performs a normality test on the listed values.
        """
        self.distributions = []
        for rhoaValues in tqdm(self.listOfRhoaValues, desc="Performing normality tests", unit=" values"):
            pValue = shapiro(rhoaValues).pvalue
            self.distributions.append("Normal" if pValue > 0.05 else "Other")

    def remove_outliers(self) -> None:
        """
        Removes outliers from the listed values based on the normality test.
        """
        self.listOfCleanedRhoaValues = []
        for rhoaValues, distribution in tqdm(zip(self.listOfRhoaValues, self.distributions), desc="Performing the removal of outlier", unit=" values"):
            if distribution == "Normal":
                mean = np.mean(rhoaValues)
                standardDeviation = np.std(rhoaValues)
                outlierBoolean = np.abs(rhoaValues - mean) > 3*standardDeviation

                self.listOfCleanedRhoaValues.append(rhoaValues[~outlierBoolean])

            else:
                Q1 = np.percentile(rhoaValues, 25)
                Q3 = np.percentile(rhoaValues, 75)
                IQR = Q3 - Q1
                outlierBoolean = (rhoaValues < (Q1 - 1.5*IQR)) | (rhoaValues > (Q3 + 1.5*IQR))

                self.listOfCleanedRhoaValues.append(rhoaValues[~outlierBoolean])

    def for_training_validation(self) -> None:
        """
        Prepares the datasets for training and validation.
        """
        self.list_values(self.filePathOfNWPresence)
        self.normality_test()
        self.remove_outliers()
        self.listOfCleanedNWPRecords = self.listOfCleanedRhoaValues

        self.list_values(self.filePathOfWPresence)
        self.normality_test()
        self.remove_outliers()
        self.listOfCleanedWPRecords = self.listOfCleanedRhoaValues

    def for_testing(self):
        """
        Prepares the dataset for testing.
        """
        self.list_values(self.filePathForTesting)
        self.normality_test()
        self.remove_outliers()
        self.listOfCleanedTestingRecords = self.listOfCleanedRhoaValues

def split_data(database: pd.DataFrame, trainSize: float = 0.8, validationSize: float = 0.1, testSize: float = 0.1) -> tuple:
    """
    Splits the database into training, validation, and test sets.

    Args:
        database (pd.DataFrame): The database to be split.
        trainSize (float): The proportion of the database to include in the train split.
        validationSize (float): The proportion of the database to include in the validation split.
        testSize (float): The proportion of the database to include in the test split.

    Returns:
        tuple: The training, validation, and test data and labels.
    """

    data = np.array(database[database.columns[1:]])
    labels = np.array(database[database.columns[0]])

    sizeToFit = validationSize/trainSize 

    XTrain, XTest, yTrain, yTest = train_test_split(data, labels, test_size=testSize, shuffle=True)
    XTrain, XValidation, yTrain, yValidation = train_test_split(data, labels, test_size=sizeToFit, shuffle=True)

    return XTrain, XValidation, XTest, yTrain, yValidation, yTest

def normalize_data(XTrain: np.ndarray, XValidation: np.ndarray, XTest: np.ndarray, method: str = None) -> tuple:
    """
    Normalizes or standardizes the data.

    Args:
        XTrain (np.ndarray): The training data.
        XValidation (np.ndarray): The validation data.
        XTest (np.ndarray): The test data.
        method (str): The normalization or standardization method.

    Returns:
        tuple: The normalized or standardized data.
    """

    if method == "normalization":
        scaler = MinMaxScaler(feature_range=(-1, 1))
        scaler.fit(XTrain)

        XTrain = scaler.transform(XTrain)
        XValidation = scaler.transform(XValidation)
        XTest = scaler.transform(XTest)

    elif method == "standardization":
        scaler = StandardScaler()
        scaler.fit(XTrain)

        XTrain = scaler.transform(XTrain)
        XValidation = scaler.transform(XValidation)
        XTest = scaler.transform(XTest)

    return XTrain, XValidation, XTest

def to_tensor(XTrain: np.ndarray, XValidation: np.ndarray, XTest: np.ndarray, yTrain: np.ndarray, yValidation: np.ndarray, yTest: np.ndarray, conversionType: str) -> tuple:
    """
    Converts the data to tensors.

    Args:
        XTrain (np.ndarray): The training data.
        XValidation (np.ndarray): The validation data.
        XTest (np.ndarray): The test data.
        yTrain (np.ndarray): The training labels.
        yValidation (np.ndarray): The validation labels.
        yTest (np.ndarray): The test labels.
        conversionType (str): The type of conversion to perform. Options are "ResNet1D" and "SqueezeNet1D".

    Returns:
        tuple: The data as tensors (XTrain, XValidation, XTest, yTrain, yValidation, yTest).

    Raises:
        TypeError: If conversionType is None.

    Note:
        For "ResNet1D", the data is converted to tensors with an extra dimension.
        For "SqueezeNet1D", the data is converted to tensors with an extra dimension and repeated along that dimension.
    """

    if conversionType in ["ResNet1D", "DiNet"]:
        XTrain = torch.tensor(XTrain.astype(np.float32)).unsqueeze(1)
        yTrain = torch.tensor(yTrain.astype(np.int64))

        XValidation = torch.tensor(XValidation.astype(np.float32)).unsqueeze(1)
        yValidation = torch.tensor(yValidation.astype(np.int64))

        XTest = torch.tensor(XTest.astype(np.float32)).unsqueeze(1)
        yTest = torch.tensor(yTest.astype(np.int64))

    elif conversionType == "SqueezeNet1D":
        XTrain = torch.tensor(XTrain.astype(np.float32)).unsqueeze(1).repeat(1, 3, 1)
        yTrain = torch.tensor(yTrain.astype(np.int64)).unsqueeze(-1)

        XValidation = torch.tensor(XValidation.astype(np.float32)).unsqueeze(1).repeat(1, 3, 1)
        yValidation = torch.tensor(yValidation.astype(np.int64)).unsqueeze(-1)

        XTest = torch.tensor(XTest.astype(np.float32)).unsqueeze(1).repeat(1, 3, 1)
        yTest= torch.tensor(yTest.astype(np.int64)).unsqueeze(-1)

    elif conversionType == None:
        raise TypeError("The type of tensor conversion for the entered neural network has not been specified.")

    return XTrain, XValidation, XTest, yTrain, yValidation, yTest

def create_data_loaders(XTrain: torch.Tensor, XValidation: torch.Tensor, XTest: torch.Tensor, yTrain: torch.Tensor, yValidation: torch.Tensor, yTest: torch.Tensor, batchSize: int = None) -> tuple:
    """
    Creates data loaders for the data.

    Args:
        XTrain (torch.Tensor): The training data.
        XValidation (torch.Tensor): The validation data.
        XTest (torch.Tensor): The test data.
        yTrain (torch.Tensor): The training labels.
        yValidation (torch.Tensor): The validation labels.
        yTest (torch.Tensor): The test labels.
        batchSize (int): The number of samples per batch.

    Returns:
        tuple: The data loaders for the training, validation, and test data.
    """

    XyTrain = torch.utils.data.TensorDataset(XTrain, yTrain)
    XyValidation = torch.utils.data.TensorDataset(XValidation, yValidation)
    XyTest = torch.utils.data.TensorDataset(XTest, yTest)

    trainLoader = torch.utils.data.DataLoader(XyTrain, batch_size=batchSize)
    validationLoader = torch.utils.data.DataLoader(XyValidation, batch_size=batchSize)
    testLoader = torch.utils.data.DataLoader(XyTest, batch_size=batchSize)

    return (trainLoader, validationLoader, testLoader)

class ANNHCMod:
    def __init__(self, **kwargs):
        self.accuracies = []

        self.filePathOfNWPresence = kwargs.get("filePathOfNWPresence", None)
        self.filePathOfWPresence = kwargs.get("filePathOfWPresence", None)
        self.compressedDatabase = kwargs.get("compressedDatabase", None)
        self.saveDatabase = kwargs.get("saveDatabase", False)
        self.databaseSavePath = kwargs.get("databaseSavePath", "./")
        self.databaseThreshold = kwargs.get("databaseThreshold", 0)

        self.net = kwargs.get("net", None)
        self.trainSize = kwargs.get("trainSize", 0.8)
        self.validationSize = kwargs.get("validationSize", 0.1)
        self.testSize = kwargs.get("testSize", 0.1)
        self.distributionMethod = kwargs.get("distributionMethod", None)
        self.conversionType = kwargs.get("conversionType", None)
        self.batchSize = kwargs.get("batchSize", 1)
        self.epochs = kwargs.get("epochs", 10)
        self.cycles = kwargs.get("cycles", 5)

        self.M = kwargs.get("M", None)
    
    def __format__(self, formatSpec) -> None:
        match formatSpec:
            case "version":
                return "Version 1.2"
        
    def filtering_data(self) -> None:
        filter = Filter(filePathOfNWPresence=self.filePathOfNWPresence, filePathOfWPresence=self.filePathOfWPresence)
        filter.for_training_validation()

        self.listOfCleanedNWPRecords = filter.listOfCleanedNWPRecords
        self.listOfCleanedWPRecords = filter.listOfCleanedWPRecords

    def create_compressed_database(self) -> None:
        dataCompressor = DataCompressor(self.M, (self.listOfCleanedNWPRecords, 0), (self.listOfCleanedWPRecords, 1))
        self.compressedDatabase = dataCompressor.execute()
        
        if self.saveDatabase:
            dataCompressor.save(self.databaseSavePath, self.databaseThreshold)

    def change_data_distribution(self) -> None:
        self.XTrain0, XValidation, XTest, self.yTrain, self.yValidation, self.yTest = split_data(self.compressedDatabase, self.trainSize, self.validationSize, self.testSize)
        self.XTrain, self.XValidation, self.XTest = normalize_data(self.XTrain0, XValidation, XTest, self.distributionMethod)

    def do_training_validation(self) -> None:
        self.metrics = []
        for _ in range(self.cycles):
            self.change_data_distribution()

            XTrain, XValidation, XTest, yTrain, yValidation, yTest = to_tensor(self.XTrain, self.XValidation, self.XTest, self.yTrain, self.yValidation, self.yTest, self.conversionType)
            trainLoader, validationLoader, testLoader = create_data_loaders(XTrain, XValidation, XTest, yTrain, yValidation, yTest, self.batchSize)

            self.net.reset_weights()
            self.net.fit(trainLoader, validationLoader, epochs=self.epochs)
            self.net.evaluate(testLoader)

            yPredicted = self.net.predictions
            precisionScore = precision_score(self.yTest, yPredicted, average="binary", zero_division=0)
            recallScore = recall_score(self.yTest, yPredicted, average="binary")
            f1Score = f1_score(self.yTest, yPredicted, average="binary")
            confusionMatrix = confusion_matrix(self.yTest, yPredicted)

            self.metrics.append((self.net.error, self.net.accuracy, precisionScore, recallScore, f1Score, confusionMatrix, self.net.trainLosses, self.net.validationLosses, self.net.state_dict()))
            
        self.averageError = sum(metric[0] for metric in self.metrics)/self.cycles
        self.averageAccuracy = sum(metric[1] for metric in self.metrics)/self.cycles
        self.averagePrecision = sum(metric[2] for metric in self.metrics)/self.cycles
        self.averageRecallScore = sum(metric[3] for metric in self.metrics)/self.cycles
        self.averageF1Score = sum(metric[4] for metric in self.metrics)/self.cycles

        self.scores = []
        for metric in self.metrics:
            average = ((1/metric[0]) + metric[1] + metric[2] + metric[3]+ metric[4])/3
            variance = np.var([(1/metric[0]), metric[1], metric[2], metric[3], metric[4]])
            score = average - variance
            self.scores.append(abs(score))
        index = self.scores.index(max(self.scores))

        self.bestMetrics = self.metrics[index][:6]
        
        self.net.reset_parameters()
        self.net.error = self.metrics[index][0]
        self.net.accuracy = self.metrics[index][1]
        self.net.trainLosses = self.metrics[index][6]
        self.net.validationLosses = self.metrics[index][7]

        self.bestWeights = self.metrics[index][8]
        self.net.load_state_dict(self.bestWeights)

    def execute(self, **kwargs) -> None:
        self.filePathOfNWPresence = kwargs.get("filePathOfNWPresence", self.filePathOfNWPresence)
        self.filePathOfWPresence = kwargs.get("filePathOfWPresence", self.filePathOfWPresence)
        self.compressedDatabase = kwargs.get("compressedDatabase", self.compressedDatabase)
        self.saveDatabase = kwargs.get("saveDatabase", self.saveDatabase)
        self.databaseSavePath = kwargs.get("databaseSavePath", self.databaseSavePath)
        self.databaseThreshold = kwargs.get("databaseThreshold", self.databaseThreshold)

        self.net = kwargs.get("net", self.net)
        self.trainSize = kwargs.get("trainSize", self.trainSize)
        self.validationSize = kwargs.get("validationSize", self.validationSize)
        self.testSize = kwargs.get("testSize", self.testSize)
        self.distributionMethod = kwargs.get("distributionMethod", self.distributionMethod)
        self.conversionType = kwargs.get("conversionType", self.conversionType)
        self.batchSize = kwargs.get("batchSize", self.batchSize)
        self.epochs = kwargs.get("epochs", self.epochs)
        self.cycles = kwargs.get("cycles", self.cycles)
        self.M = self.net.M

        self.filtering_data()
        self.create_compressed_database()
        self.change_data_distribution()
        self.do_training_validation()

    def execute_with_compressed_database(self, **kwargs) -> None:
        self.net = kwargs.get("net", self.net)
        self.trainSize = kwargs.get("trainSize", self.trainSize)
        self.validationSize = kwargs.get("validationSize", self.validationSize)
        self.testSize = kwargs.get("testSize", self.testSize)
        self.distributionMethod = kwargs.get("distributionMethod", self.distributionMethod)
        self.conversionType = kwargs.get("conversionType", self.conversionType)
        self.batchSize = kwargs.get("batchSize", self.batchSize)
        self.epochs = kwargs.get("epochs", self.epochs)
        self.cycles = kwargs.get("cycles", self.cycles)
        self.compressedDatabase = kwargs.get("compressedDatabase", self.compressedDatabase)

        self.do_training_validation()

    def new_compressed_database(self, M: int, **kwargs) -> pd.DataFrame:
        self.M = M

        self.filePathOfNWPresence = kwargs.get("filePathOfNWPresence", self.filePathOfNWPresence)
        self.filePathOfWPresence = kwargs.get("filePathOfWPresence", self.filePathOfWPresence)
        self.saveDatabase = kwargs.get("saveDatabase", self.saveDatabase)
        self.databaseSavePath = kwargs.get("databaseSavePath", self.databaseSavePath)
        self.databaseThreshold = kwargs.get("databaseThreshold", self.databaseThreshold)

        self.filtering_data()
        self.create_compressed_database()

        return self.compressedDatabase

def create_testing_database(M: int, filePathForTest: str, **kwargs):
    filter = Filter(filePathForTest=filePathForTest)
    filter.for_testing()
    
    dataCompressor = DataCompressor(M, filter.listOfCleanedTestingRecords)
    testingDatabase = dataCompressor.execute()

    compressedFilePaths = [filter.filePaths[index] for index in dataCompressor.listOfCompressedRecordIndexes]

    listOfCompressedTestingRecords = [filter.listOfCleanedTestingRecords[index] for index in dataCompressor.listOfCompressedRecordIndexes]
    percentages = [np.sum(testingRecord <= 100)/len(testingRecord) for testingRecord in listOfCompressedTestingRecords]

    if kwargs.get("save", False):
        dati = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        databaseSavePath = kwargs.get("savePath", "")
        testingDatabase.to_csv(f"{databaseSavePath}Corroboration q{M} {dati}.csv", index=False, encoding="utf-8-sig")

    return testingDatabase, compressedFilePaths, percentages