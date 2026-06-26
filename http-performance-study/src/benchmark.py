import csv
import time
from pathlib import Path

import requests

OUTPUT = Path(__file__).resolve().parent.parent / "data" / "resultados.csv"


def run_benchmark(requests_count=10):
    results = []
    for i in range(requests_count):
        start = time.perf_counter()
        response = requests.get("http://127.0.0.1:8000", timeout=5)
        elapsed = time.perf_counter() - start
        results.append((i + 1, response.status_code, elapsed))

    OUTPUT.parent.mkdir(exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["request", "status_code", "elapsed_s"])
        writer.writerows(results)

    print(f"Resultados salvos em {OUTPUT}")


if __name__ == "__main__":
    run_benchmark()
