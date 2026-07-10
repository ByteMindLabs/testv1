# use pytest to test the add function in app.py
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from testv1 import app


def test_add():
    assert app.add(2, 3) == 5
    assert app.add(-1, 1) == 0
    assert app.add(0, 0) == 0

# add a method to call the test_add function and print the result
if __name__ == "__main__":  
    test_add()
    print("All tests passed!")