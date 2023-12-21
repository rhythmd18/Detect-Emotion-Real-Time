import cv2
import torch
from torch import nn
from models.model import VGG13Custom

clf = cv2.CascadeClassifier('./src/models/haarcascade_frontalface_default.xml')

model = VGG13Custom()

model.load_state_dict(torch.load('./src/models/model_weights.pth', map_location=torch.device('cpu')))
model.eval()

labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Neutral', 'Sad', 'Surprise']


def detect_face(frame):
    faces = clf.detectMultiScale(
        frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    return faces



def predict_emotions(faces, frame):
    predictions = []
    for (x, y, width, height) in faces:
        cropped = frame[y:y+height, x:x+width]
        resized = cv2.resize(cropped, (48, 48)) / 255
        X = torch.from_numpy(resized).unsqueeze(0).unsqueeze(0).to(torch.float32)
        
        y_pred = model(X)

        pred_idx = y_pred.argmax(1).item()
        prediction = labels[pred_idx]

        predictions.append(prediction)

    return predictions