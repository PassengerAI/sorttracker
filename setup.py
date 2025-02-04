from setuptools import setup, find_packages

setup(
    name='sorttracker',
    description='SORT object tracker',
    version='0.11.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'scipy>=0.18.1',
        'filterpy>=1.4.1',
        'scikit-image>=0.14.0',
        'scikit-learn>=0.19.1'
    ]
)
