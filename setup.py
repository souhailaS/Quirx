"""
Setup script for LLMFuzz
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return "LLMFuzz - A Mutation-Based Fuzzer for Evaluating Prompt Robustness in LLM-Driven Applications"

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="llmfuzz",
    version="0.1.0",
    author="Souhaila Serbout",
    author_email="souhaila.serbout@example.com",
    description="A Mutation-Based Fuzzer for Evaluating Prompt Robustness in LLM-Driven Applications",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/llmfuzz",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Testing",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
        ],
        "advanced": [
            "nlpaug>=1.1.0",
            "textattack>=0.3.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "llmfuzz=llmfuzz.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
) 