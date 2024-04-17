```markdown
# Confidence Interval Library

The Confidence Interval Library is a Python package for calculating confidence intervals for various statistical metrics. This library simplifies the process of estimating the confidence intervals around a sample mean, proportion, or other statistical estimates.

## Installation

You can install the Confidence Interval Library directly from PyPI:

```bash
pip install confidence_interval

```

## Features

- **Mean Confidence Interval**: Calculate the confidence interval for the mean of a dataset.
- **Proportion Confidence Interval**: (If applicable) Calculate the confidence interval for the proportion of a dataset.
- **Custom Confidence Levels**: Allows specifying different confidence levels.

## Usage

Here is how you can use the Confidence Interval Library:

### Calculating Mean Confidence Interval

```python
from confidence_interval import mean_confidence_interval
data = [1, 2, 3, 4, 5]
mean, lower_bound, upper_bound = mean_confidence_interval(data)
print("Mean:", mean)
print("Lower bound:", lower_bound)
print("Upper bound:", upper_bound)
```

## Requirements

- Python 3.6+
- NumPy
- SciPy

## Contributing

Contributions are welcome! Please fork the repository and open a pull request with your additions, or open an issue if you find any bugs or have suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- **Subashanan Nair** - *Initial work* - [SubaashNair](https://github.com/SubaashNair)

## Acknowledgments

- To my students
- Logic and Mathematics
- Life
```

