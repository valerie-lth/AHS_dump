import pandas as pd 
import numpy as np
import os
import matplotlib.pyplot as plt

if __name__ == '__main__':

    acr_df = pd.read_csv("ACR_Cohort_All_Cancers_2010_2020.csv", low_memory=False)
    # print(acr_df.columns)
    # di contains outlier
    di_df = pd.read_csv("query_output_final_xlsx.csv", low_memory=False)
    di_df = di_df[pd.to_datetime(di_df["Study Date"]).dt.year > 2000]
    # print(di_df.columns)

    di_df = di_df[["ULI", "Study Date"]]
    di_df.rename(columns={"ULI":"uli"}, inplace=True)
    acr_df = acr_df[["uli", "diag_dte"]]

    final_df = pd.merge(acr_df, di_df, on="uli")
    print(final_df[:20])
    # print(pd.to_datetime(final_df["diag_dte"][:10]).dt.year)
    # print(pd.to_datetime(final_df["Study Date"][:10]).dt.year)
    final_df["date_difference"] = (pd.to_datetime(final_df["Study Date"]) - pd.to_datetime(final_df["diag_dte"])).dt.days

    plt.hist(final_df["date_difference"], bins=50)
    plt.title("Distribution of Diag/Study Date Difference")
    plt.xlabel('Date Difference (days)')
    plt.ylabel("Frequency")
    plt.savefig("date_freq.png")