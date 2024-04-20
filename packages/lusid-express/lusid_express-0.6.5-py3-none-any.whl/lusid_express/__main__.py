import argparse
import yaml
import os
import shutil
import warnings

# Suppress all warnings
warnings.filterwarnings('ignore')

def parse_args():
    
    parser = argparse.ArgumentParser(description="Configure lusid_express settings.")
    parser.add_argument('-e','--enable', nargs='+', type=str, choices=['vars', 'magic','format'], help='Enable feature(s).')
    parser.add_argument('-d','--disable', nargs='+', type=str, choices=['vars', 'magic','format'], help='Disable feature(s).')
    
    return parser.parse_args()

def update_config(args):
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f) or {}
    else:
        config = {'features': []}

    enabled_features = set(config.get('features', []))
    show_msg = False
    change_msg = "Configuration updated successfully! Changes will be applied after kernel restart."
    if args.enable:
        diff = set(args.enable) - enabled_features
        enabled_features.update(args.enable)
        if diff:
            print(f"Enabling features: {', '.join(diff)}")
            print(change_msg)

    if args.disable:
        diff = set(args.disable) - enabled_features
        for feature in args.disable:
            if feature in enabled_features:
                show_msg = True
        enabled_features.difference_update(args.disable)
        if show_msg:
            print(f"Disabling features: {', '.join(args.disable)}")
            print(change_msg)

    config['features'] = list(enabled_features)

    with open(config_path, 'w') as f:
        yaml.safe_dump(config, f)
    
    


def copy_startup_file():
    ipython_startup_dir = os.path.expanduser('~/.ipython/profile_default/startup/')
    target_file = os.path.join(ipython_startup_dir, '00-load_lusid_express.py')
    source_file = os.path.join(os.path.dirname(__file__), 'load.le')

    # Ensure the IPython startup directory exists
    os.makedirs(ipython_startup_dir, exist_ok=True)

    # Copy the load.py file if it does not already exist
    shutil.copy(source_file, target_file)
        
        
        
        
def main():
    args = parse_args()
    update_config(args)
    copy_startup_file()
    

if __name__ == "__main__":
    main()
