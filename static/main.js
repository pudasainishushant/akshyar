var canvas;
var ctx;
var width;
var height;



canvas = document.getElementById("sketchpad");
ctx = canvas.getContext("2d");
ctx.lineWidth = 10;
width = canvas.width;
height = canvas.height;
 


var isDrawing = false;
canvas.onmousedown = function(e) {
  isDrawing = true;
  ctx.moveTo(e.offsetX, e.offsetY);
};
canvas.onmousemove = function(e) {
  if (isDrawing) {
    ctx.lineTo(e.offsetX, e.offsetY);
    ctx.stroke();
  }
};
canvas.onmouseup = function() {
  isDrawing = false;
  highlight(document.querySelector('.options'));
};
// Clear the canvas context using the canvas width and height
function clearCanvas(canvas,ctx) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}
function init() {
    // Get the specific canvas element from the HTML document
    canvas = document.getElementById('sketchpad');

    // If the browser supports the canvas tag, get the 2d drawing context for this canvas
    if (canvas.getContext)
        ctx = canvas.getContext('2d');

    // Check that we have a valid context to draw on/with before adding event handlers
    if (ctx) {
        canvas.addEventListener('mousedown', canvas_mouseDown, false);
        canvas.addEventListener('mousemove', canvas_mouseMove, false);
        window.addEventListener('mouseup', canvas_mouseUp, false);
    }
}

function prepareImg() {
 var canvas = document.getElementById('sketchpad');
 var imgValue = canvas.toDataURL();
 console.out(imgValue)
 imgValue = imgValue.replace(/^data:image\/(png|jpg);base64,/, "")

 console.out(imgValue)

 document.getElementById('inp_img').value = imgValue
}