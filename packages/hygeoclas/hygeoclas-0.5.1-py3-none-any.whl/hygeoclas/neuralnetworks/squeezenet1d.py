import torch
import torch.nn as nn
import torch.optim as optim

from hygeoclas.utils.support import EarlyStopper
from hygeoclas.utils.support import reset_weights

class Fire1D(nn.Module):
    def __init__(self, inputChannels, s1x1Size, e1x1Size, e3x3Size):
        super(Fire1D, self).__init__()
        self.squeeze = nn.Conv1d(inputChannels, s1x1Size, kernel_size=1)
        self.expand1x1 = nn.Conv1d(s1x1Size, e1x1Size, kernel_size=1)
        self.expand3x3 = nn.Conv1d(s1x1Size, e3x3Size, kernel_size=3, padding=1)
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        x = self.squeeze(x)
        x = self.relu(x)
        return torch.cat([
            self.relu(self.expand1x1(x)),
            self.relu(self.expand3x3(x))
        ], 1)

class SqueezeNet1D(nn.Module):
    def __init__(self):
        super(SqueezeNet1D, self).__init__()
        self.M = 224
        self.features = nn.Sequential(
            nn.Conv1d(3, 96, kernel_size=7, stride=2, padding=2),
            nn.MaxPool1d(kernel_size=3, stride=2),
            Fire1D(96, 16, 64, 64),
            Fire1D(128, 16, 64, 64),
            Fire1D(128, 32, 128, 128),
            nn.MaxPool1d(kernel_size=3, stride=2),
            Fire1D(256, 32, 128, 128),
            Fire1D(256, 48, 192, 192),
            Fire1D(384, 48, 192, 192),
            Fire1D(384, 64, 256, 256),
            nn.MaxPool1d(kernel_size=3, stride=2),
            Fire1D(512, 64, 256, 256),
            nn.Dropout1d(0.5),
            nn.Conv1d(512, 2, kernel_size=1, stride=1),
            nn.AvgPool1d(kernel_size=13, stride=1)
        )

        self.optimizer = optim.Adadelta(self.parameters(), lr=0.04, weight_decay=0.0002)
        self.lossFunction = nn.CrossEntropyLoss()
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        self.to(self.device)
    
    def reset_weights(self):
        self.apply(reset_weights)   

    def reset_parameters(self):
        self.trainLosses = []
        self.validationLosses = []
        self.predictions = []
        self.error = None
        self.accuracy = None

    def forward(self, x):
        x = self.features(x)
        return x
    
    def fit(self, trainLoader, validationLoader, epochs):
        self.trainLosses = []
        self.validationLosses = []
        earlyStopper = EarlyStopper(patience=1, minDelta=0)
        scheduler = torch.optim.lr_scheduler.LambdaLR(self.optimizer, lr_lambda=lambda epoch: (1-(epoch/epochs))**1.0)
        
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
            scheduler.step()
            
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
            _, predicted = torch.max(output.data, 1)

        return predicted