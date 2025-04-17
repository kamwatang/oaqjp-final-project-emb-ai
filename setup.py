# setup.py

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oaqjp_final_project_emb_ai",          # PyPI package name
    version="0.1.0",                            # Package version
    url="https://github.com/kamwatang/oaqjp-final-project-emb-ai",
    packages=setuptools.find_packages(),        # Automatically finds "oaqjp_final_project_emb_ai"
    install_requires=[
        "requests"
    ],
    python_requires=">=3.7",                    # Minimum Python version required
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)