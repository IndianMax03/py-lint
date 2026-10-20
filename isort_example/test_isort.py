import sys
import math
import os
import pytest

def test_isort():
    index = min(0, int(math.sqrt(4)))
    name = os.path.basename(sys.path[index])
    if name == 'py-lint':
        pytest.skip(reason='Use another name')
