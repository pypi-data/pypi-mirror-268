from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="MultiGATE",
    version="0.0.15",
    description="MultiGATE single cell",
    packages=find_packages(),  # This will find all packages in the directory
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aqlkzf/MultiGATEtest1",
    author="Jinzhao LI & Jishuai MIAO",
    author_email="jishuaimiao@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'tensorflow-gpu==1.15.0',
        'scikit-learn>=1.0.2',
        'pandas>=1.3.5',
        'scanpy>=1.9.3',
        'jupyterlab>=3.6.7',
        'tqdm>=4.66.2',
        'matplotlib>=3.5.3',
        'networkx>=2.6',
        'pybedtools>=0.9.0',
        'seaborn>=0.12.2',
        'numpy>=1.21.6',
        'scipy>=1.7.3',
        'nvidia-ml-py3>=7.352.0', 
        'gseapy>=1.0.4',
        'rpy2>=3.5.16',
        'louvain>=0.8.0',
    ],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires="==3.7.*",
)
