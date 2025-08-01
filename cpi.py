import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from typing import Literal
from copy import deepcopy


def compound_growth(
    principal: float,
    annual_rate: float = 0.05,
    dividend_per_period: float = 0.0,
    period_per_year: Literal[1, 2, 4, 12] = 4,
    years: int = 30,
    mode: Literal["rate", "dividend"] = "rate"
):
    periods = years * period_per_year
    time_points = np.arange(0, periods + 1)
    asset_values = [principal]

    for t in range(1, periods + 1):
        current_value = asset_values[-1]
        if mode == "rate":
            growth = current_value * (annual_rate / period_per_year)
        elif mode == "dividend":
            growth = dividend_per_period
        asset_values.append(current_value + growth)

    df = pd.DataFrame({
        "Period": time_points,
        "Year": time_points / period_per_year,
        "Asset Value": asset_values,
        "Frequency": f"{period_per_year}x/year"
    })

    return df


def plot(df_list: list[pd.DataFrame]) -> None:
    plt.figure(figsize=(12, 6))
    for df in df_list:
        label = df["Frequency"].iloc[0]
        plt.plot(df["Year"], df["Asset Value"],
                 marker='o', label=f"{label} Compounding")

        yearly_df = df[df["Year"] == df["Year"].round()]
        plt.scatter(yearly_df["Year"], yearly_df["Asset Value"], s=20)
        for _, row in yearly_df.iterrows():
            plt.text(row["Year"], row["Asset Value"] + 50, f'{row["Asset Value"]:.0f}',
                     ha='center', va='bottom', fontsize=8, rotation=45)

    plt.title("Compound Growth Over Time")
    plt.xlabel("Year")
    plt.ylabel("Asset Value")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__":
    raise ImportError
