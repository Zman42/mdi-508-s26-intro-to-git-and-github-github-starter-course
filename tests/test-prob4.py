import subprocess
import sys
import pytest

def run(cmd):
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return res.stdout.strip()

def test_sum_csv():
    data_file = None
    expected = None
    atol = 1e-6

    for arg in sys.argv:
        if arg.startswith("--data-file="):
            data_file = arg.split("=", 1)[1]
        if arg.startswith("--expected="):
            expected = float(arg.split("=", 1)[1])
        if arg.startswith("--atol="):
            atol = float(arg.split("=", 1)[1])

    assert data_file is not None
    assert expected is not None

    out = float(run([sys.executable, "sum_csv.py", data_file]))
    assert out == pytest.approx(expected, abs=atol)