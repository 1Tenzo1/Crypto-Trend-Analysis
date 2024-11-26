import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Step 1: Fetch Data from CoinGecko API
def fetch_crypto_data(crypto_id, days='30', interval='daily'):
    url = f'https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart'
    params = {
        'vs_currency': 'usd',
        'days': days,
        'interval': interval
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None


# Step 2: Process Data
def process_data(data):
    df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df


# Step 3: Plot Price Trend
def plot_price_trend(df, crypto_name):
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['price'], label='Price (USD)', color='blue')
    plt.title(f'{crypto_name} Price Trend')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()


# Step 4: Calculate and Plot Volatility
def plot_volatility(df, crypto_name):
    df['daily_return'] = df['price'].pct_change()
    plt.figure(figsize=(10, 5))
    sns.histplot(df['daily_return'].dropna(), bins=50, kde=True, color='purple')
    plt.title(f'{crypto_name} Daily Return Volatility')
    plt.xlabel('Daily Return')
    plt.ylabel('Frequency')
    plt.show()


# Step 5: Compare Two Cryptocurrencies
def compare_two_cryptos(crypto1, crypto2, days='30'):
    data1 = fetch_crypto_data(crypto1, days)
    data2 = fetch_crypto_data(crypto2, days)

    if data1 and data2:
        df1 = process_data(data1)
        df2 = process_data(data2)

        plt.figure(figsize=(10, 6))
        plt.plot(df1.index, df1['price'], label=crypto1.capitalize(), color='green')
        plt.plot(df2.index, df2['price'], label=crypto2.capitalize(), color='orange')
        plt.title(f'Price Comparison: {crypto1.capitalize()} vs {crypto2.capitalize()}')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        print("Failed to fetch data for one or both cryptocurrencies.")


# Step 6: Main Function
def main():
    crypto_id = input("Enter the cryptocurrency ID (e.g., bitcoin, ethereum, solana): ").lower()
    days = input("Enter the number of days for analysis (e.g., 7, 30, 90): ")

    data = fetch_crypto_data(crypto_id, days)
    if data:
        df = process_data(data)
        plot_price_trend(df, crypto_id.capitalize())
        plot_volatility(df, crypto_id.capitalize())

        compare_choice = input("Do you want to compare this with another cryptocurrency? (yes/no): ").lower()
        if compare_choice == 'yes':
            crypto2_id = input("Enter the second cryptocurrency ID: ").lower()
            compare_two_cryptos(crypto_id, crypto2_id, days)
    else:
        print("Failed to fetch cryptocurrency data.")


# Run the main function
if __name__ == "__main__":
    main()
