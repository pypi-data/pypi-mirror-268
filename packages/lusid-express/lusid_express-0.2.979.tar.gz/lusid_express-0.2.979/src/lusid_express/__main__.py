import argparse
import yaml
import os
import shutil

def parse_args():
    
    parser = argparse.ArgumentParser(description="Configure lusid_express settings.")
    parser.add_argument('-e','--enable', nargs='+', type=str, choices=['vars', 'magic'], help='Enable feature(s).')
    parser.add_argument('-d','--disable', nargs='+', type=str, choices=['vars', 'magic'], help='Disable feature(s).')
    return parser.parse_args()

def update_config(args):
    config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f) or {}
    else:
        config = {'features': []}

    enabled_features = set(config.get('features', []))

    if args.enable:
        enabled_features.update(args.enable)

    if args.disable:
        enabled_features.difference_update(args.disable)

    config['features'] = list(enabled_features)

    with open(config_path, 'w') as f:
        yaml.safe_dump(config, f)


def copy_startup_file():
    ipython_startup_dir = os.path.expanduser('~/.ipython/profile_default/startup/')
    target_file = os.path.join(ipython_startup_dir, '00-load_lusid_express.py')
    source_file = os.path.join(os.path.dirname(__file__), 'load.py')

    # Ensure the IPython startup directory exists
    os.makedirs(ipython_startup_dir, exist_ok=True)

    # Copy the load.py file if it does not already exist
    if not os.path.exists(target_file):
        shutil.copy(source_file, target_file)
        print(f"File {source_file} copied to {target_file}")
    else:
        print(f"File {target_file} already exists. No action taken.")
        
        
        
def main():
    args = parse_args()
    update_config(args)
    copy_startup_file()
    print("Configuration updated successfully! Changes will be applied after kernel restart.")

if __name__ == "__main__":
    main()
