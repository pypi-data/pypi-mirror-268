#!/usr/bin/env python3
# Author: Matthias Mayer
# Date: 6.7.2023
import configparser
import os
from pathlib import Path

# Get default configuration file
with open(Path(__file__).parent.joinpath('cobra.config.sample')) as f:
    DEFAULT_CONFIG_TXT = f.read()

# Find the package directory of cobra-io
this_file = Path(__file__).absolute()
parent_dir = this_file
while parent_dir.name != 'cobra-io':
    parent_dir = parent_dir.parent
    if parent_dir.name == '':
        break

# Configure configparser
COBRA_CONFIG = configparser.ConfigParser()
if parent_dir.name == 'cobra-io':  # Keep the file local if cobra-io is installed from source
    CONFIG_FILE = parent_dir.joinpath('cobra.config')
    if os.getenv("CONDA_DEFAULT_ENV") == "cobra-io":
        print("Detected conda environment cobra-io. The configuration file is not plac.")
else:
    CONFIG_FILE = Path('~/.config/cobra.config').expanduser()
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
if not CONFIG_FILE.exists():
    with open(CONFIG_FILE, 'w') as f:
        f.write(DEFAULT_CONFIG_TXT)
    print("Created a default configuration file at", CONFIG_FILE, "for cobra-io.")
COBRA_CONFIG.read(CONFIG_FILE)

# Get global variables
COBRA_VERSION = COBRA_CONFIG['API']['version']
