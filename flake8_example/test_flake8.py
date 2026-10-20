import math
import os
import pytest
import sys

def test_flake8():
    index=min(0, int(math.sqrt(4)))
    long_line = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since 1966, when designers at Letraset and James Mosley, the librarian at St Bride Printing Library in London"
    name = os.path.basename(sys.path[index])
    if name == 'py-lint':
        pytest.skip(reason=f'Use this line {long_line}')
