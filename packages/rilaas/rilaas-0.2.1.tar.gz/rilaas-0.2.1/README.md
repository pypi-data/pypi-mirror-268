# RILAAS

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

RILAAS is a Python package that allows users to replace a given image with customized configurations using various machine learning models. 

## Installation

You can install the package using pip:

```bash
pip install rilaas
```

## Usage

```python
from rilaas.Client import Client

# Example usage
client = Client(id='id', api_key='API KEY', Optional_Params="Any other parameters you want to add according to the model")
```

## Configuration

The package utilizes a `config.yaml` file for configuration. Below is an example:

```yaml
# config.yaml
yolov5:
    functions:
        - render
        - invoke
    accept: image/jpeg
```

## Example

Here's an example demonstrating how to use the package:

```python
from rilaas.Client import Client

client = Client(url='<ip-address>:<port>', model_type='Models Deployed', endpoint='Function you want to execute', Optional_Params="Any other parameters you want to add according to the model")
```

## Issues

If you encounter any issues or have suggestions, please open an issue on the [GitHub repository](https://github.com/ahfahad96/rilaas/issues).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


