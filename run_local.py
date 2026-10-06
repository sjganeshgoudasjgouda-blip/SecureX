"""Start FrameTrace on http://localhost:8000 and open the browser.
Usage:  python run_local.py     (Python 3, no extra packages needed)"""
import http.server, socketserver, webbrowser, os, threading

PORT = 8000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("127.0.0.1", PORT), Quiet) as server:
    url = f"http://localhost:{PORT}/index.html"
    print(f"FrameTrace is running at {url}  (press Ctrl+C to stop)")
    threading.Timer(1, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("Stopped.")
