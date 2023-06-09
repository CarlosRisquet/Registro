
var video;
var model;
var canvas;
var ctx;
var drawFaceRectangleLines;

function setupCamera() {
    navigator.mediaDevices
        .getUserMedia({
            video: true,
            audio: false,
        })
        .then((stream) => {
            video.srcObject = stream;
        });
}

function imagedataToImage(imagedata) {
    var tempCanvas = document.createElement('canvas');
    var tempCtx = tempCanvas.getContext('2d');

    tempCanvas.width = imagedata.width;
    tempCanvas.height = imagedata.height;
    tempCtx.putImageData(imagedata, 0, 0);

    return tempCanvas.toDataURL();
}

function startFaceDetection(draw) {
    video = document.getElementById("video");
    canvas = document.getElementById("canvas");
    ctx = canvas.getContext("2d");
    drawFaceRectangleLines = draw;

    const detectFaces = async () => {
        const prediction = await model.estimateFaces(video, false);

        // draw the video first
        ctx.drawImage(video, 0, 0, 600, 400);

        if (drawFaceRectangleLines)
        {
            prediction.forEach((pred) => {
            
                // draw the rectangle enclosing the face
                ctx.beginPath();
                ctx.lineWidth = "2";
                ctx.strokeStyle = "blue";
    
                // the last two arguments are width and height
                // since blazeface returned only the coordinates, 
                // we can find the width and height by subtracting them.
                ctx.rect(
                    pred.topLeft[0],
                    pred.topLeft[1],
                    pred.bottomRight[0] - pred.topLeft[0],
                    pred.bottomRight[1] - pred.topLeft[1]
                );
    
                ctx.stroke();
                
                // let imageData = ctx.getImageData(pred.topLeft[0], pred.topLeft[1], pred.bottomRight[0] - pred.topLeft[0], pred.bottomRight[1] - pred.topLeft[1]);
                // let image = imagedataToImage(imageData);
                // publishImage(image);
    
                // publishImage(canvas.toDataURL());
            });
        }
    };

    setupCamera();

    video.addEventListener("loadeddata", async () => {
        model = await blazeface.load();
        // call detect faces every 100 milliseconds or 10 times every second
        setInterval(detectFaces, 100);
    });
}
