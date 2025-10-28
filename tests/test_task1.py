import io
import sys
from tasks.task_1 import solve

def run_io_fun(input_data):
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    solve()
    return sys.stdout.getvalue().strip()

def test_sample_1():
    assert run_io_fun("Монти Пайтон\n") == "МниПйо"

def test_sample_2():
    assert run_io_fun("Цой жив!\n") == "Цйжв"
