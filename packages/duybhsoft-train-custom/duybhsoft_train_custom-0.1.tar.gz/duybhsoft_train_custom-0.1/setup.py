from setuptools import setup, find_packages

setup(
    name='duybhsoft_train_custom',
    version='0.1',
    packages=find_packages(exclude=['data', 'myenv', 'venv']),
    description='No description',
    author='Duy',
    author_email='duyht1.bhsoft@gmail.com',
    install_requires=[
        "tensorflow",
        "pillow",
        "seaborn",
        "matplotlib",
        "opencv-python",
        "scikit-learn",
        "tqdm"
    ]
)
