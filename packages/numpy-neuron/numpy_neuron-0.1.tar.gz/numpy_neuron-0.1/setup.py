from setuptools import setup, find_packages

setup(
    name="numpy_neuron",
    version="0.1",
    author="Jensen Holm",
    author_email="jensen.dev.01@gmail.com",
    description="Simple, lightweight neural network framework built in numpy",
    long_description=open('warning.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jensen-holm/Numpy-Neuron",
    project_urls={
        "Bug Tracker": "https://github.com/Jensen-holm/Numpy-Neuron/issues"
    },
    package_dir={"": "nn"},
    packages=find_packages(where="nn"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

