from setuptools import setup, find_packages

import glob

setup(
        name            ="rx_scripts",
        version         ='0.3.4',
        description     ='Generic utilities for data analysis',
        long_description='Package used to store utilities for RX calculation',
        scripts         = glob.glob('scripts/*') + glob.glob('jobs/*'),
        packages        = find_packages(where='src'), 
        package_dir     = {'' : 'src'},
        package_data    = {'scripts_data' : ['*/*.json']},
        install_requires= open('requirements.txt').read()
        )

