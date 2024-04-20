from setuptools import setup, find_packages

setup(
    name="numpyneuron",
    version="0.4",
    author="Jensen Holm",
    author_email="jensen.dev.01@gmail.com",
    description="Simple, lightweight neural network framework built in numpy",
    long_description=open("about_package.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jensen-holm/Numpy-Neuron",
    project_urls={"Bug Tracker": "https://github.com/Jensen-holm/Numpy-Neuron/issues"},
    package_dir={"": "numpyneuron"},
    packages=find_packages(where="numpyneuron"),
    classifiers=[
    ],
    python_requires=">=3.6",
)
