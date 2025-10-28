import io
import sys
from src.task_2 import solve

def run_io_fun(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()

def test_sample():
    assert run_io_fun("Donald Trump\n") == "oadTup"
