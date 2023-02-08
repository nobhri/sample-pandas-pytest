import pandas as pd

START_DATE = "2023-02-01"
END_DATE = "2023-02-28"
TRANSACTION_DATA_PATH = "./input_data_transaction.csv"
MASTER_DATA_PATH = "./input_data_master.csv"
OUTPUT_DATA_PATH = "./output_data.csv"


def filter_with_date(df, start_date, end_date):
    df = df[df["date"].between(start_date, end_date)]
    return df


def sum_groupby_product_code(df):
    df = df.groupby("product_code").sum("quantity")
    return df


def joinon_product_code(df_left, df_right):
    df = pd.merge(left=df_left, right=df_right, how="left", on="product_code")
    return df


def calculate_total_price(df):
    df["total_price"] = df["quantity"] * df["unit_price"]
    return df


if __name__ == "__main__":
    df_tran = pd.read_csv(TRANSACTION_DATA_PATH)
    df_mst = pd.read_csv(MASTER_DATA_PATH)
    df_tran = filter_with_date(df_tran, START_DATE, END_DATE)
    df_tran = sum_groupby_product_code(df_tran)
    df_join = joinon_product_code(df_tran, df_mst)
    df_join = calculate_total_price(df_join)
    df_join.to_csv(OUTPUT_DATA_PATH)
