// ==========================================
// HAND GESTURE CONTROL SYSTEM
// script.js
// ==========================================

console.log("🚀 Hand Gesture System Loaded");

// Wait until page fully loads
window.addEventListener("DOMContentLoaded", () => {

    // ==========================================
    // CAMERA CONTAINER
    // ==========================================
    const container = document.getElementById("camera-container");

    // ==========================================
    // CREATE VIDEO ELEMENT
    // ==========================================
    const video = document.createElement("video");

    video.setAttribute("autoplay", "");
    video.setAttribute("playsinline", "");

    video.width = 800;
    video.height = 600;

    // Video Styling
    video.style.width = "800px";
    video.style.maxWidth = "95%";
    video.style.border = "5px solid #00ffcc";
    video.style.borderRadius = "20px";
    video.style.boxShadow = "0 0 30px #00ffcc";
    video.style.marginTop = "20px";

    // ==========================================
    // CREATE CANVAS
    // ==========================================
    const canvas = document.createElement("canvas");

    canvas.width = 800;
    canvas.height = 600;

    // Canvas Styling
    canvas.style.position = "absolute";
    canvas.style.left = "50%";
    canvas.style.transform = "translateX(-50%)";
    canvas.style.marginTop = "20px";
    canvas.style.pointerEvents = "none";

    // ==========================================
    // APPEND ELEMENTS
    // ==========================================
    container.appendChild(video);
    container.appendChild(canvas);

    // Canvas Context
    const ctx = canvas.getContext("2d");

    // ==========================================
    // ACCESS WEBCAM
    // ==========================================
    navigator.mediaDevices.getUserMedia({
        video: true
    })

    .then((stream) => {

        // Start Webcam
        video.srcObject = stream;

        console.log("✅ Camera Started");

        // Start Drawing Loop
        drawEffects();

    })

    .catch((error) => {

        console.log("❌ Camera Error:", error);

        container.innerHTML = `
            <h2 style="
                color:red;
                margin-top:40px;
                font-size:30px;
            ">
                Camera Access Denied ❌
            </h2>
        `;
    });

    // ==========================================
    // DRAW EFFECTS FUNCTION
    // ==========================================
    function drawEffects() {

        // Clear Canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Example animated circle
        const time = Date.now() * 0.005;

        const x = 400 + Math.sin(time) * 200;
        const y = 300 + Math.cos(time) * 100;

        // Circle Glow
        ctx.beginPath();
        ctx.arc(x, y, 30, 0, Math.PI * 2);

        ctx.fillStyle = "#00ffcc";
        ctx.shadowColor = "#00ffcc";
        ctx.shadowBlur = 20;

        ctx.fill();

        // Text
        ctx.font = "28px Arial";
        ctx.fillStyle = "white";

        ctx.fillText("🖐 Hand Tracking Active", 220, 50);

        // Continue Animation
        requestAnimationFrame(drawEffects);
    }

});