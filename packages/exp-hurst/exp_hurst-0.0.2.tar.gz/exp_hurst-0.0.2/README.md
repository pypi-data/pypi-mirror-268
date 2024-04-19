# Hurst Exponent Package

## Description
The function hurst takes a np.array of numbers and returns the Hurst exponent of the time series. The Hurst exponent is a measure of randomness of a time series. It is used in the study of long-term memory of time series. The value of the Hurst exponent is between 0 and 1. A value of 0.5 indicates that the time series is random. A value greater than 0.5 indicates that the time series is trending. A value less than 0.5 indicates that the time series is mean reverting.

## Installation
```bash
pip install exp_hurst
```

## Requirements
- numpy
- mmq

## Usage
```python
from coef_hurst import hurst
hurst(time_series)
```

## Example
```python
from exp_hurst import hurst
import numpy as np

# Create a time series of random numbers
rs = np.random.normal(0, 1, 100000)

# Evaluate the Hurst exponent
h = hurst(rs)
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

## Author
[Igor Matheus Jasenovski]

## Version
0.0.1

## References
[Hurst Exponent](https://en.wikipedia.org/wiki/Hurst_exponent#:~:text=The%20Hurst%20exponent%20is%20used,between%20pairs%20of%20values%20increases.)