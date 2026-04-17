import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# STEP 1: Define stocks
# -------------------------------
stocks = ["TCS.NS", "RELIANCE.NS", "HDFCBANK.NS", "INFY.NS"]

data = {}

# -------------------------------
# STEP 2: Download + Process Data
# -------------------------------
for stock in stocks:
    print(f"Downloading {stock}...")

    df = yf.download(
        stock,
        start="2020-01-01",
        end="2026-03-01",
        auto_adjust=True  # Fix warning
    )

    # Check if data is empty
    if df.empty:
        print(f"⚠️ No data for {stock}")
        continue

    # Clean data
    df = df.ffill()

    # -------------------------------
    # Feature Engineering
    # -------------------------------
    df['MA_7'] = df['Close'].rolling(7).mean()
    df['MA_30'] = df['Close'].rolling(30).mean()
    df['Returns'] = df['Close'].pct_change()
    df['Volatility'] = df['Returns'].rolling(30).std()

    df.dropna(inplace=True)

    data[stock] = df

# -------------------------------
# STEP 3: Combine Close Prices
# -------------------------------
combined_close = pd.concat(
    [data[stock]['Close'] for stock in data.keys()],
    axis=1
)

combined_close.columns = list(data.keys())

print("\nCombined Data Preview:")
print(combined_close.head())

# -------------------------------
# STEP 4: Price Comparison
# -------------------------------
plt.figure(figsize=(12,6))

for stock in data.keys():
    plt.plot(combined_close[stock], label=stock)

plt.title("Stock Price Comparison")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

# -------------------------------
# STEP 5: Normalized Performance
# -------------------------------
normalized = combined_close / combined_close.iloc[0] * 100

plt.figure(figsize=(12,6))

for stock in data.keys():
    plt.plot(normalized[stock], label=stock)

plt.title("Normalized Performance (Base = 100)")
plt.xlabel("Date")
plt.ylabel("Growth (%)")
plt.legend()
plt.show()

# -------------------------------
# STEP 6: Cumulative Returns
# -------------------------------
cumulative_returns = (1 + combined_close.pct_change()).cumprod()

plt.figure(figsize=(12,6))

for stock in data.keys():
    plt.plot(cumulative_returns[stock], label=stock)

plt.title("Cumulative Returns")
plt.xlabel("Date")
plt.ylabel("Growth")
plt.legend()
plt.show()

# -------------------------------
# STEP 7: Daily Returns
# -------------------------------
plt.figure(figsize=(12,6))

for stock in data.keys():
    plt.plot(data[stock]['Returns'], label=stock)

plt.title("Daily Returns")
plt.xlabel("Date")
plt.ylabel("Returns")
plt.legend()
plt.show()

# -------------------------------
# STEP 8: Volatility (Risk)
# -------------------------------
plt.figure(figsize=(12,6))

for stock in data.keys():
    plt.plot(data[stock]['Volatility'], label=stock)

plt.title("Volatility Comparison (Risk)")
plt.xlabel("Date")
plt.ylabel("Volatility")
plt.legend()
plt.show()

# -------------------------------
# STEP 9: Correlation Heatmap
# -------------------------------
returns_df = combined_close.pct_change()

plt.figure(figsize=(8,6))
sns.heatmap(returns_df.corr(), annot=True, cmap="coolwarm")

plt.title("Stock Correlation Heatmap")
plt.show()

# -------------------------------
# STEP 10: Summary Table
# -------------------------------
summary = pd.DataFrame({
    "Stock": list(data.keys()),
    "Average Return": [data[s]['Returns'].mean() for s in data.keys()],
    "Volatility": [data[s]['Volatility'].mean() for s in data.keys()]
})

print("\nSummary Analysis:")
print(summary)