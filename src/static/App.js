var video = document.querySelector("#videoElement");
var canvas = document.createElement("canvas");
canvas.id = "boundingBoxCanvas";
var ctx = canvas.getContext("2d");

var container = document.querySelector("#container");
container.appendChild(canvas); // Add the canvas to the document body

if (navigator.mediaDevices.getUserMedia) {
  navigator.mediaDevices
    .getUserMedia({ video: true })
    .then(function (stream) {
      video.srcObject = stream;
      video.onloadedmetadata = function (e) {
        video.play();
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
      };
    })
    .catch(function (err0r) {
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
      // console.log(data);

      if (data.status === "success" && data.bboxes.length > 0) {
        // console.log(data.bboxes);
        drawBoundingBoxes(data.bboxes, data.emotions);
      }
    })
    .catch((error) => {
      console.log("Error: ", error);
    });
}

// Function to draw the bounding boxes
function drawBoundingBoxes(bboxes, emotions) {
  bboxes.forEach((box) => {
    console.log(box);

    const [x, y, width, height] = box;
    const text = emotions[bboxes.indexOf(box)];

    // Set Styling
    ctx.strokeStyle = "#c3ff00";
    ctx.font = "20px Candara";
    ctx.lineWidth = 1;

    // Draw rectangles and text
    ctx.beginPath();
    ctx.fillStyle = "#c3ff00";
    ctx.fillText(text, x, y - 5);
    ctx.rect(x, y, width, height);
    ctx.stroke();
  });
}

// It capture the frame every 50 milliseconds and send it to the server
setInterval(function () {
  var frame = captureFrame();
  sendFrame(frame);
}, 50);
