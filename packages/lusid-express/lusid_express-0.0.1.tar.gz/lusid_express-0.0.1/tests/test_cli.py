import os


def test_cli():
    from src.lusid_express.config import load
    os.system("rm -rf src/lusid_express/config.yaml")
    #run the python -m lusid_express --enable vars command
    os.system("python -m lusid_express --enable vars")
    #check if the config.yaml file has been created with the vars feature enabled
    assert os.path.exists("src/lusid_express/config.yaml")
    with open("src/lusid_express/config.yaml", "r") as f:
        config = load()
        assert 'vars' in config['features'] 
        
        os.system("python -m lusid_express --disable vars")
        config = load()
        assert 'vars' not in config['features']
        os.system("python -m lusid_express --enable vars magic")
        config = load()
        assert 'vars' in config['features']
        assert 'magic' in config['features']
        os.system("python -m lusid_express --disable vars magic")
        config = load()
        assert 'vars' not in config['features']
        assert 'magic' not in config['features']

        