# test_variables.py
import pytest
from IPython.core.interactiveshell import InteractiveShell
from unittest.mock import patch

@pytest.fixture(scope="module")
def ipython_env():
    ip = InteractiveShell()
    InteractiveShell._instance = ip
    
    return ip





def test_variable_exists(ipython_env):
    with patch('src.lusid_express.config.load', return_value={'features': ['vars']}) as mock_load:
        ipython_env.run_line_magic('run', './load.py')
        assert 'lu' in ipython_env.user_ns, "lusid does not exist in the IPython namespace"
        assert 'lm' in ipython_env.user_ns, "lusid.models  does not exist in the IPython namespace"
        assert 'apis' in ipython_env.user_ns, "lusid_express.apis does not exist in the IPython namespace"
        assert 'ls' not in ipython_env.user_ns, "extraneous var found, likely an issue with test setup"
