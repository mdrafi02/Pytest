#content of test_executiongroup.py

import pytest 

def f():
    raise ExecutionGroup(
        "Group message",
        [
            RuntimeError(),
        ]
    )

def test_execution_in_group():
    with pytest.raises(ExceptionGroup) as execinfo:
        f()
        assert execinfo.group_contains(RuntimeError)
        assert not execinfo.group_contains(TypeError)
        