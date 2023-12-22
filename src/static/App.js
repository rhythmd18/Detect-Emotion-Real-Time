var video = document.querySelector("#videoElement");
var canvas = document.createElement("canvas");
var ctx = canvas.getContext("2d");

var container = document.querySelector("#video-container");

if (navigator.mediaDevices.getUserMedia) {
  // Check if getUserMedia is supported
  navigator.mediaDevices
    .getUserMedia({ video: true }) // Request access to the camera
    .then(function (stream) {
      // If access is granted
      video.srcObject = stream; // Set the video source object to the camera
      video.onloadedmetadata = function (e) {
        // Wait until the video metadata is loaded
        video.play(); // Play the video
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
      };
    })
    .catch(function (err0r) {
      // If access is denied
      console.log("Something went wrong!");
    });
}

// Function to capture the frame
function captureFrame() {
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
  var imgData = canvas.toDataURL("image/png");
  return imgData;
}

// Function to send the frame to the server
function sendFrame(imgData) {
  // Print the image data on the console
  //   console.log(imgData);
  //   Use the Fetch API to send a POST request to '/api/analyze_frame'
  fetch("/api/analyze_frame", {
    method: "POST", // HTTP method is POSt
    headers: {
      "Content-Type": "application/json", // Request content type is JSON
    },
    body: JSON.stringify({ image: imgData }), // Convert the image data to JSON format
  })
    .then((response) => response.json()) // Parse the response body as JSON
    .then((data) => {
      // Process the response data
      // console.log(data);

      if (data.status === "success") {
        // console.log(data.bboxes);
        displayEmotion(data.emotion, data.bboxes.length > 0);
      }
    })
    .catch((error) => {
      console.log("Error: ", error);
    });
}

// Function to draw the bounding boxes
function displayEmotion(emotion, hasFace) {
  // capture the frame and send it to the server
  var emotionEl = document.getElementById("emotion-el");
  if (hasFace) {
    emotionEl.style.color = "rgb(191, 255, 0)";
    emotionEl.textContent = emotion;
  } else {
    emotionEl.style.color = "red";
    emotionEl.textContent = "No face detected!";
  }
}

function getEmotion() {
  var frame = captureFrame();
  sendFrame(frame);
}
