from setuptools import setup, find_packages

setup(
    name='custom_train_duy',
    version='0.1',
    packages=find_packages(exclude=['data', 'myenv', 'venv']),
    description='No description',
    author='Duy',
    author_email='duyht1.bhsoft@gmail.com',
)
