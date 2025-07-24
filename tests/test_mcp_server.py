import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'mcp-server')))
import mcp_server.stock_analytics_server as sas

print("\U0001F9EA Testing MCP Server Functions")
print("="*50)

print("1. Testing get_stock_intraday_data for IBM...")
try:
    result = sas.get_stock_intraday_data('IBM', '5min')
    if result.get('status') == 'success':
        print("\u2705 Intraday data retrieved successfully")
        print(f"   Symbol: {result.get('symbol')}")
    else:
        print(f"\u274C Error: {result.get('message', 'Unknown error')}")
except Exception as e:
    print(f"\u274C Exception: {e}")

print("\n2. Testing get_stock_daily_data for IBM...")
try:
    result = sas.get_stock_daily_data('IBM')
    if result.get('status') == 'success':
        print("\u2705 Daily data retrieved successfully")
        print(f"   Symbol: {result.get('symbol')}")
    else:
        print(f"\u274C Error: {result.get('message', 'Unknown error')}")
except Exception as e:
    print(f"\u274C Exception: {e}")

print("\n3. Testing get_company_overview for IBM...")
try:
    result = sas.get_company_overview('IBM')
    if result.get('status') == 'success':
        print("\u2705 Company overview retrieved successfully")
        print(f"   Symbol: {result.get('symbol')}")
        print(f"   Name: {result.get('Name', 'N/A')}")
    else:
        print(f"\u274C Error: {result.get('message', 'Unknown error')}")
except Exception as e:
    print(f"\u274C Exception: {e}")

print("\n4. Testing calculate_stock_metrics...")
try:
    prices = [100, 102, 101, 99, 98, 105]
    result = sas.calculate_stock_metrics(prices)
    if isinstance(result, dict):
        print("\u2705 Stock metrics calculated successfully")
        print(f"   Mean: {result.get('mean_price')}")
        print(f"   Min: {result.get('min_price')}")
        print(f"   Max: {result.get('max_price')}")
        print(f"   Volatility: {result.get('volatility')}")
        print(f"   Price Range: {result.get('price_range')}")
    else:
        print("\u274C Unexpected result format.")
except Exception as e:
    print(f"\u274C Exception: {e}")

print("\n\U0001F389 All tests completed!") 