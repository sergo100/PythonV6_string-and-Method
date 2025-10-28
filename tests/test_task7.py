import io
import sys
from task_7 import solve

def run_io_fun(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()


def test_sample_1():
    assert run_io_fun("Every You Every Me\n") == "eVERY yOU eVERY mE"

def test_sample_2():
    assert run_io_fun("RunnING up That HILL\n") == "rUNNING uP tHAT hILL"

def test_sample_3():
    assert run_io_fun("Sleeping with GHOSTS\n") == "sLEEPING wITH gHOSTS"
