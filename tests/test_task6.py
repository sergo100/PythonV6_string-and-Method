import io
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tasks.task6 import solve


def run_io_fun(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()


def test_sample_1():
    assert run_io_fun("PyThoN besT of The BeST\n") == "pYtHOn BESt OF tHE bEst"


def test_sample_2():
    assert run_io_fun("Я у мАмы ХацКер\n") == "я У МаМЫ хАЦкЕР"


def test_sample_3():
    assert run_io_fun("lED zEPPELiN\n") == "Led ZeppelIn"
