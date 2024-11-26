# Cryptocurrency Data Analysis Tool

This Python project fetches, analyzes, and visualizes cryptocurrency price data using the CoinGecko API. It helps users examine trends, assess volatility, and compare the performance of two cryptocurrencies over a customizable period.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [License](#license)

---

## Features

- **Fetch Historical Data:** Retrieve historical price data for any cryptocurrency listed on CoinGecko.
- **Visualize Price Trends:** Plot price trends over customizable time periods.
- **Analyze Volatility:** Assess daily return volatility with histogram plots.
- **Compare Cryptocurrencies:** Compare the price performance of two cryptocurrencies side-by-side.

---

## Prerequisites

Ensure you have the following Python libraries installed:

- `requests`
- `pandas`
- `matplotlib`
- `seaborn`

To install these libraries, run:

```bash
  pip install requests pandas matplotlib seaborn
```
Installation
Clone the repository:

```bash
  git clone https://github.com/your-username/crypto-analysis-tool.git
```
cd crypto-analysis-tool
Ensure the required libraries are installed (see Prerequisites).

Usage
Run the script:
```bash
python main.py
```
Follow the prompts:

Enter the cryptocurrency ID (e.g., bitcoin, ethereum, solana).
Specify the number of days for analysis (7, 30, 90, etc.).
Optionally compare two cryptocurrencies.

Example
Analyzing Bitcoin for 30 days:

```bash
Enter the cryptocurrency ID (e.g., bitcoin, ethereum, solana): bitcoin
Enter the number of days for analysis (e.g., 7, 30, 90): 30
```
Comparing Bitcoin and Ethereum:

```bash
Do you want to compare this with another cryptocurrency? (yes/no): yes
Enter the second cryptocurrency ID: ethereum
```
CoinGecko API
This tool uses the free CoinGecko API to fetch cryptocurrency data. You can learn more about the API here [https://api.coingecko.com/api/v3/coins/{id}/market_chart]. 

Contributing
Contributions are welcome! Please open an issue to discuss changes or improvements.
