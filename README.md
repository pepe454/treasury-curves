[![Treasury Curves](https://raw.githubusercontent.com/pepe454/treasury-curves/main/.github/logo.png)](https://raw.githubusercontent.com/pepe454/treasury-curves/main/.github/logo.png)

[![ci](https://github.com/pepe454/treasury-curves/actions/workflows/ci.yml/badge.svg)](https://github.com/pepe454/treasury-curves/actions/workflows/ci.yml)
[![PyPi Version](https://img.shields.io/pypi/v/treasurycurves.svg)](https://pypi.python.org/pypi/treasurycurves/)
[![Package Status](https://img.shields.io/pypi/status/treasurycurves.svg)](https://pypi.org/project/treasurycurves/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

Access and chart US Treasury Curve data

Full documentation can be found at [treasury-curves.readthedocs.io](https://treasury-curves.readthedocs.io/en/latest/)

<br/>

# Selecting and plotting data

Using the Developer API found at [treasury.gov](https://home.treasury.gov/developer-notice-xml-changes),
one can find yield curves dating back to the 90's.

Access data for a particular date using ``` curves("2022-08-08") ```.
curves will find the nearest valid date (weekday) and returns a pandas dataframes of all curves
available on that date or nearest to it. calling ``` curves() ``` will use the current date.
Optionally specify ``` curves(allow_missing=True) ``` to keep years with missing data.

Alternatively, you can retrieve all data by calling ``` download() ```.

Once you have the data, it is possible to plot out the yield curves with
``` plot(curves_data, start="2022-01-01", end="2022-05-03", num_years=1) ```.
Specify the number of years, or pick a start and end date to sample from, as the chart would otherwise
become inundated with yield curve data.

Save your data in a spreadsheet using ``` export(curves_data, file_extension="csv") ``` and specify
"csv" or "xlsx" to determine the file type.

<br/>

# Using treasurycurves from the Command Line

Install through pip:

``` pip install treasury-curves ```

Once installing, you can run the entrypoint:

``` treasury --help ```

Use the module directly:

``` import treasury  ```

Working inside the repository

``` python treasury.py --help ```

```

usage: treasury.py [-h] [-a] [-s START] [-e END] [-d DATE] [-y YEARS] [-p] [-o OUTPUT]

treasurycurves - query and analyze US Treasury yield data

optional arguments:
  -h, --help            show this help message and exit
  -a, --allowna         Allow NaN values
  -s START, --start START
                        Year to start analysis
  -e END, --end END     Year to end analysis. If equal to start, analyze curves for the year
  -d DATE, --date DATE  Date in YYYY-MM-DD to analyze
  -y YEARS, --years YEARS
                        Num years before end to analyze
  -p, --plot            Plot yield curves
  -o OUTPUT, --output OUTPUT
                        File extension to save data (csv or xlsx), leave empty to avoid saving file
```

<br/>
