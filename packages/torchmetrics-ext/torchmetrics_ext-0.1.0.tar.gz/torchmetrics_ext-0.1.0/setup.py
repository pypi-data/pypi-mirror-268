from setuptools import find_packages, setup

setup(
    name="torchmetrics_ext",
    version="0.1.0",
    author="Yiming Zhang",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    download_url="https://github.com/eamonn-zh/torchmetrics_ext",
    install_requires=[
        "torchmetrics", "torch"
    ]
)
