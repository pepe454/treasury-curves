# Treasury Curve Data

Using the Developer API found at [treasury.gov](https://home.treasury.gov/developer-notice-xml-changes),
one can find yield curves dating back to the 90's.

## Selecting and plotting data

Access data for a particular date using ``` curves("2022-08-08") ```.
curves will find the nearest valid date (weekday) and returns a pandas dataframes of all curves
available on that date or nearest to it.

Once you have the data, it is possible to plot out the yield curves with ``` plot(curves_data, num_years=10) ```.
Specify the number of years as the chart quickly becomes inundated with yield curve data.

Save your data in a spreadsheet using ``` export(curves_data, file_extension="csv") ``` and specify
"csv" or "xlsx" to determine the file type.
