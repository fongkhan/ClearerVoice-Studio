from setuptools import setup, find_packages

setup(
    name="clearvoice",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch>=2.0.1",
        "torchaudio>=2.0.2",
        "numpy>=1.24.2",
        "scipy>=1.10.1",
        "soundfile>=0.12.1",
        "librosa>=0.10.2",
    ],
) 