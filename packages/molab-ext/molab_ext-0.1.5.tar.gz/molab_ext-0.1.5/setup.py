from setuptools import find_packages, setup

setup(
    name='molab_ext',
    packages=find_packages(),
    version='0.1.5',
    description='molab extension',
    author='frgoyb',
    install_requires=['IPython',
                      'requests',
                      'dill',
                      'VizKG']
)