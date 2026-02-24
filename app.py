from flask import Flask, render_template_string
import os

app = Flask(__name__)

SOCIAL_URL = "https://socialstream.ninja/dock.html?session=cxbfKsNRwF&transparent&fadein&hidemenu"
HTML_PAGE = f"""
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        html, body {{
            margin: 0;
            padding: 0;
            background: transparent;
            overflow: hidden;
        }}
        iframe {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
            background: transparent;
        }}
    </style>
</head>
<body>
    <iframe id="overlayFrame" src="{SOCIAL_URL}" allowtransparency="true"></iframe>

    <script>
        const iframe = document.getElementById("overlayFrame");

        function reloadFrame() {{
            iframe.src = "";
            setTimeout(() => {{
                iframe.src = "{SOCIAL_URL}";
            }}, 1000);
        }}

        iframe.onerror = reloadFrame;

        setInterval(() => {{
            reloadFrame();
        }}, 60000);

        window.addEventListener("online", reloadFrame);
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
