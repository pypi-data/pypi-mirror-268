from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name = 'leoid',
    version = '1.1.6',
    author = 'Jay Ticku',
    description = 'LEOID Python Package',
    long_description = long_description,
    long_description_content_type='text/markdown',
    install_requires = [
        'imbalanced-learn==0.12.0',
        'scikit-learn==1.2.2',
        'lightgbm==4.2.0'
    ],
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    include_package_data = True
)
