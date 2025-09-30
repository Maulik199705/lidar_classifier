"""
Setup script for LiDAR Classification Orchestrator.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
if readme_file.exists():
    with open(readme_file, "r", encoding="utf-8") as fh:
        long_description = fh.read()
else:
    long_description = "LiDAR Classification Workflow Orchestrator"

setup(
    name="lidar-classifier",
    version="1.0.0",
    author="LiDAR Tools Team",
    description="Production-ready desktop application for LiDAR classification workflow orchestration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: GIS",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.10",
    install_requires=[
        "PySide6>=6.4.0",
        "numpy>=1.21.0",
        "pandas>=1.3.0",
    ],
    entry_points={
        "console_scripts": [
            "lidar-classifier=lidar_classifier.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "lidar_classifier": ["../configs/*.json"],
    },
)