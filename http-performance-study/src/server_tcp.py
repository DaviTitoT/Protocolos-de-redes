import argparse
import socket


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Servidor TCP simples")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=9001)
    args = parser.parse_args()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((args.host, args.port))
        server.listen(5)
        print(f"Servidor TCP escutando em {args.host}:{args.port}")

        while True:
            conn, _ = server.accept()
            with conn:
                data = conn.recv(4096)
                if data:
                    conn.sendall(b"TCP_OK")
