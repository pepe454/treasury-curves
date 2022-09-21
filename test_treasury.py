from unittest import mock

import numpy as np
import pandas as pd
import pytest

import treasury


@pytest.fixture
def curve_data():
    # all days in the past 30 years (365 * 30 = 10950)
    date_range = pd.date_range(end="2020-02-15", periods=10950, freq="D")
    curve_data = pd.DataFrame(data={"Date": date_range})
    curve_data["Date"] = pd.to_datetime(curve_data["Date"])
    curve_data = curve_data.set_index("Date")
    curve_data["1 Yr"] = 0.4
    curve_data["2 Yr"] = 0.5
    curve_data["5 Yr"] = 0.75
    curve_data["10 Yr"] = 1
    curve_data["20 Yr"] = 1.1
    curve_data["30 Yr"] = 1.5
    return curve_data


def test_curves(curve_data):
    # mock download to guarantee consistency
    original_download = treasury.download
    treasury.download = mock.MagicMock(return_value=curve_data)
    max_date = curve_data.index.max()
    test_date = max_date.strftime(treasury.DATE_FMT)
    curves = treasury.curves(test_date, False)

    # curves should group data by year and randomly select 1 sample per year
    assert curves.index.is_unique

    # dates should be around the time of the testing date
    curves["Date"] = pd.to_datetime(curves["Date"])
    day_min, day_max = max_date.day - 5, max_date.day + 5
    assert np.all(curves["Date"].dt.day < day_max)
    assert np.all(curves["Date"].dt.day > day_min)
    assert np.all(curves["Date"].dt.month == max_date.month)

    # un-mock the download
    treasury.download = original_download


def test_filter_curves(curve_data):
    curve_data = curve_data.reset_index()
    curve_data["Year"] = curve_data["Date"].dt.year
    curve_data = curve_data.set_index("Year")

    # use num_years alone
    for years in [1,2,3,4,5,6,7,8]:
        numyears_only = treasury.filter_curves(curve_data, num_years=years)
        minyear = pd.to_numeric(numyears_only.index.max()) - years
        assert np.all(numyears_only.index >= minyear)

    # now go outside bounds [1,10] --> filter should coerce to bounds [1,10]
    negatives = treasury.filter_curves(curve_data, num_years=-20)
    negative_minyear = pd.to_numeric(numyears_only.index.max()) - 1
    assert np.all(negatives.index >= negative_minyear)

    too_large = treasury.filter_curves(curve_data, num_years=50)
    too_large_minyear = pd.to_numeric(numyears_only.index.max()) - 10
    assert np.all(too_large.index >= too_large_minyear)

    # use start date only
    for years in [1,2,3,4,5,10]:
        start = curve_data.index.min() + years
        end = start + 10
        start_only = treasury.filter_curves(curve_data, start_year=start)
        assert np.all((start_only.index >= start) & (start_only.index <= end))

    # use end date only
    for years in [1,2,3,4,5,10]:
        end = curve_data.index.max() - years
        start = end - 10
        end_only = treasury.filter_curves(curve_data, end_year=end)
        assert np.all((end_only.index >= start) & (end_only.index <= end))

    # now combination of start and end
    start, end = curve_data.index.min() + 2, curve_data.index.max() - 2
    start_end = treasury.filter_curves(curve_data, start_year=start, end_year=end)
    assert np.all((start_end.index >= start) & (start_end.index <= end))

    # combination of start, end, and num_years
    actual_start = end - 5
    start_end = treasury.filter_curves(curve_data, start_year=start, end_year=end, num_years=5)
    assert np.all((start_end.index >= actual_start) & (start_end.index <= end))
