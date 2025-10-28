import io
import sys
from src.task_8 import solve

def run_io_fun(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()


def test_sample_1():
    assert run_io_fun("banana\n") == "5"

def test_sample_2():
    assert run_io_fun("cat\n") == "1"

def test_sample_3():
    assert run_io_fun("zoo\n") == "-1"
