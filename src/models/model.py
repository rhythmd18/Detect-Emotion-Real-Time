import torch
from torch import nn

class VGG13Custom(nn.Module):
    
    def __init__(self):
        
        super(VGG13Custom, self).__init__()
        
        self.conv3_64 = nn.Sequential(
            nn.Conv2d(1, 64, 3, padding='same'),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Conv2d(64, 64, 3, padding='same'),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Dropout2d(0.25)
        )

        self.conv3_128 = nn.Sequential(
            nn.Conv2d(64, 128, 3, padding='same'),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.Conv2d(128, 128, 3, padding='same'),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Dropout2d(0.25)
        )

        self.conv3_256_1 = nn.Sequential(
            nn.Conv2d(128, 256, 3, padding='same'),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Conv2d(256, 256, 3, padding='same'),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Conv2d(256, 256, 3, padding='same'),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Dropout2d(0.25)
        )

        self.conv3_256_2 = nn.Sequential(
            nn.Conv2d(256, 256, 3, padding='same'),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Conv2d(256, 256, 3, padding='same'),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.Conv2d(256, 256, 3, padding='same'),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.MaxPool2d(2, 2),
            nn.Dropout2d(0.25)
        )

        self.flatten = nn.Flatten()
        
        # Get the output shape of the flatten layer
        x = torch.randn(1, 1, 48, 48)  # assuming input size (1, 64, 64)
        x = self.conv3_64(x)
        x = self.conv3_128(x)
        x = self.conv3_256_1(x)
        x = self.conv3_256_2(x)
        x = self.flatten(x)

        self.fc = nn.Sequential(
            nn.Linear(x.shape[1], 1024),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(1024, 1024),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(1024, 7)
        )
        
    def forward(self, x):
        x = self.conv3_64(x)
        x = self.conv3_128(x)
        x = self.conv3_256_1(x)
        x = self.conv3_256_2(x)
        x = self.fc(self.flatten(x))
        
        return x