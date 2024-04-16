#
#
#   _____ _____     ____   ____        _________________    ____  ____
#  /     \\__  \   / ___\_/ __ \      /  ___/\____ \__  \ _/ ___\/ __ \
# |  Y Y  \/ __ \_/ /_/  >  ___/      \___ \ |  |_> > __ \\  \__\  ___/
# |__|_|  (____  /\___  / \___  > /\ /____  >|   __(____  /\___  >___  >
#       \/     \//_____/      \/  \/      \/ |__|       \/     \/    \/
#
# Copyright (C) (2024) Ollano, Inc. - All Rights Reserved
#
from setuptools import setup, find_packages

# Read the contents of your requirements.txt file
with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="mageic-common",
    version="0.4.0",
    author="Gregory D. Hunkins",
    author_email="greg@ollano.com",
    packages=find_packages(),
    license=open("LICENSE.txt").read(),
    long_description=open("README.md").read(),
    install_requires=required,
)
