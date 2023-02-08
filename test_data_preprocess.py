import pandas as pd
import pytest
from data_preprocess import (
    filter_with_date,
    sum_groupby_product_code,
    joinon_product_code,
    calculate_total_price,
)


def test_filter_with_date():
    input_column_list = ["date", "strings"]
    input_data_list = [
        ["2023-01-15", "good morning"],
        ["2023-02-08", "hello"],
        ["2023-03-8", "good night"],
    ]
    START_DATE = "2023-02-01"
    END_DATE = "2023-02-28"
    actual_df = pd.DataFrame(data=input_data_list, columns=input_column_list)
    actual_df = filter_with_date(actual_df, START_DATE, END_DATE)
    actual_df = actual_df.reset_index(drop=True)
    expected_data_list = [["2023-02-08", "hello"]]
    expected_df = pd.DataFrame(data=expected_data_list, columns=input_column_list)

    pd.testing.assert_frame_equal(left=expected_df, right=actual_df)


def test_sum_groupby_product_code():
    input_column_list = ["product_code", "quantity"]
    input_data_list = [
        ["AAAAA", 1],
        ["AAAAA", 1],
        ["AAAAA", 1],
        ["BBBBB", 1],
        ["BBBBB", 1],
        ["CCCCC", 1],
    ]
    actual_df = pd.DataFrame(data=input_data_list, columns=input_column_list)
    actual_df = sum_groupby_product_code(actual_df)
    actual_df = actual_df.reset_index(drop=False)
    expected_data_list = [
        ["AAAAA", 3],
        ["BBBBB", 2],
        ["CCCCC", 1],
    ]
    expected_df = pd.DataFrame(data=expected_data_list, columns=input_column_list)
    pd.testing.assert_frame_equal(left=expected_df, right=actual_df)


def test_joinon_product_code():
    input_left_column_list = ["product_code", "quantity"]
    input_left_data_list = [
        ["AAAAA", 3],
        ["BBBBB", 2],
        ["CCCCC", 1],
    ]
    df_left = pd.DataFrame(data=input_left_data_list, columns=input_left_column_list)

    input_right_column_list = ["product_code", "product_name"]
    input_right_data_list = [
        ["AAAAA", "name_of_AAAAA"],
        ["BBBBB", "name_of_BBBB"],
        ["CCCCC", "name_of_CCCCC"],
    ]
    df_right = pd.DataFrame(data=input_right_data_list, columns=input_right_column_list)
    actual_df = joinon_product_code(df_left, df_right)
    actual_df = actual_df.reset_index(drop=True)
    expected_column_list = ["product_code", "quantity", "product_name"]
    expected_data_list = [
        ["AAAAA", 3, "name_of_AAAAA"],
        ["BBBBB", 2, "name_of_BBBB"],
        ["CCCCC", 1, "name_of_CCCCC"],
    ]
    expected_df = pd.DataFrame(data=expected_data_list, columns=expected_column_list)
    pd.testing.assert_frame_equal(left=expected_df, right=actual_df)


def test_calculate_total_price():
    input_column_list = ["quantity", "unit_price"]
    input_data_list = [
        [3, 100],
        [2, 5],
        [1, 1000],
    ]
    actual_df = pd.DataFrame(data=input_data_list, columns=input_column_list)
    actual_df = calculate_total_price(actual_df)
    expected_column_list = ["quantity", "unit_price", "total_price"]
    expected_data_list = [
        [3, 100, 300],
        [2, 5, 10],
        [1, 1000, 1000],
    ]
    expected_df = pd.DataFrame(data=expected_data_list, columns=expected_column_list)
    print(expected_df.head())
    print(actual_df.head())
