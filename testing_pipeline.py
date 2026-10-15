
import csv
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR / "output" / "processed_transactions.csv"


def test_pipeline():
    result = subprocess.run(
        [sys.executable, str(BASE_DIR / "main.py")],
        capture_output=True,
        text=True,
        check=True,
    )

    assert "Pipeline successful: 3 records processed." in result.stdout
    assert OUTPUT_FILE.exists()

    with OUTPUT_FILE.open(encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    assert len(rows) == 3
    assert all(row["status"] == "SUCCESS" for row in rows)
    assert rows[0]["transaction_id"] == "103"
    assert rows[0]["processing_fee"] == "160.00"
