import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'mcp_client')))
from mcp_client.alpha_vantage_client import AlphaVantageClient

print("\U0001F9EA Testing Alpha Vantage Client")
print("="*50)

print("1. Initializing Alpha Vantage client...")
try:
    client = AlphaVantageClient()
    print("\u2705 Client initialized successfully\n")
except Exception as e:
    print(f"\u274C Failed to initialize client: {e}")
    sys.exit(1)

print("2. Testing intraday data for IBM...")
try:
    data = client.get_intraday_data('IBM', interval='5min')
    if data and 'Time Series (5min)' in data:
        print("\u2705 Intraday data retrieved successfully")
        points = len(data['Time Series (5min)'])
        print(f"   Data points: {points}")
        latest = next(iter(data['Time Series (5min)']))
        latest_data = data['Time Series (5min)'][latest]
        print(f"   Latest data: {latest} - Open: {latest_data['1. open']}, Close: {latest_data['4. close']}")
    else:
        print("\u274C Intraday data not found or malformed.")
except Exception as e:
    print(f"\u274C Error fetching intraday data: {e}")

print("\n3. Testing daily data for IBM...")
try:
    data = client.get_daily_data('IBM')
    if data and 'Time Series (Daily)' in data:
        print("\u2705 Daily data retrieved successfully")
        points = len(data['Time Series (Daily)'])
        print(f"   Data points: {points}")
    else:
        print("\u274C Daily data not found or malformed.")
except Exception as e:
    print(f"\u274C Error fetching daily data: {e}")

print("\n4. Testing company overview for IBM...")
try:
    data = client.get_company_overview('IBM')
    if data and 'Name' in data:
        print("\u2705 Company overview retrieved successfully")
        print(f"   Company: {data.get('Name')}")
        print(f"   Sector: {data.get('Sector')}")
        print(f"   Market Cap: {data.get('MarketCapitalization')}")
    else:
        print("\u274C Company overview not found or malformed.")
except Exception as e:
    print(f"\u274C Error fetching company overview: {e}")

print("\n\U0001F389 All tests completed!") 