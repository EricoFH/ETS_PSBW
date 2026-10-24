import threading, webview
from app import app

def run():
    app.run(port=5050)

threading.Thread(target=run, daemon=True).start()
webview.create_window("InvenTrack", "http://127.0.0.1:5050")
webview.start()