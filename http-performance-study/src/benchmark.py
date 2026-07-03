import csv
import socket
import subprocess
import sys
import time
from pathlib import Path

import matplotlib.pyplot as plt
import requests

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
CSV_PATH = DATA_DIR / "resultados.csv"
IMAGE_PATH = DATA_DIR / "benchmark_http_tcp.png"


def _start_server(script_name, port):
    return subprocess.Popen(
        [sys.executable, str(BASE_DIR / "src" / script_name), "--host", "127.0.0.1", "--port", str(port)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def _wait_for_port(host, port, timeout=10):
    deadline = time.time() + timeout
    while time.time() < deadline:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.2)
            try:
                sock.connect((host, port))
                return True
            except OSError:
                time.sleep(0.1)
    return False


def _stop_server(process):
    if process is None:
        return
    process.terminate()
    try:
        process.wait(timeout=3)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait(timeout=3)


def measure_http(iterations=10):
    measurements = []
    for _ in range(iterations):
        start = time.perf_counter()
        response = requests.get("http://127.0.0.1:8001/health", timeout=5)
        elapsed = time.perf_counter() - start
        measurements.append({"protocol": "HTTP", "elapsed_s": elapsed, "status_code": response.status_code})
    return measurements


def measure_tcp(iterations=10):
    measurements = []
    for _ in range(iterations):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            start = time.perf_counter()
            client.connect(("127.0.0.1", 9001))
            client.sendall(b"ping")
            client.recv(4096)
            elapsed = time.perf_counter() - start
            measurements.append({"protocol": "TCP", "elapsed_s": elapsed, "status_code": 200})
    return measurements


def save_results(http_results, tcp_results):
    DATA_DIR.mkdir(exist_ok=True)
    rows = []
    for item in http_results:
        rows.append(["HTTP", item["elapsed_s"], item["status_code"]])
    for item in tcp_results:
        rows.append(["TCP", item["elapsed_s"], item["status_code"]])

    with CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["protocol", "elapsed_s", "status_code"])
        writer.writerows(rows)

    print(f"Resultados salvos em {CSV_PATH}")


def plot_results(http_results, tcp_results):
    http_times = [item["elapsed_s"] for item in http_results]
    tcp_times = [item["elapsed_s"] for item in tcp_results]

    plt.figure(figsize=(8, 4.5))
    box = plt.boxplot([http_times, tcp_times])
    box["medians"][0].set_color("#1f77b4")
    box["medians"][1].set_color("#d62728")
    plt.xticks([1, 2], ["HTTP", "TCP"])
    plt.title("Comparação de latência HTTP x TCP")
    plt.ylabel("Tempo de resposta (s)")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(IMAGE_PATH, dpi=150)
    plt.close()

    print(f"Gráfico salvo em {IMAGE_PATH}")


def run_benchmark(iterations=10):
    http_process = _start_server("server_http.py", 8001)
    tcp_process = _start_server("server_tcp.py", 9001)

    try:
        if not _wait_for_port("127.0.0.1", 8001) or not _wait_for_port("127.0.0.1", 9001):
            raise RuntimeError("Não foi possível iniciar um dos servidores de teste.")
        time.sleep(0.5)
        http_results = measure_http(iterations)
        tcp_results = measure_tcp(iterations)
        save_results(http_results, tcp_results)
        plot_results(http_results, tcp_results)
    finally:
        _stop_server(http_process)
        _stop_server(tcp_process)


if __name__ == "__main__":
    print("Iniciando benchmark HTTP x TCP...")
    run_benchmark()
