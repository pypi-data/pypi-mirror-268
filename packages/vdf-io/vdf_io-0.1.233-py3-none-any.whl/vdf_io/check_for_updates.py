import requests

import vdf_io

def check_for_update():
    package_name = 'vdf-io'
    response = requests.get(f'https://pypi.org/pypi/{package_name}/json')
    if response.status_code == 200:
        latest_version = response.json()['info']['version']
        if latest_version != vdf_io.__version__:
            print(f'Update available: {latest_version}. Run `pip install --upgrade {package_name}` to update.')
