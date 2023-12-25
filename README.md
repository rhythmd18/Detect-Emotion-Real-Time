# Facial Emotion Detector

A simple Flask application that detects facial expressions using machine learning. It captures frames from a video stream and predicts the facial expressions.

It uses a CNN architecture which is an implementation of the model as described in this [research paper](https://arxiv.org/abs/1608.01041).

The application has been dockerized for other devs to try out.

## Run Locally

In order to run this application locally follow these steps:

- Install [Docker](https://www.docker.com/products/docker-desktop/)
- Start the docker engine, and
- Run the following command to pull the image

```bash
docker pull rhythmd18/facial-emotion-detector-app:latest
```

- Run the application using this command

```bash
docker run -p 5000:5000 rhythmd18/facial-emotion-detector-app
```

That's it!

## Demo

![](https://github.com/rhythmd18/Facial-Emotion-Detector/blob/main/demo.gif)

## Files Description

- `app.py`: This is the main file that runs the Flask application. It sets up the server and routes for the API, and serves the Convolutional Neural Network (CNN) model.

- `utils.py`: This file contains utility functions. One function takes in a frame and detect the nearest face in it. Another function predicts the emotion of the detected face by passing it through the model.

- `model.py`: This file defines the architecture of the CNN model using PyTorch. It is an implementation of the model defined in this [paper](https://arxiv.org/abs/1608.01041).

- `model_weights.pth`: This file contains the trained parameters of the CNN model. It is used to load the weights into the model architecture defined in `model.py`.

- `test.py`: This is a standalone file used for testing the application without using the web interface. It uses OpenCV to capture frames and then uses the model to predict emotions.

- `Scripts.ipynb`: Notebook file which contains the model training scripts.

- `App.js`: This file contains scripts that interact with the API route. It sends frames to the API and receives responses in JSON format, which are then used to update the DOM.
- `index.html` and `styles.css`: Pretty self-explanatory!

## Tech Stack

**Client:** HTML, CSS, JavaScript

**Server:** Flask

**CNN Architecture:** PyTorch

## Appendix

- [Dataset](https://www.kaggle.com/datasets/prilia/fer2013pluscleanedaugmballanced1)
- [Research Paper](https://arxiv.org/abs/1608.01041)
- [PyTorch Quickstart](https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html)
