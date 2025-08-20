import pandas as pd

def main():
    files_path = ["data/daily_sales_data_0.csv","data/daily_sales_data_1.csv","data/daily_sales_data_2.csv"]
    df_list = [pd.read_csv(path) for path in files_path]
    merged_df = pd.concat(df_list, ignore_index=True)
    
    merged_df = merged_df[merged_df["product"] == "pink morsel"]
    merged_df["price"] = merged_df["price"].replace('[\$,]', '', regex=True).astype(float)

    merged_df["sales"] = merged_df["quantity"] * merged_df["price"]
    merged_df.drop(columns=["quantity", "price", "product"], inplace=True)

    merged_df.to_csv("output/data.csv", index=False)

if __name__ == "__main__":
    main()