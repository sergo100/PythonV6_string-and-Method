import io
import sys
from task_4 import solve

def run_io_fun(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()

def test_sample_1():
    assert run_io_fun("The Big Bang Theory\n") == "ye ag T"

def test_sample_2():
    assert run_io_fun("there is no doubt that money in the form\n") == "mfhnyottbdnirt"
