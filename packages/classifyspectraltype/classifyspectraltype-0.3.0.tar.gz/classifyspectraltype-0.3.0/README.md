[![codecov](https://codecov.io/gh/DSCI-310-2024/classifyspectraltype/branch/main/graph/badge.svg)](https://codecov.io/gh/DSCI-310-2024/classifyspectraltype)

# classifyspectraltype

`classifyspectraltype` is a Python package tailored for data scientists and analysts focusing on predictive analytics in laptop pricing. This package focuses on data cleaning, file copying, logistic regression modeling, and plot saving functionalities to facilitate a smoother workflow from raw data to insights.


## Installation

```bash
$ pip install classifyspectraltype
```

## Usage

classifyspectraltype allows users to create tables and boxplot visualizations from NASA’s Exoplanet Archive' planetary systems dataset, as well as perform cross validation, confidence interval removal, and train test split functions.

```bash
from classifyspectraltype.boxplot_table_function import make_boxplot_and_table
from classifyspectraltype.split_cross_val import split_cross_val
from classifyspectraltype.clean_confidence_intervals import clean_confidence_intervals
```
Below are some examples of how to use our functions:

```bash
make_boxplot_and_table("preprocessed_data_csv", "column_name", "example_csv_directory", "example_boxplot_directory") # This function produces a boxplot and csv table saved to respective dirs

split_cross_val("preprocessed_data_csv", "target_variable_name", "split= decimal_percent", "folds= number_of_folds") # This function splits the data using train_test_split and calculates cross validation scores for logistic regression and random forest models

clean_confidence_intervals("example_dataset_csv") # This function removes confidence intervals, keeping only the mean values in the dataset
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`classifyspectraltype` was created by DSCI310 Group16. It is licensed under the terms of the MIT license.

## Credits

`classifyspectraltype` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
