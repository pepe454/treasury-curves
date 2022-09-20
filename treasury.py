import functools
from datetime import datetime, timedelta
from io import StringIO
from tracemalloc import start

import pandas as pd
import requests
from dateutil.relativedelta import relativedelta

DATE_FMT = "%Y-%m-%d"
COLUMNS = ["1 Yr", "2 Yr", "5 Yr", "10 Yr", "20 Yr", "30 Yr"]

def curves(date=datetime.today()):
    """get treasury curves for today or a specific date"""
    date = date if isinstance(date, datetime) else datetime.strptime(DATE_FMT)
    dt_str = date.strftime(DATE_FMT)
    dt_range = pd.date_range(end=dt_str, periods=50, freq="12M").shift(date.day, freq="D")

    # gather a big range of dates to filter the curve data
    date_ranges = [dt_range.shift(periods=-delta, freq="D") for delta in range(4)]
    ranges = functools.reduce(lambda r1, r2: r1.append(r2), date_ranges)

    # retrieve curve data, filter with date ranges, and sample by year
    curve_data = download()
    curve_data = curve_data[curve_data.index.isin(ranges)]
    curve_years = curve_data.groupby(curve_data.index.year)
    year_samples = curve_years.apply(lambda year: year.sample(n=1))

    # clean the index
    year_samples.index = year_samples.index.set_names(["Year", "Date"])
    return year_samples.reset_index().set_index(keys="Year")


def plot(curve_data, num_years=10, start_year=None, end_year=None):
    """plot treasury curves over the past num_years. alternatively use start_year, end_year"""
    start_year = curve_data.index.min() if start_year is None else int(start_year)
    end_year = curve_data.index.max() if end_year is None else int(end_year)
    assert start_year <= end_year, "start_year must be earlier than end_year"

    # use start and end year to filter the index
    sorted = curve_data.sort_values(by="Date", ascending=False)
    filtered = sorted[(sorted.index >= start_year) & (sorted.index <= end_year)]

    # bound num years by [1, 10] and get the first num_years rows
    num_years = max(10, min(num_years, 1))
    return filtered.head(num_years)


def download():
    """retrieve all available yield curve data at treasury.gov website"""
    archive_request = requests.get(archive_url())
    archive_data = parse_csv_request(archive_request)
    current_request = requests.get(year_url(datetime.today()))
    current_data = parse_csv_request(current_request)
    all_data = pd.concat([current_data, archive_data]).set_index(keys="Date")
    all_data.index = pd.to_datetime(all_data.index)
    return all_data


def archive_url():
    """the url to the treasury.gov yield curve api"""
    last_year = (datetime.today() - relativedelta(years=1)).strftime("%Y")
    return (
        f"https://home.treasury.gov/system/files/276/yield-curve-rates-1990-{last_year}.csv"
    )


def year_url(date):
    """get csv for a single year"""
    date = date.strftime("%Y")
    return (
        "https://home.treasury.gov/resource-center/data-chart-center/"
        f"interest-rates/daily-treasury-rates.csv/{date}/all?"
        f"type=daily_treasury_yield_curve&field_tdr_date_value={date}&page&_format=csv"
    )


def parse_csv_request(request):
    return pd.read_csv(StringIO(request.text)).dropna(subset=COLUMNS)

