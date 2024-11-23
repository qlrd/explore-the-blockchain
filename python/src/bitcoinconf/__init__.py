"""
Parse bitcoin.conf file at $HOME/.bitcoin/bitcoin.conf    
"""

import os
from configparser import ConfigParser


def get_path():
    """Get the full path from $HOME/.bitcoin/bitcoin.conf"""
    config_home = os.path.expanduser("~")
    config_path = os.path.join(config_home, ".bitcoin", "bitcoin.conf")
    return os.path.abspath(config_path)


def get_conf(filepath: str):
    """Parse the bitcoin.conf file"""
    with open(filepath, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Add a fake section header for configparser
    processed_lines = ["[DEFAULT]\n"] + [
        line if line.strip().startswith("#") or "=" in line else "#" + line
        for line in lines
    ]

    # Parse the processed lines using configparser
    config = ConfigParser(allow_no_value=True)
    config.read_string("".join(processed_lines))

    # Return the parsed configuration as a dictionary
    return dict(config["DEFAULT"])
