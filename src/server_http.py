import argparse
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def index():
    return jsonify({
        "status": "ok",
        "message": "Servidor HTTP pronto",
        "service": "hospital-integration"
    }), 200


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Servidor HTTP simples")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8001)
    args = parser.parse_args()

    app.run(host=args.host, port=args.port, debug=False, use_reloader=False)
