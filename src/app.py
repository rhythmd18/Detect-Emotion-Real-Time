from flask import Flask, jsonify, render_template, request
import cv2
import numpy as np
import base64
from utils import detect_face, predict_emotions

app = Flask(__name__)


@app.route('/')
def home():
    """
    A function that handles requests to the root URL ("/") and returns the rendered template of the "index.html" file.
    """
    return render_template('index.html')


@app.route('/api/analyze_frame', methods=['POST'])
def analyze_frame():
    """
    Analyzes a frame of an image received via a POST request to the '/api/analyze_frame' endpoint.
    
    Returns:
        A JSON response containing the status of the analysis, bounding boxes of detected faces, and predicted emotions.
    """
    data = request.get_json()
    img_data = data['image']
    img_data = base64.b64decode(img_data.split(',')[1])
    nparr = np.frombuffer(img_data, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)

    # Perform the predictions here
    bboxes = detect_face(img)
    emotion = predict_emotions(bboxes, img)

    if type(bboxes) == tuple:
        bboxes = list(bboxes)
    else:
        bboxes = bboxes.tolist()

    return jsonify({'status': 'success', 'bboxes': bboxes, 'emotion': emotion})


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)