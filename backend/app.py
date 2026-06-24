import os
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = b"Hello from Effective Mobile!"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def log_message(self, format, *args):
        print(f"[backend] {self.address_string()} - {format % args}")

if __name__ == "__main__":
    port = int(os.environ.get("BACKEND_PORT", 8080))
    print(f"[backend] Starting on port {port}...")
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()