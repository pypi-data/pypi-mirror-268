from setuptools import setup, find_packages

setup(
    name='transformermath',
    version='0.1.1',  
    packages=find_packages(),
    install_requires=[
        'matplotlib==3.8.4',
        'numpy==1.26.4',
        'pandas==1.5.3', 
        'scikit-learn==1.4.2',
        'plotly==5.20.0',
        'umap-learn==0.5.6',
        'torch==2.2.2',
        'seaborn==0.13.2',
        'scipy==1.13.0',
    ],
)
