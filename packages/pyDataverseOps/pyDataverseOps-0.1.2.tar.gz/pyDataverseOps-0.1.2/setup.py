from setuptools import setup, find_packages

setup(
    name="pyDataverseOps",
    version="0.1.2",
    author="Akash Yadav",
    author_email="akash21091999@gmail.com",
    description="A Python library to facilitate operations on Microsoft Dataverse",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ray2199/pyDataverseOps.git",  # Replace with your repository URL
    packages=find_packages(),
    install_requires=["pandas>=1.0", "requests>=2.20"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
