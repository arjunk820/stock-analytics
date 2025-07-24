import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

import argparse
from mcp_server import stock_analytics_server as sas

# -----------------------------
# CLI Tool for Stock Analytics
# -----------------------------
# This script lets you call the main analytics functions from the terminal.
# Each command maps to a function in the server.

# Create the main parser
def main():
    parser = argparse.ArgumentParser(
        description="Stock Analytics CLI - Query stock data and analytics from your terminal!"
    )
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # Subparser for 'intraday' command
    intraday_parser = subparsers.add_parser("intraday", help="Get intraday stock data")
    intraday_parser.add_argument("--symbol", required=True, help="Stock symbol, e.g. IBM, AAPL, MSFT")
    intraday_parser.add_argument("--interval", default="60n", help="Interval (1min, 5min, 15min, 30min, 60min)")

    # Subparser for 'daily' command
    daily_parser = subparsers.add_parser("daily", help="Get daily stock data")
    daily_parser.add_argument("--symbol", required=True, help="Stock symbol, e.g. IBM")

    # Subparser for 'overview' command
    overview_parser = subparsers.add_parser("overview", help="Get company overview")
    overview_parser.add_argument("--symbol", required=True, help="Stock symbol, e.g. IBM")

    # Subparser for 'metrics' command
    metrics_parser = subparsers.add_parser("metrics", help="Calculate stock metrics from prices")
    metrics_parser.add_argument("--prices", nargs='+', type=float, required=True, help="List of prices, e.g. 100 102 101 99 98 105")

    args = parser.parse_args()

    # Handle each command
    if args.command == "intraday":
        result = sas.get_stock_intraday_data(args.symbol, args.interval)
        print_result(result)
    elif args.command == "daily":
        result = sas.get_stock_daily_data(args.symbol)
        print_result(result)
    elif args.command == "overview":
        result = sas.get_company_overview(args.symbol)
        print_result(result)
    elif args.command == "metrics":
        result = sas.calculate_stock_metrics(args.prices)
        print_result(result)
    else:
        parser.print_help()

# Helper function to print results nicely
def print_result(result):
    import json
    print("\n--- Result ---")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main() 