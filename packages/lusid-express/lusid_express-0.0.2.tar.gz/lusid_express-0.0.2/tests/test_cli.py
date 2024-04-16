import os
import subprocess
import sys

def test_cli():
    from src.lusid_express.config import load
    os.system("rm -rf src/lusid_express/config.yaml")
    #run the python -m lusid_express --enable vars command
    command = [sys.executable, "-m", "lusid_express", "--enable", "vars"]
    result = subprocess.run(command, capture_output=True, text=True)
    print("stdout:", result.stdout)
    print("stderr:", result.stderr)
    #check if the config.yaml file has been created with the vars feature enabled
    assert os.path.exists("src/lusid_express/config.yaml")
    with open("src/lusid_express/config.yaml", "r") as f:
        config = load()
        assert 'vars' in config['features'] 
        command = [sys.executable, "-m", "lusid_express", "--disable", "vars"]
        subprocess.run(command, capture_output=True, text=True)
        config = load()
        assert 'vars' not in config['features']
        command = [sys.executable, "-m", "lusid_express", "--enable", "vars", "magic"]
        subprocess.run(command, capture_output=True, text=True)
        config = load()
        assert 'vars' in config['features']
        assert 'magic' in config['features']
        command = [sys.executable, "-m", "lusid_express", "--disable", "vars",  "magic"]
        subprocess.run(command, capture_output=True, text=True)
        config = load()
        assert 'vars' not in config['features']
        assert 'magic' not in config['features']

        