from setuptools import setup, find_packages
setup(
    name = 'GSG',
    version='0.4.5',
    packages=find_packages(),
    python_requires='>=3.7',
    py_modules=['GSG'],
    install_requires=[
        'torch==1.9.0',
        'numpy==1.21.6',
        'scanpy==1.8.2',
        'anndata==0.8.0',
        'dgl==0.9.0',
        'pandas==1.2.4',
        'scipy==1.7.3',
        'scikit-learn==1.0.1',
        'tqdm==4.64.1',
        'matplotlib==3.5.3',
        'tensorboardX==2.5.1',
        'pyyaml==6.0.1',
    ]
)