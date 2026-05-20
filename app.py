from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
    <html>
    <head>
        <title>Hand Gesture Control</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                background: linear-gradient(to right, #141e30, #243b55);
                color: white;
                padding-top: 100px;
            }
            h1 {
                font-size: 40px;
                color: #00ffcc;
            }
            p {
                font-size: 18px;
            }
            .box {
                background: rgba(255,255,255,0.1);
                padding: 20px;
                margin: auto;
                width: 60%;
                border-radius: 15px;
                box-shadow: 0 0 10px #00ffcc;
            }
        </style>
    </head>

    <body>
        <h1>🤖 Hand Gesture Control System</h1>
        <div class="box">
            <p>Welcome to your AI-based project 🚀</p>
            <p>Modules:</p>
            <p>✔ Hand Tracking</p>
            <p>✔ Virtual Mouse</p>
            <p>✔ Air Canvas</p>
            <p><b>Project is successfully deployed on Render</b></p>
        </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)