import argparse
import socket
import time


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cliente TCP simples")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=9001)
    args = parser.parse_args()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        start = time.perf_counter()
        client.connect((args.host, args.port))
        client.sendall(b"ping")
        response = client.recv(4096)
        elapsed = time.perf_counter() - start

        print({
            "status": response.decode("utf-8"),
            "elapsed_s": round(elapsed, 6)
        })
