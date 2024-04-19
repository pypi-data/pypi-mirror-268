import torch
import torch.nn as nn
import torch.optim as optim

from hygeoclas.utils.support import EarlyStopper

def kaiming_init(module):
    nn.init.kaiming_normal_(module.weight, mode="fan_out", nonlinearity="relu")
    if module.bias is not None:
        nn.init.constant_(module.bias, 0)

def reset_weights(self):
    for module in self.modules():
        if isinstance(module, nn.Conv1d) or isinstance(module, nn.Linear):
            kaiming_init(module)
        elif isinstance(module, nn.BatchNorm1d):
            nn.init.constant_(module.weight, 1)
            nn.init.constant_(module.bias, 0)

class BasicBlock1D(nn.Module):
    def __init__(self, inputChannels, outputChannels, inputStride):
        super(BasicBlock1D, self).__init__()
        self.conv1 = nn.Conv1d(inputChannels, outputChannels, kernel_size=3, stride=inputStride, padding=1, dilation=1)
        self.conv2 = nn.Conv1d(outputChannels, outputChannels, kernel_size=3, stride=1, padding=1, dilation=1)
        self.bn = nn.BatchNorm1d(outputChannels)
        self.relu = nn.ReLU()
        self.to(torch.device("cuda:0" if torch.cuda.is_available() else "cpu"))

        if inputStride!=1 or inputChannels!=outputChannels:
            self.shortcut = nn.Sequential(
                nn.Conv1d(inputChannels, outputChannels, kernel_size=1, stride=inputStride, padding=0, dilation=1),
                nn.BatchNorm1d(outputChannels)
            )
        else:
            self.shortcut = nn.Identity()

    def forward(self, x):
        fx = self.conv1(x)
        fx = self.bn(fx)
        fx = self.relu(fx)
        fx = self.conv2(fx)
        fx = self.bn(fx)
        hx = fx + self.shortcut(x)
        hx = self.relu(hx)
        return hx
    
class BottleneckBlock1D(nn.Module):
    def __init__(self, inputChannels, outputChannels, inputStride):
        super(BottleneckBlock1D, self).__init__()
        bottleneckChannels = outputChannels//4        

        self.conv1 = nn.Conv1d(inputChannels, bottleneckChannels, kernel_size=1, stride=inputStride, padding=0, dilation=1)
        self.bn1 = nn.BatchNorm1d(bottleneckChannels)
        self.conv2 = nn.Conv1d(bottleneckChannels, bottleneckChannels, kernel_size=3, stride=1, padding=1, dilation=1)
        self.bn2 = nn.BatchNorm1d(bottleneckChannels)
        self.conv3 = nn.Conv1d(bottleneckChannels, outputChannels, kernel_size=1, padding=0, dilation=1)
        self.bn3 = nn.BatchNorm1d(outputChannels)
        self.relu = nn.ReLU()
        self.to(torch.device("cuda:0" if torch.cuda.is_available() else "cpu"))

        if inputStride!=1 or inputChannels!=outputChannels:
            self.shortcut = nn.Sequential(
                nn.Conv1d(inputChannels, outputChannels, kernel_size=1, stride=inputStride, padding=0, dilation=1),
                nn.BatchNorm1d(outputChannels)
            )
        else:
            self.shortcut = nn.Identity()

    def forward(self, x):
        fx = self.conv1(x)
        fx = self.bn1(fx)
        fx = self.relu(fx)
        fx = self.conv2(fx)
        fx = self.bn2(fx)
        fx = self.relu(fx)
        fx = self.conv3(fx)
        fx = self.bn3(fx)
        hx = fx + self.shortcut(x)
        hx = self.relu(hx)
        return hx

class ResNet1D(nn.Module):
    def __init__(self, block=BasicBlock1D, nBlocks=[2,2,2,2], nClasses=2):
        super(ResNet1D, self).__init__()
        self.block = block
        self.nClasses = nClasses
        self.M = 224

        self.conv1 = nn.Conv1d(1, 64, kernel_size=7, stride=2, padding=3, dilation=1)
        self.bn1 = nn.BatchNorm1d(64)
        self.relu = nn.ReLU()
        self.mp = nn.MaxPool1d(kernel_size=3, stride=2, padding=1, dilation=1)
        if block == BasicBlock1D:
            self.rl1 = self._make_layer(block, 64, 64, nBlocks[0], 1)
            self.rl2 = self._make_layer(block, 64, 128, nBlocks[1], 2)
            self.rl3 = self._make_layer(block, 128, 256, nBlocks[2], 2)
            self.rl4 = self._make_layer(block, 256, 512, nBlocks[3], 2)
        else:
            self.rl1 = self._make_layer(block, 64, 256, nBlocks[0], 1)
            self.rl2 = self._make_layer(block, 256, 512, nBlocks[1], 2)
            self.rl3 = self._make_layer(block, 512, 1024, nBlocks[2], 2)
            self.rl4 = self._make_layer(block, 1024, 2048, nBlocks[3], 2)
        self.ap = nn.AdaptiveAvgPool1d(1)
        self.fc512 = nn.Linear(512, self.nClasses)
        self.fc2048 = nn.Linear(2048, self.nClasses)

        self.optimizer = optim.SGD(self.parameters(), lr=0.1, momentum=0.9, weight_decay=0.0001) 
        self.lossFunction = nn.CrossEntropyLoss()
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.to(self.device)

    def _make_layer(self, block, inputChannels, outputChannels, nBlocks, inputStride):
        strides = [inputStride] + [1]*(nBlocks-1)
        layers = []
        for stride in strides:
            layers.append(block(inputChannels, outputChannels, stride))
            inputChannels = outputChannels
        return nn.Sequential(*layers)
    
    def reset_weights(self):
        self.apply(reset_weights) 

    def reset_parameters(self):
        self.trainLosses = []
        self.validationLosses = []
        self.predictions = []
        self.error = None
        self.accuracy = None

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.mp(x)
        x = self.rl1(x)
        x = self.rl2(x)
        x = self.rl3(x)
        x = self.rl4(x)
        x = self.ap(x)
        x = torch.flatten(x, 1)
        if self.block == BasicBlock1D:
            x = self.fc512(x)
        else:
            x = self.fc2048(x)
        return x

    def fit(self, trainLoader, validationLoader, epochs):
        self.trainLosses = []
        self.validationLosses = []
        bestValidationLoss = float("inf")
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

            if validationLoss < bestValidationLoss:
                bestValidationLoss = validationLoss
            else:
                for param_group in self.optimizer.param_groups:
                    param_group["lr"] /= 10
            
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