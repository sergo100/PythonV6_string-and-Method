import io
import sys
from src.task_5 import solve

def run_io_fun(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()

def test_sample_1():
    assert run_io_fun("become\n") == "ebecom"

def test_sample_2():
    assert run_io_fun("come\n") == "ecom"

def test_sample_3():
    assert run_io_fun("qwertY\n") == "Yqwert"

def test_sample_4():
    assert run_io_fun("AbracadabrA\n") == "AAbracadabr"
