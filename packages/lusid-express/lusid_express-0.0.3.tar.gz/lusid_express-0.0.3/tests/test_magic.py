import pytest
from IPython.core.interactiveshell import InteractiveShell
from unittest.mock import patch

@pytest.fixture(scope="module")
def ipython_env():
    ip = InteractiveShell()
    InteractiveShell._instance = ip
    return ip


def test_variable_exists(ipython_env):
    with patch('src.lusid_express.config.load', return_value={'features': ['magic']}) as mock_load:
        ipython_env.run_line_magic('run', './load.py')
        assert ipython_env.find_line_magic('luminesce') is not None, "luminesce does not exist"
    
