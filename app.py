from flask import Flask, render_template_string

app = Flask(__name__)

# URLs for your overlays
SOCIAL_OVERLAY_URL = "https://socialstream.ninja/dock.html?session=cxbfKsNRwF&password=false&savesingle&fadein&transparent&hidemenu"
MULTI_ALERTS_URL = "https://socialstream.ninja/multi-alerts.html?session=cxbfKsNRwF&password=false"

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
            width: 100%;
            height: 100%;
            background: transparent;
            overflow: hidden;
        }}
        iframe {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
            background: transparent;
        }}
        #multiAlerts {{
            pointer-events: none; /* so clicks pass through to underlying iframe */
            z-index: 10; /* on top */
        }}
        #overlay {{
            z-index: 5; /* behind alerts */
        }}
    </style>
</head>
<body>
    <!-- Main overlay -->
    <iframe id="overlay" src="{SOCIAL_OVERLAY_URL}" allowtransparency="true"></iframe>

    <!-- Multi-alerts overlay -->
    <iframe id="multiAlerts" src="{MULTI_ALERTS_URL}" allowtransparency="true"></iframe>

    <script>
        function reloadIframe(iframe, url) {{
            iframe.src = "";
            setTimeout(() => {{
                iframe.src = url;
            }}, 1000);
        }}

        const overlay = document.getElementById("overlay");
        const multiAlerts = document.getElementById("multiAlerts");

        // Handle iframe errors
        overlay.onerror = () => {{
            console.log("Overlay iframe error. Reloading...");
            reloadIframe(overlay, "{SOCIAL_OVERLAY_URL}");
        }};
        multiAlerts.onerror = () => {{
            console.log("Alerts iframe error. Reloading...");
            reloadIframe(multiAlerts, "{MULTI_ALERTS_URL}");
        }};

        // Auto-refresh every 60 seconds
        setInterval(() => {{
            reloadIframe(overlay, "{SOCIAL_OVERLAY_URL}");
            reloadIframe(multiAlerts, "{MULTI_ALERTS_URL}");
        }}, 60000);

        // Reload if internet reconnects
        window.addEventListener("online", () => {{
            reloadIframe(overlay, "{SOCIAL_OVERLAY_URL}");
            reloadIframe(multiAlerts, "{MULTI_ALERTS_URL}");
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
