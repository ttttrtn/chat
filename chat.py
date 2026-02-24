from flask import Flask, render_template_string

app = Flask(__name__)

SOCIAL_URL = "https://socialstream.ninja/dock.html?session=cxbfKsNRwF&password=false&savesingle&fadein&transparent&hidemenu"

HTML_PAGE = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Prism Live Overlay</title>
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

        // Reload if iframe errors
        iframe.onerror = function() {{
            console.log("Iframe error detected. Reloading...");
            reloadFrame();
        }};

        function reloadFrame() {{
            iframe.src = "";
            setTimeout(() => {{
                iframe.src = "{SOCIAL_URL}";
            }}, 1000);
        }}

        // Auto refresh every 60 seconds (keeps it alive)
        setInterval(() => {{
            console.log("Refreshing iframe to keep connection alive...");
            reloadFrame();
        }}, 60000);

        // Reload if page regains internet
        window.addEventListener("online", () => {{
            console.log("Connection restored. Reloading iframe...");
            reloadFrame();
        }});

    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)