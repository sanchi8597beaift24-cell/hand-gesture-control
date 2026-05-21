from flask import Flask, render_template

app = Flask(__name__)

# =========================
# HOME PAGE
# =========================
@app.route('/')
def home():
    return render_template("index.html")


# =========================
# START CAMERA PAGE
# =========================
@app.route('/start')
def start():
    return """
    <!DOCTYPE html>

    <html>

    <head>

        <title>Hand Gesture Camera</title>

        <!-- External CSS -->
        <link rel="stylesheet" href="/static/style.css">

        <!-- External JavaScript -->
        <script src="/static/script.js" defer></script>

        <style>

            body{
                margin:0;
                padding:0;
                text-align:center;
                font-family:Arial;
                background: linear-gradient(to right, #141e30, #243b55);
                color:white;
            }

            h1{
                margin-top:30px;
                color:#00ffcc;
            }

            #camera-container{
                margin-top:30px;
            }

        </style>

    </head>

    <body>

        <h1>🖐 Hand Gesture Camera Started</h1>

        <div id="camera-container"></div>

    </body>

    </html>
    """


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)