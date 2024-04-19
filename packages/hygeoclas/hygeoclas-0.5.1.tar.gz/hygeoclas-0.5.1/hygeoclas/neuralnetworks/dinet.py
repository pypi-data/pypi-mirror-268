import torch
import torch.nn as nn

from hygeoclas.utils.support import EarlyStopper
from hygeoclas.utils.support import reset_weights

class DiNet(nn.Module):
    def __init__(self):
        super(DiNet, self).__init__()
        self.conv1 = nn.Conv1d(1, 5, 3, stride=1, padding=0, dilation=1) 
        self.bn1 = nn.BatchNorm1d(5)
        self.maxPool = nn.MaxPool1d(kernel_size=2, stride=1, padding=0, dilation=1)
        self.conv2 = nn.Conv1d(5, 10, 5, stride=1, padding=0, dilation=1)
        self.bn2 = nn.BatchNorm1d(10)
        self.dropout = nn.Dropout(0.1)
        self.fc = nn.Linear(1420, 2)

        self.optimizer = torch.optim.RMSprop(self.parameters(), lr=0.001)
        self.lossFunction = nn.CrossEntropyLoss()
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        
        self.to(self.device)
    
    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = nn.functional.leaky_relu(x, 0.1)
        x = self.maxPool(x)
        x = self.conv2(x)
        x = self.bn2(x)
        x = nn.functional.leaky_relu(x, 0.1)
        x = self.maxPool(x)
        x = torch.flatten(x, 1)
        x = self.dropout(x)
        x = self.fc(x)
        x = nn.functional.softmax(x, 1)
        return x
    
    def reset_weights(self):
        self.apply(reset_weights)   

    def reset_parameters(self):
        self.trainLosses = []
        self.validationLosses = []
        self.predictions = []
        self.error = None
        self.accuracy = None

    def fit(self, trainLoader, validationLoader, epochs):
        self.trainLosses = []
        self.validationLosses = []
        earlyStopper = EarlyStopper(patience=1, minDelta=0)

        for epoch in range(epochs):
            trainLossSummation = 0
            self.train()
            for data, target in trainLoader:
                data = data.to(self.device)
                target = target.to(self.device)

                output = self(data)
                loss = self.lossFunction(output, target)

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

                trainLossSummation += loss.item()
            trainLoss = trainLossSummation/len(trainLoader)
            self.trainLosses.append(trainLoss)

            validationLossSummation = 0
            self.eval()
            with torch.no_grad():
                for data, target in validationLoader:
                    data = data.to(self.device)
                    target = target.to(self.device)

                    output = self(data)
                    loss = self.lossFunction(output, target)

                    validationLossSummation += loss.item()
            validationLoss = validationLossSummation/len(validationLoader)
            self.validationLosses.append(validationLoss)

            for param_group in self.optimizer.param_groups:
                param_group["lr"] *= 0.9

            if earlyStopper.early_stop(self, validationLossSummation):
                print(f"Stopping training early at epoch {epoch}")
                self.trainLosses = self.trainLosses[:-1]
                self.validationLosses = self.validationLosses [:-1]
                break
        self.error = self.trainLosses[-1]

    def evaluate(self, testLoader):
        self.predictions = []
        correct = 0
        total = 0
        self.eval()

        with torch.no_grad():
            for data, target in testLoader:
                data = data.to(self.device)

                target = target.to(self.device)
                output = self(data)
                _, predicted = torch.max(output.data, 1)

                self.predictions.extend(predicted.tolist())

                total += target.size(0)
                correct += (predicted == target).sum().item()
        self.accuracy = 100*(correct/total)
        print(f"Accuracy: {round(self.accuracy, 2)}%")
    
    def predict(self, torchVector):
        self.eval()
        
        with torch.no_grad(): 
            output = self(torchVector)
            probabilities = torch.softmax(output, dim=1)
            predicted = torch.argmax(probabilities, dim=1)

            return predicted