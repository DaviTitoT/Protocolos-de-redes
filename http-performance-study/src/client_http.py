import argparse
import json
import time

import requests


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cliente HTTP simples")
    parser.add_argument("--url", default="http://127.0.0.1:8001/")
    args = parser.parse_args()

    start = time.perf_counter()
    response = requests.get(args.url, timeout=5)
    elapsed = time.perf_counter() - start

    payload = {
        "status_code": response.status_code,
        "elapsed_s": round(elapsed, 6),
        "body": response.text.strip(),
    }
    print(json.dumps(payload))
