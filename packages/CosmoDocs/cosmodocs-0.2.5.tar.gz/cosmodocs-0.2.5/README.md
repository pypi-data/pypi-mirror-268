# Cosmo Docs

<p align="center">
  <img src="https://raw.githubusercontent.com/Strovsk/CosmoDocs/main/docs/image/Cosmo%20Docs%20Logo.png" />
</p>

Cosmo Docs is a powerful package that serves as a parser for describing functions and classes in a Python script. It provides detailed information about functions and classes, and can generate the information in markdown format. This makes it easy to document and share code documentation in a standardized and readable format.

With Cosmo Docs, you can effortlessly extract information about the structure, parameters, and return values of functions and classes in your Python code. This package is particularly useful for generating documentation for libraries, frameworks, and large codebases, where maintaining up-to-date documentation can be a challenging task.

Whether you are a developer looking to document your own code or a user exploring a Python package, Cosmo Docs simplifies the process of understanding and utilizing the available functions and classes. By providing clear and concise documentation in markdown format, Cosmo Docs enhances code readability and promotes collaboration among developers.

Get started with Cosmo Docs today and unlock the power of comprehensive code documentation!

# Getting Started

## Installation

To install Cosmo Docs, run the following command:

```bash
pip install cosmo-docs
```

## Usage

To use Cosmo Docs, import the `CosmoDocs` class from `cosmo_docs` module.

```python
from cosmo_docs import CosmoDocs

cosmos = CosmosDocs("tests/data/sample_file.py")

# to get the file information in CosmoDocsInfo dict format
# if you want use it for easy intellisense: from cosmo_docs import CosmoDocsInfo
print(cosmos.file_info)

# to get the file information in markdown format
print(cosmos.markdown)
```

> Note: You can create your own formats from `comos.file_info` dict.
